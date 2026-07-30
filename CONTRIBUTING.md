# Contributing to Human Trajectory Model

Thank you for considering a contribution to HTM. This project brings together several communities that do not usually work in the same repository: machine learning, statistics, life-course research, Chinese studies, traditional MingLi research, data engineering, documentation, and open science.

You do not need to be a programmer to contribute. Source verification, terminology review, theory reconstruction, benchmark criticism, annotation design, and negative results are all first-class contributions.

## Before you begin

Please keep three distinctions clear.

First, HTM studies traditional theories without assuming they are correct. A contribution may preserve a historical claim, translate it into a formal representation, test it, criticize it, or show that it fails.

Second, historical description and modern interpretation must be separated. When documenting a classical source, identify what the source actually says, what later commentators add, and what your own interpretation proposes.

Third, project claims should be reproducible. Important statements should point to a source, a dataset record, an experiment, or a clearly labeled hypothesis.

## Ways to contribute

### Source and textual research

You may contribute reliable editions, bibliographic records, textual comparisons, source notes, chapter summaries, or corrections to existing quotations. Please include edition details and page or section references whenever possible.

### Traditional theory documentation

You may document a concept, rule, reasoning pattern, practitioner method, disagreement, exception, or case tradition. Contributions should describe scope and uncertainty rather than present a school-specific interpretation as universal.

### Terminology and translation

Chinese concepts often have no exact English equivalent. Good terminology contributions should preserve distinctions, document alternative translations, and explain what information is lost or changed in translation.

### Data and schema design

You may propose improvements to life-event types, evidence confidence, temporal uncertainty, privacy controls, annotation rules, or longitudinal record formats. Please include examples and discuss possible information leakage.

### Modeling and evaluation

You may contribute baselines, theory encoders, graph representations, temporal models, calibration methods, benchmark tasks, robustness checks, or ablation experiments. New models should be compared with simple and strong baselines.

### Review, replication, and criticism

Replication failures, counterexamples, unclear definitions, unsupported claims, and evidence of no predictive improvement are valuable contributions. The project does not treat negative results as project failures.

### Documentation

Clear explanations, diagrams, tutorials, examples, issue templates, contributor guides, and Chinese translations are welcome.

## Contribution workflow

For small corrections and documentation improvements, you may open a pull request directly.

For major changes, open an issue first. Major changes include new theoretical frameworks, new benchmark tasks, changes to core schemas, model architecture proposals, dataset releases, or claims that affect the public positioning of HTM.

A good proposal issue should explain:

1. the problem being addressed;
2. the evidence or sources involved;
3. the proposed change;
4. how the change can be reviewed or tested;
5. known limitations or competing interpretations.

## Pull request expectations

A pull request should be narrow enough to review. It should explain what changed, why the change is needed, what evidence supports it, and what remains uncertain.

Source-based contributions should include references. Experimental contributions should include reproducible instructions and report failed as well as successful runs. Schema changes should include before-and-after examples. Terminology changes should note affected documents.

Do not include private personal data, unlicensed copyrighted material, or sensitive case records.

## Evidence labels

Contributors are encouraged to distinguish among the following types of content:

- `historical-source`: directly supported by an identifiable historical text;
- `commentarial-interpretation`: attributed to a later commentator or school;
- `practitioner-claim`: documented in modern practice literature or teaching;
- `project-hypothesis`: proposed by HTM contributors but not yet validated;
- `experimental-result`: supported by a documented experiment;
- `negative-result`: a tested claim or representation that did not perform as expected;
- `open-question`: unresolved or contested.

## Good first issues

Beginner-friendly tasks may include source verification, glossary improvements, documentation edits, small schema examples, public-event annotation, or reproduction of a simple baseline. Look for the `good first issue` label.

## Discussion culture

HTM welcomes skeptical and supportive contributors. Critique claims, methods, translations, and evidence rather than people or communities. Traditional knowledge practitioners and scientific researchers may use different vocabularies; contributors should make assumptions explicit and avoid dismissive language in either direction.

## Language

Issues may be opened in English or Chinese. Pull requests that affect stable public documentation should preferably include English text. Chinese source notes and terminology discussions are welcome and often necessary.

## Current priority areas

The project currently needs the most help with source inventories, theory reconstruction, terminology, knowledge representation, trajectory schemas, baseline definitions, and falsifiable benchmark design.

Thank you for helping build a project in which inherited knowledge can be preserved accurately, tested openly, corrected responsibly, and extended collaboratively.
