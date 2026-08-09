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


def test_repository_owner_data_flag_is_rejected() -> None:
    record = copy.deepcopy(load_json(EXAMPLE))
    record["data_governance"]["contains_repository_owner_data"] = True
    issues = _issues_for(record)
    assert any("contains_repository_owner_data" in issue for issue in issues)


def test_owner_private_communication_flag_is_rejected() -> None:
    record = copy.deepcopy(load_json(EXAMPLE))
    record["data_governance"]["derived_from_owner_private_communications"] = True
    issues = _issues_for(record)
    assert any("derived_from_owner_private_communications" in issue for issue in issues)


def test_public_record_basis_is_allowed_for_a_third_party() -> None:
    record = copy.deepcopy(load_json(EXAMPLE))
    record["entity_type"] = "public_figure"
    record["synthetic"] = False
    record["public_name"] = "Public Example"
    record["data_governance"] = {
        "source_scope": "public_record",
        "authorization_basis": "public_record",
        "contains_repository_owner_data": False,
        "derived_from_owner_private_communications": False,
        "license": "CC-BY-4.0",
        "review_status": "reviewed",
    }
    record["birth"]["confidence_grade"] = "A"
    record["birth"]["provenance"] = {
        "source_type": "official_record",
        "citation": "https://example.org/public-record",
        "accessed_at": "2026-08-09",
    }
    for event in record["events"]:
        event["evidence_confidence"] = "high"
        event["provenance"] = {
            "source_type": "reputable_secondary",
            "citation": f"https://example.org/{event['event_id']}",
            "accessed_at": "2026-08-09",
        }
        event["label_eligibility"] = "test"

    assert _issues_for(record) == []


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


def test_prohibited_raw_field_name_is_rejected() -> None:
    record = copy.deepcopy(load_json(EXAMPLE))
    record["events"][0]["attributes"]["private_note"] = "do not store"
    issues = _issues_for(record)
    assert any("prohibited raw identifier" in issue for issue in issues)
