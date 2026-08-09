# HTM Schemas

The JSON Schemas in this directory are the executable source of truth for record validation.

- `trajectory-record.schema.json` defines a complete versioned trajectory record.
- `life-event.schema.json` defines one timestamped event.
- `trajectory-record-v0.1.md` is the human-readable companion document.

The current trajectory-record schema is `0.1.1`. The patch separates the repository owner's absolute opt-out from the declared authorization bases available for third-party data.

Schema changes must include:

1. the research or interoperability problem being solved;
2. before-and-after examples;
3. migration impact;
4. data-governance and leakage implications;
5. tests and a version decision.

Run:

```bash
htm validate examples/synthetic/*.json
```
