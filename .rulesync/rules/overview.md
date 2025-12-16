---
root: true
targets: ["*"]
description: "Project overview and general development guidelines"
globs: ["**/*"]
---

## Project Overview

This is a python project that enforces strict typing and linting standards. 
Uses `uv` as the package manager with `hatchling` as the build backend.

## Commands

```bash
make install      # Install dependencies (uv sync)
make build        # Build the project
make typecheck    # Run mypy type checking
make test         # Run pytest
make lint         # Run ruff linter
make deptry       # Check for dependency issues
make pre-commit   # Run all pre-commit hooks
```

Run a single test file:

```bash
uv run pytest tests/test_utils.py
```

Run a single test function:

```bash
uv run pytest tests/test_utils.py::test_add
```

## Style and Type Guide for AI Agents

### Type Annotations Are Mandatory

All function definitions must include complete type annotations. The mypy configuration enforces `disallow_untyped_defs = true`.

```python
# Correct
def process(data: list[str], count: int) -> dict[str, int]:
    ...

# Wrong - will fail type checking
def process(data, count):
    ...
```

### Use Modern Python Typing

Target Python 3.12+. Use built-in generic types, not `typing` module equivalents:

```python
# Correct (Python 3.12+)
def get_items() -> list[str]:
    ...

def get_mapping() -> dict[str, int]:
    ...

# Avoid (legacy style)
from typing import List, Dict
def get_items() -> List[str]:
    ...
```

Use `Optional` from typing or the `X | None` union syntax:

```python
from typing import Optional

def find(name: Optional[str] = None) -> str:
    ...

# Or equivalently:
def find(name: str | None = None) -> str:
    ...
```

### Line Length

Maximum line length is 120 characters (configured in ruff).

### Pre-commit Hooks

The following checks run automatically:

- **On commit**: Type checking (mypy), Linting (ruff)
- **On push**: Build verification, Dependency check (deptry)

### Test Files

Test files are excluded from mypy checking (`exclude = "test_*"` in pyproject.toml), but should still follow typing conventions for consistency.

