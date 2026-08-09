from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Any, Iterable

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

PROHIBITED_RAW_KEYS = {
    "address",
    "authentication_token",
    "bank_account_number",
    "chat_log",
    "conversation_id",
    "credit_card_number",
    "email",
    "government_id",
    "medical_record",
    "password",
    "phone",
    "private_message",
    "private_note",
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON value must be an object")
    return value


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = yaml.safe_load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level YAML value must be a mapping")
    return value


def load_event_type_ids(ontology_path: Path) -> set[str]:
    ontology = load_yaml(ontology_path)
    entries = ontology.get("event_types")
    if not isinstance(entries, list):
        raise ValueError(f"{ontology_path}: event_types must be a list")

    ids: list[str] = []
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict) or not isinstance(entry.get("id"), str):
            raise ValueError(f"{ontology_path}: event_types[{index}] requires a string id")
        ids.append(entry["id"])

    duplicates = sorted({event_id for event_id in ids if ids.count(event_id) > 1})
    if duplicates:
        raise ValueError(f"{ontology_path}: duplicate event type id(s): {', '.join(duplicates)}")
    return set(ids)


def _build_validator(schema_path: Path, event_schema_path: Path) -> Draft202012Validator:
    record_schema = load_json(schema_path)
    event_schema = load_json(event_schema_path)
    event_schema_id = event_schema.get("$id")
    if not isinstance(event_schema_id, str):
        raise ValueError(f"{event_schema_path}: schema requires a string $id")

    registry = Registry().with_resource(
        event_schema_id,
        Resource.from_contents(event_schema),
    )
    return Draft202012Validator(
        record_schema,
        registry=registry,
        format_checker=FormatChecker(),
    )


def _format_json_path(parts: Iterable[Any]) -> str:
    path = "$"
    for part in parts:
        if isinstance(part, int):
            path += f"[{part}]"
        else:
            path += f".{part}"
    return path


def _walk_prohibited_keys(value: Any, path: str = "$") -> list[str]:
    issues: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if key.lower() in PROHIBITED_RAW_KEYS:
                issues.append(
                    f"{child_path}: prohibited raw identifier, secret, or private-correspondence field name"
                )
            issues.extend(_walk_prohibited_keys(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            issues.extend(_walk_prohibited_keys(child, f"{path}[{index}]"))
    return issues


def _parse_date(value: str, label: str, issues: list[str]) -> date | None:
    try:
        return date.fromisoformat(value)
    except (TypeError, ValueError):
        issues.append(f"{label}: expected ISO date")
        return None


def validate_record_data(
    record: dict[str, Any],
    *,
    validator: Draft202012Validator,
    event_type_ids: set[str],
) -> list[str]:
    issues: list[str] = []

    for error in sorted(validator.iter_errors(record), key=lambda item: list(item.absolute_path)):
        issues.append(f"{_format_json_path(error.absolute_path)}: {error.message}")

    issues.extend(_walk_prohibited_keys(record))

    governance = record.get("data_governance", {})
    if governance.get("contains_repository_owner_data") is not False:
        issues.append("$.data_governance.contains_repository_owner_data must be false")
    if governance.get("derived_from_owner_private_communications") is not False:
        issues.append(
            "$.data_governance.derived_from_owner_private_communications must be false"
        )

    events = record.get("events")
    if not isinstance(events, list):
        return issues

    event_by_id: dict[str, dict[str, Any]] = {}
    for index, event in enumerate(events):
        if not isinstance(event, dict):
            continue
        event_id = event.get("event_id")
        event_type = event.get("event_type")
        if isinstance(event_id, str):
            if event_id in event_by_id:
                issues.append(f"$.events[{index}].event_id: duplicate event id {event_id!r}")
            else:
                event_by_id[event_id] = event
        if isinstance(event_type, str) and event_type not in event_type_ids:
            issues.append(f"$.events[{index}].event_type: unknown ontology id {event_type!r}")

    prediction = record.get("prediction_context", {})
    cutoff_raw = prediction.get("cutoff_date")
    cutoff = (
        _parse_date(cutoff_raw, "$.prediction_context.cutoff_date", issues)
        if isinstance(cutoff_raw, str)
        else None
    )
    permitted = prediction.get("permitted_event_ids", [])
    hidden = prediction.get("hidden_future_event_ids", [])

    if isinstance(permitted, list) and isinstance(hidden, list):
        overlap = sorted(set(permitted).intersection(hidden))
        if overlap:
            issues.append(
                "$.prediction_context: permitted and hidden event ids overlap: "
                + ", ".join(overlap)
            )

        for category, event_ids in (
            ("permitted_event_ids", permitted),
            ("hidden_future_event_ids", hidden),
        ):
            for event_id in event_ids:
                if event_id not in event_by_id:
                    issues.append(
                        f"$.prediction_context.{category}: unknown event id {event_id!r}"
                    )

        if cutoff is not None:
            for event_id in permitted:
                event = event_by_id.get(event_id)
                if not event or not isinstance(event.get("start_date"), str):
                    continue
                event_date = _parse_date(
                    event["start_date"],
                    f"$.events[{event_id}].start_date",
                    issues,
                )
                if event_date is not None and event_date > cutoff:
                    issues.append(
                        f"$.prediction_context.permitted_event_ids: {event_id!r} occurs after cutoff"
                    )
            for event_id in hidden:
                event = event_by_id.get(event_id)
                if not event or not isinstance(event.get("start_date"), str):
                    continue
                event_date = _parse_date(
                    event["start_date"],
                    f"$.events[{event_id}].start_date",
                    issues,
                )
                if event_date is not None and event_date <= cutoff:
                    issues.append(
                        f"$.prediction_context.hidden_future_event_ids: {event_id!r} is not after cutoff"
                    )

    if record.get("synthetic") is True:
        birth_provenance = record.get("birth", {}).get("provenance", {})
        if birth_provenance.get("source_type") != "synthetic":
            issues.append("$.birth.provenance.source_type must be synthetic for synthetic records")
        for index, event in enumerate(events):
            if (
                isinstance(event, dict)
                and event.get("provenance", {}).get("source_type") != "synthetic"
            ):
                issues.append(
                    f"$.events[{index}].provenance.source_type must be synthetic for synthetic records"
                )

    return sorted(set(issues))


def validate_record_file(
    record_path: Path,
    *,
    schema_path: Path,
    event_schema_path: Path,
    ontology_path: Path,
) -> list[str]:
    validator = _build_validator(schema_path, event_schema_path)
    event_type_ids = load_event_type_ids(ontology_path)
    record = load_json(record_path)
    return validate_record_data(
        record,
        validator=validator,
        event_type_ids=event_type_ids,
    )
