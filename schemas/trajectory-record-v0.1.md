# Trajectory Record Schema v0.1

## Status

This document is the human-readable companion to the executable schemas:

- `schemas/trajectory-record.schema.json`
- `schemas/life-event.schema.json`

The JSON Schemas are authoritative for automated validation. This document explains the design intent. Governance fields were refined in schema version `0.1.1` to distinguish the repository owner's absolute opt-out from the allowed bases for third-party data.

## Purpose

The schema defines the minimum information required for an HTM pilot record. The starter repository contains synthetic records only. Future non-synthetic records require a declared source and authorization basis, provenance, licensing, and review appropriate to the intended use.

## Core identity and governance

```yaml
schema_version: 0.1.1
record_id: stable internal identifier
entity_type: synthetic | public_figure | consented_volunteer | research_dataset_subject
synthetic: boolean
public_name: optional; null for starter synthetic records
data_governance:
  source_scope: synthetic | public_record | consented | licensed_dataset | approved_research_protocol
  authorization_basis: synthetic | public_record | consent | dataset_license | approved_protocol
  contains_repository_owner_data: false
  derived_from_owner_private_communications: false
  license: string
  review_status: synthetic_verified | unreviewed | reviewed | restricted
```

The two owner-protection fields are schema-level constants set to `false`. They implement the repository owner's absolute opt-out; they do not impose that same opt-out on all other people.

Third-party records instead declare why the data may be used:

- `public_figure` pairs with `public_record`;
- `consented_volunteer` pairs with `consent`;
- `research_dataset_subject` pairs with either `dataset_license` or `approved_protocol`;
- `synthetic` pairs with `synthetic`.

Schema validity does not by itself establish lawful use, ethical acceptability, or scientific quality. See `DATA_POLICY.md`.

## Birth information

```yaml
birth:
  local_date: YYYY-MM-DD
  local_time: HH:MM or null
  timezone: IANA timezone or documented historical offset
  location:
    city: string
    country: string
    latitude: number or null
    longitude: number or null
  time_precision: exact | minute | hour | approximate | unknown
  confidence_grade: AA | A | B | C | D | synthetic | unknown
  provenance:
    source_type: synthetic | certificate | official_record | direct_statement | biography | secondary | consented_statement | licensed_dataset | approved_protocol | unknown
    citation: string
    accessed_at: date or null
  ambiguities:
    daylight_saving: string or null
    calendar_system: string
    alternative_times: list
```

## Background covariates

Only information known before the prediction cutoff may be included.

```yaml
background:
  sex_or_gender: value or null
  birth_region: string or null
  socioeconomic_context: controlled category or null
  family_context: object or null
  historical_cohort: string
```

Sensitive attributes require a declared research need, data minimization, and governance review.

## Life events

```yaml
events:
  - event_id: stable identifier
    event_type: controlled ontology identifier
    start_date: date or null
    end_date: date or null
    date_precision: day | month | year | interval | unknown
    location: string or null
    attributes: object
    evidence_confidence: high | medium | low | synthetic
    provenance:
      citation: string
      source_type: synthetic | official | primary | reputable_secondary | consented_statement | other
      accessed_at: date or null
    label_eligibility: train | validation | test | excluded | synthetic
```

## Prediction cutoff

```yaml
prediction_context:
  cutoff_date: date
  information_snapshot_id: string
  permitted_event_ids: list
  hidden_future_event_ids: list
```

The validator rejects permitted events after the cutoff, hidden events on or before the cutoff, unknown IDs, and overlap between permitted and hidden events.

## Derived representations

Derived fields must be reproducible and versioned.

```yaml
derived:
  demographic_features_version: string
  birth_representation_version: string or null
  trajectory_encoding_version: string
  generated_at: datetime
```

## Quality controls

A record is excluded from a benchmark when:

- provenance is insufficient for the task;
- its authorization basis does not support the proposed use or redistribution;
- an event was used both to infer an input and score a hidden target;
- event dates cannot meet the task's minimum precision;
- biography leakage reveals the future label;
- sources materially conflict and the conflict is unresolved;
- required review or access controls are not met.

## Repository limits

Do not collect or publish raw passwords, authentication material, government identifiers, bank-account numbers, private correspondence, or personal contact details. Sensitive trajectory events may be represented when necessary and appropriately governed. The repository owner's personal trajectory and material derived from the owner's private communications remain prohibited. See `DATA_POLICY.md` for the binding rule.
