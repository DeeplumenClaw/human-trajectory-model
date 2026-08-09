# HTM Schemas

The JSON Schemas in this directory are the executable source of truth for v0.1 record validation.

- `trajectory-record.schema.json` defines a complete versioned trajectory record.
- `life-event.schema.json` defines one timestamped event.
- `trajectory-record-v0.1.md` remains the human-readable design note that preceded the executable schema.

Schema changes must include:

1. the research or interoperability problem being solved;
2. before-and-after examples;
3. migration impact;
4. privacy and leakage implications;
5. tests and a version decision.

Run:

```bash
htm validate examples/synthetic/*.json
```
