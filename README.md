<div align="center">

# Human Trajectory Model (HTM)

**Open schemas, benchmarks, and baselines for studying how human lives unfold over time — including the boundary of what can be predicted.**

[![Validation](https://github.com/DeeplumenClaw/human-trajectory-model/actions/workflows/validate.yml/badge.svg)](https://github.com/DeeplumenClaw/human-trajectory-model/actions/workflows/validate.yml)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

</div>

HTM asks a falsifiable question:

> Given initial conditions and an observed life history up to time `t`, which future states can be estimated better than strong demographic and history-only baselines — and when should a model abstain?

```text
initial conditions + history up to t
                 │
                 ▼
        trajectory representation
                 │
       ┌─────────┼─────────┐
       ▼         ▼         ▼
   baselines   knowledge   sequence
                priors      models
       └─────────┼─────────┘
                 ▼
     future-state distribution
       + calibration + abstention
```

HTM is not a fortune-telling product and does not assume that any historical theory is correct. Traditional Chinese MingLi is the first structured knowledge tradition studied by the project because it contains a large and historically continuous body of hypotheses about life trajectories. Those hypotheses must be reconstructed faithfully, represented explicitly, and tested against non-traditional baselines.

## Current artifact: HTM Starter v0.1

This repository now provides a small, executable research core rather than only a project proposal:

- a machine-readable trajectory record schema;
- a controlled life-event vocabulary;
- six fully synthetic trajectory examples;
- a validation CLI with privacy and leakage checks;
- a reproducible synthetic next-event benchmark smoke test;
- contribution templates for event types, benchmark tasks, and research proposals;
- an explicit data policy that forbids private-conversation cases and unconsented private data.

The synthetic benchmark verifies the infrastructure. It is **not** evidence that human trajectories, MingLi representations, or any other theory have predictive validity.

## Quickstart

```bash
git clone https://github.com/DeeplumenClaw/human-trajectory-model.git
cd human-trajectory-model
python -m pip install -e ".[dev]"

htm validate examples/synthetic/*.json
htm benchmark benchmark/tasks/next-event-synthetic-v0.1.yaml
pytest -q
```

Expected validation output:

```text
PASS examples/synthetic/trajectory_001.json
...
Validated 6 record(s): 6 passed, 0 failed.
```

The benchmark command prints a JSON result card containing accuracy, log loss, multiclass Brier score, class probabilities, and the exact task identifier.

## What HTM is building

HTM separates a theory-neutral public core from several research tracks.

### Public core

- longitudinal record and event schemas;
- source provenance and evidence quality;
- benchmark task definitions;
- leakage-resistant evaluation protocols;
- demographic, history-only, and temporal baselines;
- probability calibration, uncertainty, and abstention;
- privacy and data-governance rules.

### Research tracks

- **Life-course modeling:** links to demography, sociology, economics, education, public health, and longitudinal machine learning.
- **Traditional priors:** explicit computational representations of historical trajectory theories, beginning with Chinese MingLi.
- **Uncertainty and limits:** what is predictable, what is not, and how a model should communicate insufficient evidence.
- **Representation transfer:** whether a shared trajectory representation transfers across tasks, cohorts, regions, and domains.

A traditional representation earns a place in HTM only through clear sourcing, frozen definitions, ablation, held-out evaluation, calibration, and replication. Historical authority determines what deserves serious study; it does not determine what must be accepted as correct.

## Repository map

```text
src/htm/                 Validation and benchmark CLI
schemas/                 Machine-readable and human-readable schemas
ontology/                Controlled life-event vocabulary
examples/synthetic/      Fictional records used only for tests and demos
benchmark/               Task specifications and result-card conventions
research/                Falsifiable experiment plans
model/                   Architecture notes
docs/                    Project overview and contributor documentation
.github/                 CI, issue forms, and pull-request template
```

See:

- [Project overview](docs/PROJECT_OVERVIEW.md)
- [Architecture v0.1](model/architecture-v0.1.md)
- [Evidence plan v0.1](research/evidence-plan-v0.1.md)
- [Roadmap](ROADMAP.md)
- [Contributing](CONTRIBUTING.md)
- [Data policy](DATA_POLICY.md)

## Data boundary

The following material must never be committed to this repository:

- cases or personal details obtained from private conversations, chats, messages, or consultations;
- information about the contributor's family, friends, clients, or other private individuals without explicit research consent and review;
- private addresses, contact details, medical records, financial-account data, or raw private correspondence;
- data whose license or provenance cannot be documented.

The starter dataset is entirely synthetic. Public-person and consented-volunteer datasets require separate review before they can become part of a benchmark. Read [DATA_POLICY.md](DATA_POLICY.md) before proposing any data contribution.

## Contributing

The easiest useful contributions are standardized artifacts, not broad declarations of support. Contributors can:

1. add or improve one life-event type;
2. add one synthetic trajectory that passes validation;
3. propose one benchmark task with a cutoff, target, split, baseline, and metric;
4. implement or reproduce one baseline;
5. formalize one well-sourced theory claim and define how it could fail;
6. improve one Chinese-English terminology record or source note.

Each contribution type has an issue form and acceptance criteria. See [CONTRIBUTING.md](CONTRIBUTING.md).

### Current contribution opportunities

- [Review the starter life-event ontology across disciplines](https://github.com/DeeplumenClaw/human-trajectory-model/issues/2)
- [Add machine-readable benchmark-task and prediction-output schemas](https://github.com/DeeplumenClaw/human-trajectory-model/issues/3)
- [Add a synthetic interval-duration trajectory example](https://github.com/DeeplumenClaw/human-trajectory-model/issues/4) — good first issue
- [Implement a history-only next-event baseline](https://github.com/DeeplumenClaw/human-trajectory-model/issues/5)
- [Create the public Chinese-English terminology record template](https://github.com/DeeplumenClaw/human-trajectory-model/issues/6) — good first issue
- [Design a source-grounded theory-claim record format](https://github.com/DeeplumenClaw/human-trajectory-model/issues/7)

Please comment on an issue before starting a substantial contribution so scope and ownership are visible.

## Research principles

1. **Reality before theory.** Observed outcomes take priority over elegant explanations.
2. **Prediction before explanation.** Claims should be frozen before hidden outcomes are inspected whenever possible.
3. **Evidence before authority.** Historical status and expert reputation justify attention, not automatic acceptance.
4. **Failure is data.** Null results, failed representations, and counterexamples must be preserved.
5. **Uncertainty is part of the output.** A model should communicate calibration, missing information, and reasons to abstain.
6. **Privacy is not optional.** Access to a private case or conversation is never permission to publish or train on it.

## Status and scope

HTM is an early-stage open research project. It does not yet provide a trained trajectory model, a validated MingLi predictor, or a human-trajectory foundation model. The term **foundation model** is reserved for a future system that demonstrates reusable transfer across multiple trajectory tasks, populations, and time periods with limited task-specific adaptation.

HTM outputs must not be used to make high-stakes decisions about employment, insurance, credit, education access, medical treatment, policing, or legal outcomes.

## License and citation

Code and repository documentation are licensed under [Apache License 2.0](LICENSE) unless a file states otherwise. Future datasets may require separate licenses and access rules. Citation metadata is provided in [CITATION.cff](CITATION.cff).
