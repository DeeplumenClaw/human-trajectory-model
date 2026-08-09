# Trajectory Record Schema v0.1

## Status

This document is the human-readable companion to the executable schemas:

- `schemas/trajectory-record.schema.json`
- `schemas/life-event.schema.json`

The JSON Schemas are authoritative for automated validation. This document explains the design intent.

## Purpose

The schema defines the minimum information required for an HTM pilot record. The v0.1 repository contains synthetic records only. It must not be reused for private individuals without a separately reviewed consent, privacy, licensing, and withdrawal protocol.

## Core identity and governance

```yaml
schema_version: 0.1.0
record_id: stable internal identifier
entity_type: synthetic | public_figure | consented_volunteer
synthetic: boolean
public_name: optional; null for starter synthetic records
data_governance:
  source_scope: synthetic | public_record | consented
  contains_private_conversation_data: false
  contains_unconsented_private_data: false
  license: string
  review_status: synthetic_verified | unreviewed | reviewed
```

Both private-data flags are schema-level constants set to `false`. A record sourced from a private conversation is prohibited rather than merely low-confidence.

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
    source_type: synthetic | certificate | official_record | direct_statement | biography | secondary | consented_statement | unknown
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

Sensitive attributes require a declared research need and governance review.

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

A record is excluded from a real-data benchmark when:

- provenance is insufficient for the task;
- an event was used both to infer an input and score a hidden target;
- event dates cannot meet the task's minimum precision;
- biography leakage reveals the future label;
- sources materially conflict and the conflict is unresolved;
- consent, licensing, or privacy requirements are not met.

## Data minimization

Do not collect private addresses, contact details, private medical records, financial-account information, raw correspondence, or information about non-public relatives. See `DATA_POLICY.md` for the binding repository rule.
