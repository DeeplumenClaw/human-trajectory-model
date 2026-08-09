from __future__ import annotations

import json
import math
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any

from .validation import load_json, load_yaml, validate_record_file


def _target_for_record(record: dict[str, Any]) -> str:
    cutoff = date.fromisoformat(record["prediction_context"]["cutoff_date"])
    hidden_ids = set(record["prediction_context"]["hidden_future_event_ids"])
    candidates: list[tuple[date, str]] = []
    for event in record["events"]:
        if event["event_id"] not in hidden_ids or event["start_date"] is None:
            continue
        event_date = date.fromisoformat(event["start_date"])
        if event_date > cutoff:
            candidates.append((event_date, event["event_type"]))
    if not candidates:
        raise ValueError(f"{record['record_id']}: no hidden event after cutoff")
    candidates.sort(key=lambda item: item[0])
    return candidates[0][1]


def run_benchmark(
    task_path: Path,
    *,
    schema_path: Path,
    event_schema_path: Path,
    ontology_path: Path,
) -> dict[str, Any]:
    task = load_yaml(task_path)
    if task.get("target", {}).get("type") != "next_event_type":
        raise ValueError("Only target.type=next_event_type is implemented in v0.1")
    if task.get("baseline", {}).get("type") != "global_frequency":
        raise ValueError("Only baseline.type=global_frequency is implemented in v0.1")

    task_root = task_path.parent.parent.parent
    record_paths = [task_root / item for item in task["dataset"]["records"]]
    records: dict[str, dict[str, Any]] = {}
    for record_path in record_paths:
        issues = validate_record_file(
            record_path,
            schema_path=schema_path,
            event_schema_path=event_schema_path,
            ontology_path=ontology_path,
        )
        if issues:
            joined = "\n".join(f"- {issue}" for issue in issues)
            raise ValueError(f"{record_path} failed validation:\n{joined}")
        record = load_json(record_path)
        records[record["record_id"]] = record

    train_ids = task["split"]["train_record_ids"]
    test_ids = task["split"]["test_record_ids"]
    allowed = task["target"]["allowed_event_types"]
    if not allowed or len(set(allowed)) != len(allowed):
        raise ValueError("target.allowed_event_types must contain unique values")

    missing = [record_id for record_id in train_ids + test_ids if record_id not in records]
    if missing:
        raise ValueError(f"Task references missing record id(s): {', '.join(missing)}")

    train_targets = [_target_for_record(records[record_id]) for record_id in train_ids]
    test_targets = [_target_for_record(records[record_id]) for record_id in test_ids]
    unknown_targets = sorted(set(train_targets + test_targets).difference(allowed))
    if unknown_targets:
        raise ValueError(f"Targets outside allowed_event_types: {', '.join(unknown_targets)}")

    alpha = float(task["baseline"].get("laplace_alpha", 1.0))
    if alpha <= 0:
        raise ValueError("baseline.laplace_alpha must be positive")

    counts = Counter(train_targets)
    denominator = len(train_targets) + alpha * len(allowed)
    probabilities = {
        label: (counts.get(label, 0) + alpha) / denominator
        for label in allowed
    }
    predicted_label = max(allowed, key=lambda label: (probabilities[label], label))

    accuracy = sum(target == predicted_label for target in test_targets) / len(test_targets)
    log_loss = -sum(math.log(probabilities[target]) for target in test_targets) / len(test_targets)
    brier = 0.0
    for target in test_targets:
        brier += sum(
            (probabilities[label] - (1.0 if label == target else 0.0)) ** 2
            for label in allowed
        )
    brier /= len(test_targets)

    return {
        "task_id": task["id"],
        "status": task.get("status"),
        "implementation_version": "0.1.0",
        "baseline": {
            "type": "global_frequency",
            "laplace_alpha": alpha,
            "train_target_counts": dict(sorted(counts.items())),
            "probabilities": probabilities,
            "predicted_label": predicted_label,
        },
        "evaluation": {
            "train_records": len(train_ids),
            "test_records": len(test_ids),
            "test_targets": test_targets,
            "metrics": {
                "accuracy": accuracy,
                "log_loss": log_loss,
                "multiclass_brier": brier,
            },
        },
        "disclaimer": task.get("disclaimer"),
    }


def result_as_json(result: dict[str, Any]) -> str:
    return json.dumps(result, indent=2, sort_keys=True)
