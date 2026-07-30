# Human Trajectory Model (HTM)

**Can human trajectories be learned?**

HTM is a research project exploring whether human life trajectories contain learnable statistical structure, and whether initial conditions provide measurable predictive information about later life states.

The project does not assume that any traditional or modern theory is correct. Every representation, feature set, and modeling claim is treated as a testable hypothesis.

## Core research question

Given a person's initial conditions and observed life history up to time `t`, can a model estimate the probability distribution of future life states better than strong demographic and historical baselines?

## Initial scope

HTM v0.1 focuses on four components:

1. A reproducible representation of initial conditions.
2. A structured life-event trajectory schema.
3. Baseline models that do not use birth-derived representations.
4. Controlled experiments that measure whether additional representations provide predictive lift.

## Research discipline

HTM follows five rules:

- Reality before theory.
- Prediction before explanation.
- Evidence before authority.
- Failure is data.
- Uncertainty is part of the output.

## Current status

The repository is at the research-design stage. The immediate goal is not to claim a working foundation model, but to define the first falsifiable experiment, dataset schema, evaluation protocol, and baseline architecture.

## Repository structure

```text
research/       Research questions, hypotheses, and experiment plans
schemas/        Data and prediction schemas
model/          Architecture notes and modeling assumptions
benchmark/      Evaluation tasks, metrics, and baseline definitions
```

## Language

English is the primary project language. Chinese translations may be added under `docs/zh-CN/` after the English research documents stabilize.

## License

License selection will be finalized before the repository is made public.
