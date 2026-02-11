---
name: lint
description: "Run Ruff linter and formatter on the codebase"
---

# Lint & Format

Run Ruff to check and fix code quality issues.

1. First check for issues:
```bash
ruff check src/
```

2. Then check formatting:
```bash
ruff format --check src/
```

If the user asks to fix, run:
```bash
ruff check --fix src/ && ruff format src/
```

Summarize findings grouped by rule category (imports, style, etc.).
