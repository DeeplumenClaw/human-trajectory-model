# Quickstart

## Install

```bash
git clone https://github.com/DeeplumenClaw/human-trajectory-model.git
cd human-trajectory-model
python -m pip install -e ".[dev]"
```

## Validate records

```bash
htm validate examples/synthetic/*.json
```

Validation checks:

- JSON Schema conformance;
- ontology event IDs;
- duplicate events;
- prediction-cutoff leakage;
- hidden/permitted event separation;
- synthetic provenance;
- repository-owner opt-out flags;
- third-party source and authorization-basis fields;
- prohibited raw identifiers, secrets, and private-correspondence field names.

## Run the synthetic smoke test

```bash
htm benchmark benchmark/tasks/next-event-synthetic-v0.1.yaml
```

The task learns a global event-type frequency distribution from four fictional training records and evaluates it on two fictional test records. Its purpose is to exercise the interface and metrics, not to produce a scientific conclusion.

## Run tests

```bash
pytest -q
```

## Add a contribution

Start with one of the issue forms. The smallest complete contributions are usually one ontology definition, one synthetic record, one schema test, or one terminology correction.
