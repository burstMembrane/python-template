# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python project template that enforces strict typing and linting standards. Uses `uv` as the package manager with `hatchling` as the build backend. Note: Files contain Jinja2 template variables (e.g., `{{ project_name }}`) for project scaffolding.

## Commands

```bash
make install      # Install dependencies (uv sync)
make build        # Build the project
make typecheck    # Run mypy type checking
make test         # Run pytest
make lint         # Run ruff linter
make format       # Format code with ruff
make deptry       # Check for dependency issues
make bandit       # Run security checks
make audit        # Run pip-audit vulnerability scan
make pre-commit   # Run all pre-commit hooks
make clean        # Remove build artifacts and caches
```

Run a single test file:

```bash
uv run pytest tests/test_utils.py
```

Run a single test function:

```bash
uv run pytest tests/test_utils.py::test_add
```

## Style and Type Guide

### Type Annotations Are Mandatory

All function definitions must include complete type annotations. The mypy configuration enforces `disallow_untyped_defs = true` via `strict = true`.

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
def get_items() -> list[str]: ...
def get_mapping() -> dict[str, int]: ...

# Avoid (legacy style)
from typing import List, Dict
```

Use `X | None` union syntax or `Optional`:

```python
def find(name: str | None = None) -> str: ...
```

### Docstrings

Use NumPy-style docstrings for all public functions:

```python
def add(a: int, b: int) -> int:
    """
    Add two integers.

    Parameters
    ----------
    a : int
        First integer.
    b : int
        Second integer.

    Returns
    -------
    int
        Sum of a and b.
    """
    return a + b
```

### Line Length

Maximum line length is 120 characters.

### Pre-commit Hooks

- **On commit**: Type checking, tests, linting, format check, security (bandit)
- **On push**: Build, dependency check (deptry), vulnerability scan (pip-audit)

### Test Files

Test files are excluded from mypy checking and docstring requirements (`tests/**` ignores `D` rules).
