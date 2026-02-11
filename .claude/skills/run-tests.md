---
name: run-tests
description: "Run the pytest test suite and show results"
---

# Run Tests

Run the full test suite with pytest from the project root.

```bash
python -m pytest tests/ -v
```

If a specific test file or pattern is provided as an argument, run only that:
```bash
python -m pytest tests/ -v -k "<pattern>"
```

After running, summarize:
- Total passed/failed/skipped
- Any failure details with file and line number
- Suggestions to fix failures if obvious
