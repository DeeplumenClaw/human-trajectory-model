# Human Trajectory Model (HTM)

**An open research project for understanding, representing, and modeling how human lives unfold over time.**

Human Trajectory Model (HTM) asks a broad question: can human life trajectories be represented in a form that is computationally useful, empirically testable, and transferable across different life domains?

The project does not begin from a blank slate. Human societies have spent centuries developing theories about how lives evolve under the influence of birth conditions, family structure, social environment, personal choices, historical context, and time. Traditional Chinese MingLi is one of the richest and most systematic bodies of such knowledge, so it is the first major knowledge tradition HTM will study. It is a starting point, not the boundary of the project.

HTM aims to bring together researchers and contributors from machine learning, statistics, history, Chinese studies, sociology, psychology, demography, data engineering, and traditional knowledge communities. The goal is not to defend a belief system. The goal is to convert inherited theories and modern longitudinal evidence into explicit representations that can be examined, challenged, improved, and reused.

## Why this project exists

Modern machine learning has learned useful representations of language, images, proteins, weather, markets, and human movement. Human life-course modeling also exists in medicine, demography, education, labor economics, and social science, but these efforts are usually fragmented by domain. They may predict health risks, employment transitions, educational outcomes, or mortality, yet they rarely share one common representation of a life trajectory.

At the same time, historical traditions have attempted to describe long-term human trajectories using structured concepts, temporal cycles, relational patterns, and accumulated case experience. These systems contain hypotheses that may be valuable, partially valuable, context-dependent, outdated, or wrong. Today, for the first time, we have the computational tools and evidence standards needed to represent these claims precisely and test them systematically.

HTM exists to build that bridge.

## The central research question

Given a person's initial conditions, social context, and observed life history up to time `t`, can a model estimate the probability distribution of future life states better than strong demographic, historical, and domain-specific baselines?

This question includes several connected problems:

- How should a human life be represented as a longitudinal sequence rather than a static label?
- Which parts of initial conditions contain measurable information about later outcomes?
- Can traditional trajectory theories be translated into computable representations without distorting their original meaning?
- Do knowledge-guided representations improve performance over purely data-driven baselines?
- Can one shared representation transfer across education, career, health, relationships, migration, and other domains?
- How should uncertainty, missing information, historical change, and individual agency be modeled?

## Where traditional Chinese theory fits

HTM is broader than Bazi, Zi Wei Dou Shu, or any single school of traditional thought. However, traditional Chinese MingLi provides an unusually detailed starting knowledge base. It contains concepts about initial structure, relational roles, seasonal conditions, temporal cycles, transitions, and event activation. These concepts can be treated as a form of accumulated domain knowledge and possible inductive bias.

HTM will study this tradition in three stages. First, the original theories must be reconstructed carefully from primary texts, major commentaries, and documented practice traditions. Second, the concepts must be translated into explicit features, graphs, rules, constraints, and temporal mechanisms. Third, those representations must be tested against real trajectories, blind predictions, counterexamples, and non-traditional baselines.

Traditional authority determines what deserves serious study. It does not determine what must be accepted as correct.

## What HTM is building

The long-term project has five connected components.

### 1. A trajectory knowledge base

A structured account of historical and modern theories of human trajectory, including their concepts, assumptions, disagreements, exceptions, and reasoning patterns. Traditional Chinese theory is the first major source, but the framework is designed to incorporate compatible knowledge from social science, psychology, demography, medicine, economics, and other traditions.

### 2. A shared life-event representation

A common schema for describing life events and states across domains such as education, work, wealth, family, health, relationships, migration, legal events, and social context. The schema must support incomplete dates, uncertain evidence, overlapping events, and changing environments.

### 3. Computational representations of theory

Formal encodings of concepts that currently exist only in prose or practitioner reasoning. These may take the form of features, graphs, symbolic rules, constraints, temporal functions, probabilistic priors, or learned embeddings.

### 4. Open benchmarks and baselines

Evaluation tasks that compare simple demographic models, history-only models, domain-specific models, knowledge-guided models, and eventually transferable trajectory models. The benchmark must reward calibration and falsifiability, not persuasive storytelling.

### 5. A transferable trajectory model

The long-term objective is a model that learns reusable representations across multiple life-course tasks and populations. HTM will use the term "foundation model" only when there is evidence of genuine transfer across domains, tasks, and cohorts.

## What HTM is not

HTM is not a fortune-telling product, a deterministic account of human destiny, or an attempt to present traditional knowledge as already scientifically proven. It is also not a purely black-box effort that ignores centuries of accumulated theory and begins pattern discovery from zero.

HTM does not claim that a person's future can be completely predicted. Human trajectories are shaped by institutions, family, chance, decisions, historical events, and many variables that may never be observed. A useful model must be able to express uncertainty and sometimes conclude that available information is insufficient.

