# mini-tasks

Small in-memory task tracker, no framework, no database. Built as a
reviewer-agent test bed: small enough to keep every finding easy to trace,

with enough real cross-module calls between `src/store.py`, `src/pricing.py`,
and `src/reports.py` to exercise CodeGraph's caller/impact ana.

```
src/
  models.py   -- Task, TaskStatus
  store.py    -- in-memory TaskStore
  pricing.py  -- discount / late-fee math
tests/
  test_store.py
  test_pricing.py
```
