from __future__ import annotations

import argparse
import glob
import sys
from pathlib import Path
from typing import Sequence

from .benchmark import result_as_json, run_benchmark
from .validation import validate_record_file

DEFAULT_SCHEMA = Path("schemas/trajectory-record.schema.json")
DEFAULT_EVENT_SCHEMA = Path("schemas/life-event.schema.json")
DEFAULT_ONTOLOGY = Path("ontology/event-types.yaml")


def _expand_paths(values: Sequence[str]) -> list[Path]:
    paths: list[Path] = []
    for value in values:
        matches = sorted(glob.glob(value))
        if matches:
            paths.extend(Path(match) for match in matches)
        else:
            paths.append(Path(value))
    return paths


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="htm",
        description="HTM schema validation and benchmark starter tools",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate", help="validate trajectory JSON records")
    validate.add_argument("records", nargs="+", help="record paths or glob patterns")
    validate.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    validate.add_argument("--event-schema", type=Path, default=DEFAULT_EVENT_SCHEMA)
    validate.add_argument("--ontology", type=Path, default=DEFAULT_ONTOLOGY)

    benchmark = subparsers.add_parser("benchmark", help="run a benchmark task")
    benchmark.add_argument("task", type=Path)
    benchmark.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    benchmark.add_argument("--event-schema", type=Path, default=DEFAULT_EVENT_SCHEMA)
    benchmark.add_argument("--ontology", type=Path, default=DEFAULT_ONTOLOGY)
    return parser


def _run_validate(args: argparse.Namespace) -> int:
    record_paths = _expand_paths(args.records)
    passed = 0
    failed = 0
    for record_path in record_paths:
        if not record_path.exists():
            print(f"FAIL {record_path}", file=sys.stderr)
            print("  - file does not exist", file=sys.stderr)
            failed += 1
            continue
        try:
            issues = validate_record_file(
                record_path,
                schema_path=args.schema,
                event_schema_path=args.event_schema,
                ontology_path=args.ontology,
            )
        except (OSError, ValueError) as exc:
            print(f"FAIL {record_path}", file=sys.stderr)
            print(f"  - {exc}", file=sys.stderr)
            failed += 1
            continue
        if issues:
            print(f"FAIL {record_path}", file=sys.stderr)
            for issue in issues:
                print(f"  - {issue}", file=sys.stderr)
            failed += 1
        else:
            print(f"PASS {record_path}")
            passed += 1
    print(f"Validated {passed + failed} record(s): {passed} passed, {failed} failed.")
    return 1 if failed else 0


def _run_benchmark(args: argparse.Namespace) -> int:
    try:
        result = run_benchmark(
            args.task,
            schema_path=args.schema,
            event_schema_path=args.event_schema,
            ontology_path=args.ontology,
        )
    except (KeyError, OSError, TypeError, ValueError) as exc:
        print(f"Benchmark failed: {exc}", file=sys.stderr)
        return 1
    print(result_as_json(result))
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "validate":
        return _run_validate(args)
    if args.command == "benchmark":
        return _run_benchmark(args)
    raise AssertionError(f"Unhandled command: {args.command}")