## Research principles

The project follows five core principles:

1. **Reality before theory.** Real outcomes take priority over elegant explanations.
2. **Prediction before explanation.** Testable claims should be recorded before outcomes are revealed whenever possible.
3. **Evidence before authority.** Historical status and expert reputation justify attention, not automatic acceptance.
4. **Failure is data.** Incorrect predictions and failed representations must be preserved and analyzed.
5. **Uncertainty is part of the output.** A model should communicate confidence, missing information, and competing explanations.

Additional project rules include strict source tracking, separation of training and evaluation data, explicit handling of birth-time uncertainty, versioned theory changes, and comparison against strong non-traditional baselines.

## Current phase

HTM is currently in the knowledge-foundation and research-design phase. The project is not yet presenting a trained foundation model.

The immediate priorities are:

- reconstruct the first group of traditional theories from reliable sources;
- document disagreements between major schools and practitioners;
- define a neutral vocabulary for trajectory concepts;
- complete the first life-event and evidence schemas;
- select a small set of theories for computational translation;
- design the first falsifiable benchmark tasks;
- establish baseline models that do not use traditional representations.

## How you can contribute

HTM is intended to be a genuinely collaborative research project. Contributions are welcome even if you do not write code.

You can help with:

- **Classical source research:** locating reliable editions, checking quotations, comparing textual variants, and explaining historical context.
- **Traditional theory review:** documenting concepts, practitioner methods, disagreements, exceptions, and real case reasoning.
- **Terminology:** developing accurate Chinese-English terminology without flattening distinct concepts into misleading translations.
- **Knowledge representation:** designing ontologies, knowledge graphs, rule formats, and temporal representations.
- **Dataset design:** defining life-event schemas, evidence quality, uncertainty fields, privacy rules, and annotation guidelines.
- **Machine learning:** building baselines, representation models, sequence models, graph models, calibration methods, and ablation studies.
- **Statistics and evaluation:** designing falsifiable tasks, leakage-resistant splits, causal controls, significance tests, and robustness checks.
- **Social science and life-course research:** connecting HTM to established work in demography, sociology, psychology, economics, education, and public health.
- **Reproduction and criticism:** challenging assumptions, identifying weak claims, reproducing experiments, and contributing negative results.
- **Documentation and translation:** improving explanations, examples, tutorials, diagrams, and Chinese-language documentation.

Before proposing a major new feature or theoretical framework, please open an issue so the scope and evidence requirements can be discussed. Small corrections, source improvements, documentation fixes, and clearly scoped contributions can be submitted directly as pull requests.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution process and [docs/PROJECT_OVERVIEW.md](docs/PROJECT_OVERVIEW.md) for the detailed project origin, research scope, and planned workstreams.

## Good first contributions

The project will maintain beginner-friendly issues in several categories:

- verify one source or quotation;
- summarize one classical chapter using the project schema;
- document one disagreement between schools;
- improve one Chinese-English term definition;
- add one well-sourced public life event;
- review one benchmark label definition;
- reproduce one baseline result;
- improve one section of the documentation.

Issues suitable for new contributors will be labeled `good first issue`. Tasks needing domain expertise will be labeled by area, such as `classical-texts`, `mingli`, `statistics`, `machine-learning`, `life-course-research`, or `documentation`.

## Repository structure

```text
research/       Research questions, hypotheses, and experiment plans
knowledge/      Public knowledge-framework documents and theory summaries
schemas/        Data, evidence, theory, and prediction schemas
model/          Architecture notes and computational representations
benchmark/      Evaluation tasks, metrics, splits, and baseline definitions
docs/           Project overview, terminology, contribution guides, and translations
```

Detailed source notes, unpublished case material, experimental features, and internal failure analyses are developed separately until they are sufficiently clear, responsibly sourced, and suitable for public review.

## Language

English is the primary project language so that the global research community can participate. Chinese documentation will be maintained under `docs/zh-CN/` because much of the first source tradition is Chinese and cannot be responsibly represented through English terminology alone.

Contributors may open issues in either English or Chinese. Important project decisions and stable documentation should eventually be available in English, with Chinese versions maintained for source accuracy and accessibility.

## Project status and openness

This repository is currently being prepared for public release. Research claims should be treated as provisional unless they are linked to a documented source, experiment, or benchmark result.

The project welcomes disagreement. A strong contribution may confirm a theory, narrow its scope, expose a translation error, demonstrate that a feature adds no predictive value, or show that a simpler baseline performs better.

## License

The project intends to adopt a permissive open-source license before public release. Dataset components may require separate licenses or access rules because of privacy, source rights, and consent requirements.

## Acknowledgment

HTM is built on the work of many generations of authors, commentators, practitioners, archivists, researchers, and open-source contributors. The project aims to preserve attribution, distinguish historical claims from modern interpretations, and make every important research step open to review.
