# HTM benchmarks

A benchmark contribution must define:

- what information is available at prediction time;
- the cutoff and prediction horizon;
- the target and label rule;
- train, validation, and test separation;
- at least one strong non-traditional baseline;
- metrics, calibration, and uncertainty reporting;
- leakage risks and exclusions;
- data governance and licensing.

`next-event-synthetic-v0.1.yaml` is an infrastructure smoke test. It uses fictional data and must not be cited as evidence that real human trajectories are predictable.

Run:

```bash
htm benchmark benchmark/tasks/next-event-synthetic-v0.1.yaml
```

Result cards should record the task ID, implementation version, data version, seed where relevant, metrics, failures, and limitations. The `benchmark/results/` directory is reserved for reproducible result cards, not marketing summaries.
