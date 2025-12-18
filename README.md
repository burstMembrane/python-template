# {{ project_name }}

Template for a minimal, tested Python package with a CLI.

## Quick start

- Install dependencies: `make install`
- Run tests: `make test`
- Lint/type check: `make lint` / `make typecheck`
- Try the CLI: `uv run test-cli`

## Tooling

- Formatting: `make format`
- Linting: `make lint`
- Type checks: `mypy`
- Security: `bandit`, `pip-audit`
- Hooks: `pre-commit run --all-files`
