## What changed

Describe the narrow problem and the exact artifact changed.

## Contribution type

- [ ] Event ontology
- [ ] Synthetic example
- [ ] Schema or validator
- [ ] Benchmark task or baseline
- [ ] Theory/source representation
- [ ] Terminology or documentation
- [ ] Other

## Evidence and validation

List sources, commands, tests, or result cards used to review the change.

```bash
htm validate examples/synthetic/*.json
htm benchmark benchmark/tasks/next-event-synthetic-v0.1.yaml
pytest -q
```

## Data-governance declaration

- [ ] I have read `DATA_POLICY.md`.
- [ ] This pull request contains no trajectory record about the repository owner and is not derived from the owner's private communications.
- [ ] Any synthetic record is intentionally fictional and is not a lightly altered version of the owner or another real case.
- [ ] Every non-synthetic third-party record declares one allowed basis: public record, informed consent, dataset license, or approved research protocol.
- [ ] Provenance, usage rights, redistribution limits, and publication controls are documented where applicable.
- [ ] This pull request contains no unnecessary raw secrets, government identifiers, bank-account numbers, private correspondence, or personal contact details.

## Limitations and competing interpretations

State what this change does not establish, known edge cases, and any unresolved disagreement.
