.PHONY: install venv build typecheck test lint deptry bandit audit pre-commit pre-push rulesync
install:
	uv sync 
venv:
	uv venv
build:
	uv build
typecheck:
	uv run mypy python_template
test: 
	uv run pytest tests 
lint:
	uv run ruff check python_template tests
deptry:
	uv run deptry python_template
bandit:
	uv run bandit -r python_template -c pyproject.toml
audit:
	uv run pip-audit
pre-commit:
	uv run pre-commit run --all-files
pre-push: lint typecheck test bandit audit deptry
rulesync:
	npx rulesync generate
