# Project Overview

## Origin

Human beings have always tried to understand why lives unfold differently. Some explanations emphasize biology, others family, institutions, education, social class, historical conditions, personality, chance, or individual choice. Across civilizations, long-running knowledge traditions also developed structured theories about life trajectories.

Traditional Chinese MingLi is one of the most extensive examples. Over centuries, authors and practitioners developed concepts for describing initial structure, relational roles, seasonal conditions, temporal cycles, transitions, and recurring patterns in education, work, family, health, status, and movement. The tradition is internally diverse: different periods and schools use different assumptions, methods, and standards of evidence.

Modern research approaches the same broad problem from other directions. Demography studies life courses and population transitions. Medicine models longitudinal health records. Economics studies education, work, income, and mobility. Psychology studies traits and development. Machine learning increasingly models long sequences of events and learns transferable representations.

HTM begins from the possibility that these lines of work can be connected. Historical theories may contain compressed observations, useful abstractions, cultural assumptions, mistaken generalizations, or all of these at once. Modern longitudinal datasets may contain rich evidence but lack the conceptual structure developed by earlier traditions. The project seeks to make both sides explicit enough to compare, test, and improve.

## The project goal

The long-term goal of HTM is to develop a computational framework for human trajectories: a way to represent initial conditions, social context, observed life history, temporal change, uncertainty, and possible future states within one extensible system.

This does not mean producing a single deterministic forecast of a person's life. A trajectory model should estimate possibilities and uncertainty. It should distinguish predictable structure from historical contingency, missing information, and individual agency. It should also be capable of saying that a question cannot be answered reliably from the available evidence.

A mature HTM system would support multiple research tasks, including event prediction, transition modeling, trajectory similarity, counterfactual analysis, representation transfer, theory comparison, and evaluation of historical knowledge claims.

## Why begin with traditional Chinese MingLi

HTM does not begin with MingLi because the project assumes the tradition is already validated. It begins there because the tradition provides a large, structured, and historically continuous body of hypotheses about human trajectories.

Starting from an existing theory base may be more efficient than asking a model to rediscover every useful abstraction from raw data. In machine learning terms, the tradition may offer candidate representations and inductive biases. The task is to reconstruct those candidates faithfully, formalize them precisely, and measure whether they help.

MingLi is therefore the first knowledge track, not the complete identity of HTM. Other forms of knowledge may later be incorporated when their concepts, evidence, and ethical implications can be handled responsibly.

## Main workstreams

### Knowledge reconstruction

This workstream studies primary texts, commentaries, modern practice traditions, and documented cases. It identifies concepts, rules, reasoning sequences, disagreements, exceptions, and historical changes. The objective is not to produce simplified quotations but to reconstruct how each theory works as a system.

### Knowledge representation

This workstream translates theory into computational objects. A prose statement may become a feature definition, relation, graph, constraint, temporal function, probabilistic prior, decision rule, or hypothesis. Alternative interpretations should remain distinguishable rather than being silently merged.

### Trajectory data

This workstream defines how lives are represented. Records may include education, career, health, relationships, family, migration, wealth, legal events, social environment, and historical context. Every event needs temporal information, evidence quality, uncertainty, and privacy handling.

### Benchmarking

This workstream defines tasks and evaluation protocols. HTM models must be compared with demographic baselines, history-only baselines, domain-specific statistical models, and modern sequence models. Evaluation should include accuracy where appropriate, probability calibration, time-window error, robustness, transfer, and information leakage checks.

### Model development

This workstream investigates symbolic, probabilistic, graph-based, sequence-based, and hybrid approaches. Early models may test small representations. A foundation model becomes relevant only after there is evidence that a shared representation transfers across tasks and populations.

### Open research infrastructure

This workstream builds documentation, schemas, source standards, issue templates, review processes, and contributor pathways so that people from different disciplines can collaborate.

## What success would look like

HTM does not require every traditional theory to be validated. Several forms of success are possible.

The project may identify a subset of historical concepts that provide measurable predictive or explanatory value. It may show that some claims work only in narrow historical or social contexts. It may find that many traditional features add little beyond standard baselines. It may also develop useful trajectory representations from the process even when specific inherited rules fail.

A successful project should produce clearer knowledge, better tests, reusable datasets and schemas, reproducible benchmarks, and an honest account of what can and cannot be inferred about human trajectories.

## What the community is being invited to build

HTM is not asking contributors merely to implement a predefined model. The research problem itself requires collective construction.

Traditional knowledge specialists can help reconstruct theories and detect inaccurate simplifications. Historians and Chinese studies scholars can establish context and source reliability. Social scientists can connect the project to established life-course theory and warn against confounding. Statisticians can improve evaluation and uncertainty. Machine-learning researchers can build representations and baselines. Data engineers can make records traceable and reproducible. Privacy and ethics contributors can shape appropriate boundaries. Skeptics can identify unfalsifiable claims and design stronger controls.

The project especially welcomes contributions that make a claim more precise, more testable, more limited, or easier to disprove.

## Development stages

### Stage 0: Foundation

Establish the project language, source standards, contribution process, trajectory schema, theory schema, and first benchmark definitions.

### Stage 1: Knowledge base

Reconstruct a selected core of traditional Chinese trajectory theory and publish reviewed, attributable representations of its concepts and disagreements.

### Stage 2: Computable theories

Translate a small number of well-defined theories into executable or machine-readable forms. Preserve alternative interpretations and version every change.

### Stage 3: Baselines and tests

Build simple demographic and historical baselines, define leakage-resistant datasets, and test whether theory-derived representations add measurable information.

### Stage 4: Transferable representations

Study whether a shared trajectory representation can improve multiple tasks across cohorts, regions, and domains.

### Stage 5: Foundation model research

Only after transfer is demonstrated should HTM investigate large-scale pretraining and a general Human Trajectory Foundation Model.

## Ethical boundaries

Human trajectory modeling can affect privacy, autonomy, discrimination, and self-perception. HTM should not be used to make high-stakes decisions about individuals without strong evidence, consent, appropriate governance, and human review. The project must avoid presenting probabilistic outputs as destiny or using sensitive personal data without authorization.

Public-person datasets still require careful sourcing. Volunteer datasets require informed consent, withdrawal mechanisms, privacy protection, and clear use restrictions. Models should be audited for demographic, cultural, and historical bias.

## Invitation

HTM begins with a difficult question rather than a predetermined answer. We invite contributors to help preserve historical knowledge accurately, translate it carefully, test it rigorously, criticize it openly, and extend the study of human trajectories beyond the limits of any one discipline or tradition.
