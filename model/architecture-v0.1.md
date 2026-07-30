# HTM Architecture v0.1

## Status

This document defines a research architecture, not a claim that a foundation model already exists.

## Modeling objective

HTM models a human life as a sequence of partially observed states:

```text
initial conditions -> observed states -> transition probabilities -> future state distribution
```

The model should estimate multiple plausible futures rather than output a single deterministic narrative.

## Input layers

### 1. Initial-condition representation

Potential inputs include:

- date, time, and location of birth
- historical cohort
- geographic context
- family and socioeconomic context, when ethically collected

Birth-derived symbolic or numerical representations are experimental modalities. They must be evaluated through ablation rather than treated as privileged truth.

### 2. Observed-history representation

A timestamped sequence of events and states known up to prediction time `t`, including education, occupation, migration, relationships, and major public milestones.

### 3. Context representation

External conditions that affect opportunity and risk, such as wars, economic cycles, policy regimes, and technological change.

## Core representations

### Life-event tokens

Each event should encode:

- event type
- start and end time or uncertainty interval
- geographic context
- evidence confidence
- source provenance
- state before and after the event, where inferable

### Latent trajectory state

The model may learn a latent state vector summarizing the person's observed trajectory at time `t`. This representation must not be presented as a psychological diagnosis or a complete description of the person.

## Candidate model family

The first implementation should be simpler than a large foundation model:

1. logistic and survival-analysis baselines;
2. gradient-boosted models on aggregated features;
3. sequence models for timestamped events;
4. multimodal trajectory encoders only after sufficient data exists.

Scaling model size before demonstrating signal is explicitly out of scope.

## Outputs

Every prediction should include:

- target event or state
- prediction horizon
- probability or probability distribution
- confidence or uncertainty estimate
- baseline probability
- strongest supporting and opposing evidence
- model and feature version

## Foundation-model threshold

The term `foundation model` should be used operationally only after a shared pretrained representation transfers across multiple trajectory tasks, populations, and time periods with limited task-specific adaptation.

Until then, the project should describe its artifacts as datasets, representations, benchmarks, baselines, or trajectory models.

## Safety boundary

HTM must not be used to make high-stakes decisions about employment, insurance, credit, education access, medical treatment, policing, or legal outcomes. Research outputs are probabilistic and may encode historical bias.
