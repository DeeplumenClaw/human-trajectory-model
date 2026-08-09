# Contributing to Human Trajectory Model

HTM is an open research project. A useful contribution can be code, a schema change, a source correction, a benchmark design, a negative result, or a carefully bounded theory representation. It does not need to support any predetermined conclusion.

## Data boundary and third-party pathways

Before contributing, read [DATA_POLICY.md](DATA_POLICY.md).

The repository owner's personal trajectory is an absolute opt-out. Never submit a record about the owner or material derived from the owner's private communications. A third-party fact mentioned in an owner communication must be sourced independently before it can be considered.

Other people are not covered by that blanket owner opt-out. A third-party record may be proposed when it has one declared basis:

- public record;
- informed consent;
- a compatible dataset license;
- an approved research protocol.

The contribution must document provenance, allowed uses, redistribution limits, and the review appropriate to that basis. Do not commit unnecessary raw secrets, government identifiers, bank-account numbers, private correspondence, or personal contact details.

A synthetic example must be intentionally fictional, not a lightly altered real case.

## Development setup

```bash
git clone https://github.com/DeeplumenClaw/human-trajectory-model.git
cd human-trajectory-model
python -m pip install -e ".[dev]"
htm validate examples/synthetic/*.json
htm benchmark benchmark/tasks/next-event-synthetic-v0.1.yaml
pytest -q
```

Use a focused branch and keep each pull request narrow enough to review.

## Contribution contracts

The project grows through standardized artifacts. Choose the closest contract below.

### 1. Add or revise a life-event type

Edit `ontology/event-types.yaml`. A contribution must include:

- a stable namespaced ID;
- a domain;
- an inclusion definition;
- at least one positive example;
- at least one exclusion or boundary case;
- required attributes, if any;
- discussion of cultural, historical, data-governance, or leakage limitations.

Acceptance means the definition can be applied consistently by someone other than its author and all validation tests pass.

### 2. Add a synthetic trajectory

Add a JSON record under `examples/synthetic/`. It must:

- pass the executable schemas;
- be intentionally fictional;
- use only ontology event types;
- use `authorization_basis: synthetic`;
- set both owner-protection flags to `false`;
- use synthetic provenance for birth and events;
- contain a prediction cutoff with permitted and hidden event IDs;
- add or update a test when it exercises new behavior.

Run:

```bash
htm validate path/to/record.json
```

### 3. Propose a benchmark task

Open a benchmark-task issue before implementing a major task. Define:

- available inputs at prediction time;
- cutoff and prediction horizon;
- target and exact label rule;
- train, validation, and test strategy;
- baseline models;
- metrics and calibration reporting;
- leakage risks and exclusions;
- source, authorization, publication, and licensing rules;
- conditions under which the hypothesis would be rejected or downgraded.

A benchmark should reward calibrated, reproducible prediction rather than persuasive narrative.

### 4. Add or reproduce a baseline

A baseline contribution must include:

- implementation and configuration;
- exact run command;
- dependency and random-seed information;
- tests;
- a result card;
- failures and limitations;
- comparison with an appropriately simple baseline.

Do not scale model size before showing that the task and data pipeline contain a reproducible signal.

### 5. Formalize a theory claim

Theory contributions must separate:

1. the historical source;
2. later commentarial interpretation;
3. modern practitioner claim;
4. the contributor's formalization;
5. the proposed test;
6. known exceptions and counterexamples.

Include edition, section, page, or stable public identifier where possible. Do not copy unlicensed modern books or proprietary course materials into the repository.

A computational representation should specify its inputs, outputs, conditions, version, and failure criteria. Traditional authority justifies investigation, not acceptance.

### 6. Improve terminology or translation

A terminology contribution should document:

- the Chinese term and characters;
- pinyin where useful;
- candidate English renderings;
- distinctions lost in translation;
- historical or school-specific variation;
- reliable sources.

Avoid forcing different concepts into one convenient English label.

## Evidence labels

Use these distinctions in documents and proposals:

- `historical-source`: directly supported by an identifiable historical text;
- `commentarial-interpretation`: attributed to a later commentator or school;
- `practitioner-claim`: documented in modern practice literature or teaching;
- `project-hypothesis`: proposed but not validated;
- `experimental-result`: supported by a documented experiment;
- `negative-result`: tested without the expected improvement;
- `open-question`: unresolved or contested.

## Pull-request requirements

A pull request should explain:

- the problem;
- the exact change;
- evidence or sources;
- how to validate it;
- limitations and competing interpretations;
- data basis, licensing, and publication implications.

Before opening a pull request:

```bash
htm validate examples/synthetic/*.json
htm benchmark benchmark/tasks/next-event-synthetic-v0.1.yaml
pytest -q
```

The pull-request template contains mandatory owner-opt-out and third-party data-basis declarations.

## Review and task ownership

- Comment on an issue before beginning a substantial contribution.
- Maintainers may assign or mark an issue as claimed.
- If work becomes inactive, the issue may be reopened for another contributor.
- Reviews evaluate evidence, scope, compatibility, data basis, and reproducibility—not agreement with a preferred theory.
- A null or negative result is eligible for acceptance when the protocol is sound.

## Language and conduct

Issues may be opened in English or Chinese. Stable public documentation should eventually have an English version; Chinese text is often necessary for source accuracy.

Follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Critique claims and methods rather than contributors or communities.
