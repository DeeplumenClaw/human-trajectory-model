# HTM Evidence Plan v0.1

## Objective

The first HTM experiment asks one narrow question:

> Do birth-derived representations provide measurable predictive information about later human trajectories after controlling for demographic, historical, and socioeconomic baselines?

This experiment is designed to produce a useful result whether the answer is positive, negative, or inconclusive.

## Experimental groups

### Baseline A: demographic prior

Inputs may include:

- birth year
- sex, where available and ethically appropriate
- country or region
- broad socioeconomic context
- historical cohort

### Baseline B: observed-history model

Adds life events known before prediction time `t`, such as education, occupation, migration history, and relationship status.

### Experimental model C: birth-derived representation

Adds a deterministic representation derived from birth date, time, and location. The first version must remain compact, reproducible, and frozen before evaluation.

### Experimental model D: combined trajectory model

Combines demographic priors, observed history, and the birth-derived representation.

## Initial prediction tasks

The first benchmark should use outcomes that are public, timestampable, and less dependent on subjective interpretation:

1. Entry into higher education.
2. Cross-border migration.
3. Founding a company or becoming a documented founder.
4. Major career transition.
5. Marriage or publicly documented long-term partnership transition.

Each task requires a precise label definition and an explicit prediction window.

## Data split

The benchmark must prevent information leakage through:

- chronological train, validation, and test splits
- identity-hidden blind evaluation where practical
- freezing all features before test labels are inspected
- separating records used for birth-time correction from records used for evaluation
- preventing multiple near-duplicate biographies of the same individual from crossing splits

## Evaluation

Accuracy alone is insufficient. HTM v0.1 will report:

- AUROC and AUPRC for binary tasks
- Brier score for probability quality
- calibration error
- log loss
- lift over demographic and observed-history baselines
- confidence intervals from bootstrap resampling

## Success criteria

A birth-derived representation is considered provisionally useful only if it:

1. improves performance on a held-out test set;
2. remains useful after demographic controls;
3. survives ablation and permutation tests;
4. shows acceptable probability calibration;
5. can be reproduced from the published protocol.

One positive result is not enough to establish a general claim. Replication across cohorts and tasks is required.

## Failure criteria

The first hypothesis should be rejected or downgraded if gains disappear under temporal splitting, vanish after demographic controls, depend on uncertain birth times, or cannot be reproduced.

## Immediate execution sequence

1. Finalize the event and prediction schemas.
2. Assemble a pilot dataset of 100–300 high-confidence public records.
3. Implement demographic and observed-history baselines.
4. Freeze one compact birth-derived feature set.
5. Run blind evaluation.
6. Publish the complete result, including null and negative findings.
