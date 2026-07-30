# Trajectory Record Schema v0.1

## Purpose

This schema defines the minimum information required for an HTM pilot record. It is designed for public-figure research first and must not be reused for private individuals without consent, privacy review, and data-minimization controls.

## Record identity

```yaml
record_id: stable internal identifier
public_name: optional display name
entity_type: public_figure | volunteer | synthetic
```

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
  confidence_grade: AA | A | B | C | D | unknown
  provenance:
    source_type: certificate | official_record | direct_statement | biography | secondary | unknown
    citation: string
    accessed_at: date
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
  family_context: structured fields or null
  historical_cohort: string
```

## Life events

```yaml
events:
  - event_id: stable identifier
    event_type: controlled vocabulary
    start_date: date or null
    end_date: date or null
    date_precision: day | month | year | interval | unknown
    location: string or null
    attributes: object
    evidence_confidence: high | medium | low
    provenance:
      citation: string
      source_type: official | primary | reputable_secondary | other
    label_eligibility: train | validation | test | excluded
```

## Prediction cutoff

```yaml
prediction_context:
  cutoff_date: date
  information_snapshot_id: string
  permitted_event_ids: list
  hidden_future_event_ids: list
```

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

A record is excluded from the primary benchmark when:

- birth time provenance is missing for a time-sensitive experiment;
- the same event was used both to infer or correct the birth time and to score the prediction;
- event dates cannot meet the task's minimum precision;
- biography leakage makes the future label directly visible in model input;
- sources materially conflict and the conflict is unresolved.

## Data minimization

Do not collect sensitive attributes unless they are necessary for a declared research question. Do not publish private addresses, contact details, medical records, financial account information, or information about non-public relatives.
