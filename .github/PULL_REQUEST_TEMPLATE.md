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

## Data and privacy declaration

- [ ] I have read `DATA_POLICY.md`.
- [ ] This pull request contains no cases or personal details obtained from private conversations, chats, consultations, family, friends, clients, or other private individuals.
- [ ] Any synthetic record is intentionally fictional and is not a lightly altered real case.
- [ ] This pull request contains no unconsented private-person data.
- [ ] Provenance and licensing are documented for any non-synthetic source material.

## Limitations and competing interpretations

State what this change does not establish, known edge cases, and any unresolved disagreement.
