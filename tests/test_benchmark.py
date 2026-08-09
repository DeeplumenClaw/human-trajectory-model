from pathlib import Path

from htm.benchmark import run_benchmark

ROOT = Path(__file__).resolve().parents[1]


def test_synthetic_benchmark_runs_end_to_end() -> None:
    result = run_benchmark(
        ROOT / "benchmark/tasks/next-event-synthetic-v0.1.yaml",
        schema_path=ROOT / "schemas/trajectory-record.schema.json",
        event_schema_path=ROOT / "schemas/life-event.schema.json",
        ontology_path=ROOT / "ontology/event-types.yaml",
    )
    assert result["task_id"] == "htm.synthetic.next_event_type.v0.1"
    assert result["status"] == "infrastructure_only"
    assert result["evaluation"]["train_records"] == 4
    assert result["evaluation"]["test_records"] == 2
    metrics = result["evaluation"]["metrics"]
    assert 0.0 <= metrics["accuracy"] <= 1.0
    assert metrics["log_loss"] >= 0.0
    assert metrics["multiclass_brier"] >= 0.0
