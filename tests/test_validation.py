from __future__ import annotations

import copy
from pathlib import Path

from htm.validation import (
    _build_validator,
    load_event_type_ids,
    load_json,
    validate_record_data,
    validate_record_file,
)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas/trajectory-record.schema.json"
EVENT_SCHEMA = ROOT / "schemas/life-event.schema.json"
ONTOLOGY = ROOT / "ontology/event-types.yaml"
EXAMPLE = ROOT / "examples/synthetic/trajectory_001.json"


def _issues_for(record: dict) -> list[str]:
    return validate_record_data(
        record,
        validator=_build_validator(SCHEMA, EVENT_SCHEMA),
        event_type_ids=load_event_type_ids(ONTOLOGY),
    )


def test_synthetic_example_is_valid() -> None:
    assert validate_record_file(
        EXAMPLE,
        schema_path=SCHEMA,
        event_schema_path=EVENT_SCHEMA,
        ontology_path=ONTOLOGY,
    ) == []


def test_private_conversation_flag_is_rejected() -> None:
    record = copy.deepcopy(load_json(EXAMPLE))
    record["data_governance"]["contains_private_conversation_data"] = True
    issues = _issues_for(record)
    assert any("contains_private_conversation_data" in issue for issue in issues)


def test_unknown_event_type_is_rejected() -> None:
    record = copy.deepcopy(load_json(EXAMPLE))
    record["events"][0]["event_type"] = "unknown.private_claim"
    issues = _issues_for(record)
    assert any("unknown ontology id" in issue for issue in issues)


def test_future_event_cannot_be_permitted_history() -> None:
    record = copy.deepcopy(load_json(EXAMPLE))
    record["prediction_context"]["permitted_event_ids"].append("e05")
    issues = _issues_for(record)
    assert any("occurs after cutoff" in issue for issue in issues)


def test_prohibited_private_field_name_is_rejected() -> None:
    record = copy.deepcopy(load_json(EXAMPLE))
    record["events"][0]["attributes"]["private_note"] = "do not store"
    issues = _issues_for(record)
    assert any("prohibited private-data field" in issue for issue in issues)
