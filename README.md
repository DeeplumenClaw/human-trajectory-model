# Human Trajectory Model (HTM)

**Can centuries of traditional life-course theory be translated into a computable, testable, and extensible model?**

HTM is a research project that begins with the accumulated theories of traditional Chinese MingLi and asks how those theories can be represented computationally, evaluated against real-world outcomes, corrected where they fail, and extended with modern machine learning.

HTM does not start from the assumption that human trajectory theory must be rediscovered from scratch. Traditional Chinese systems such as Bazi, Zi Wei Dou Shu, and related schools already contain structured hypotheses about initial conditions, temporal cycles, relational patterns, and life events. The project treats this inherited body of knowledge as a serious domain prior rather than as unquestioned truth.

The aim is therefore neither to reproduce traditional fortune-telling nor to discard traditional theory in favor of purely data-driven pattern discovery. The aim is to build a rigorous bridge between historical knowledge and modern computational research.

## Core research question

Can traditional Chinese life-course theories be converted into explicit computational representations that improve the modeling of human trajectories beyond strong demographic and historical baselines?

This question has four parts. First, the original theories must be reconstructed accurately from classical texts and experienced practitioners. Second, their concepts must be translated into formal features, relations, constraints, and temporal mechanisms. Third, their claims must be tested on documented life trajectories. Fourth, the resulting system must be allowed to revise, narrow, or reject rules when evidence does not support them.

## Research approach

HTM follows a knowledge-first path. Classical texts, commentaries, modern masters, and documented practice cases form the initial knowledge foundation. This material is not used as unquestioned doctrine; it is organized as a set of theories, rules, disagreements, exceptions, and reasoning patterns.

The second stage is computational translation. Concepts such as structural balance, relational roles, seasonal strength, temporal activation, and cycle interaction are converted into machine-readable representations. The third stage is validation, where those representations are tested against real cases, blind predictions, counterexamples, and non-traditional baselines.

Only after these stages are sufficiently developed does HTM move toward a transferable trajectory model or foundation model.

## What HTM is not

HTM is not an attempt to present traditional MingLi as scientifically proven. It is not a fortune-telling product, a deterministic theory of human life, or a purely black-box model trained to rediscover patterns that centuries of prior work have already attempted to describe.

HTM is a knowledge-engineering and model-building effort grounded in traditional Chinese theory, modern evidence standards, explicit uncertainty, and continuous correction.

## Initial scope

HTM v0.1 focuses on four foundations:

1. Reconstructing the traditional knowledge base from primary texts, commentaries, and major practice traditions.
2. Building a formal vocabulary and knowledge graph for concepts, rules, conflicts, and temporal reasoning.
3. Translating selected theories into computable representations and reasoning procedures.
4. Designing validation tasks that can measure where those representations work, where they fail, and whether they add predictive value.

## Research discipline

HTM follows five rules:

- Reality before theory.
- Prediction before explanation.
- Evidence before authority.
- Failure is data.
- Uncertainty is part of the output.

Traditional authority determines what deserves careful study, not what must be accepted as correct.

## Current status

The project is currently building its knowledge foundation. The immediate work is to organize the classical literature and major practice traditions, identify their core contributions and disagreements, and translate a first group of concepts into explicit computational structures.

The project is not yet claiming a working foundation model. That term will only be used once the system has a transferable representation that performs across multiple trajectory tasks and populations.

## Repository structure

```text
research/       Research questions, hypotheses, and experiment plans
knowledge/      Public descriptions of the traditional knowledge framework
schemas/        Data, theory, and prediction schemas
model/          Architecture notes and computational representations
benchmark/      Evaluation tasks, metrics, and baseline definitions
docs/           Project background and language-specific documentation
```

The detailed source notes, internal theory comparisons, experimental features, unpublished case material, and failure analyses are developed in a separate private research repository. Material is moved here only when it is sufficiently clear, responsibly sourced, and suitable for public review.

## Language

English is the primary project language. Chinese documentation will be maintained under `docs/zh-CN/` because the primary source tradition is Chinese and cannot be responsibly represented through English terminology alone.

## License

License selection will be finalized before the repository is made public.
