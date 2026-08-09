# HTM Roadmap

This roadmap separates executable public infrastructure from long-term scientific claims. Dates are intentionally secondary to reviewable artifacts and evidence gates.

## v0.1 — Executable starter

Goal: make the project usable and contributable without requiring private data or acceptance of any theory.

- [x] Machine-readable trajectory record schema
- [x] Controlled life-event vocabulary
- [x] Fully synthetic examples
- [x] Record validator with privacy and temporal-leakage checks
- [x] Synthetic next-event benchmark smoke test
- [x] Continuous integration
- [x] Data policy and contribution templates

**Evidence gate:** v0.1 demonstrates infrastructure only. It makes no predictive claim.

## v0.2 — Stable representation contract

Goal: turn the starter into a reviewed specification that external researchers can extend.

- [ ] Review the first 20–30 event types with life-course researchers
- [ ] Add versioning and migration rules for schema changes
- [ ] Add benchmark-task and prediction-output JSON Schemas
- [ ] Add event-duration, interval, and competing-risk examples
- [ ] Add a public terminology registry with Chinese-English provenance
- [ ] Publish a contributor credit and decision process

**Evidence gate:** independent contributors can add an event type, synthetic record, or task without maintainer-authored custom code.

## v0.3 — Baselines and evaluation protocol

Goal: establish strong non-traditional baselines before testing historical priors.

- [ ] Logistic-regression and survival-analysis baselines
- [ ] History-only sequence baseline
- [ ] Temporal and cohort-aware splits
- [ ] Calibration, Brier score, log loss, and abstention metrics
- [ ] Leakage audit checklist and automated checks
- [ ] Reproducible result cards

**Evidence gate:** the same benchmark can be reproduced from a clean environment and produces stable results within declared tolerance.

## v0.4 — Public-data pilot protocol

Goal: define whether and how a small public-record pilot can be conducted responsibly.

- [ ] Data protection and ethics review
- [ ] Public-record inclusion and exclusion criteria
- [ ] Provenance, conflict, correction, and removal procedures
- [ ] Dataset license and access model
- [ ] Identity-separated blind evaluation design
- [ ] No private-conversation or privately supplied cases

**Evidence gate:** a documented reviewer confirms that the protocol meets the repository's data policy before any real-person records are added.

## Research track A — Traditional Chinese MingLi as a candidate prior

This track is important to HTM's origin, but it is evaluated as a research hypothesis rather than treated as privileged truth.

- [ ] Define a public-source citation standard
- [ ] Separate historical text, later commentary, practitioner claim, and project hypothesis
- [ ] Freeze a compact deterministic representation before outcome inspection
- [ ] Document birth-time uncertainty and correction leakage
- [ ] Compare against demographic and observed-history baselines
- [ ] Run ablation, permutation, calibration, and cohort-robustness tests
- [ ] Publish negative and null findings

Private repositories, private conversations, and privately discussed cases are outside this public track.

## Research track B — Limits of predictability

- [ ] Define abstention and insufficient-evidence outputs
- [ ] Measure calibration across horizons and subgroups
- [ ] Compare event prediction with trajectory-similarity tasks
- [ ] Study distribution shift across historical periods and regions
- [ ] Identify tasks where no tested representation beats a strong baseline

## Foundation-model threshold

HTM will not call an artifact a human-trajectory foundation model merely because it is large or pretrained. The term becomes appropriate only after a shared representation demonstrates transfer across multiple tasks, domains, cohorts, and populations with limited adaptation and reproducible gains over strong baselines.
