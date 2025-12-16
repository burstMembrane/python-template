.PHONY: install venv build typecheck test lint format format-check deptry bandit audit pre-commit pre-push rulesync clean
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
format:
	uv run ruff format python_template tests
format-check:
	uv run ruff format --check python_template tests
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
clean:
	rm -rf build dist *.egg-info .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage
