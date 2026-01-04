.PHONY: install venv build typecheck test lint format format-check deptry bandit audit pre-commit pre-push rulesync clean bootstrap
install:
	uv sync 
venv:
	uv venv
build:
	uv build
typecheck:
	uv run mypy {{ project_name | snake_case }}
test: 
	uv run pytest tests 
lint:
	uv run ruff check {{ project_name | snake_case }} tests
format:
	uv run ruff format {{ project_name | snake_case }} tests
format-check:
	uv run ruff format --check {{ project_name | snake_case }} tests
deptry:
	uv run deptry {{ project_name | snake_case }}
bandit:
	uv run bandit -r {{ project_name | snake_case }} -c pyproject.toml
audit:
	uv run pip-audit
pre-commit:
	uv run pre-commit run --all-files
pre-push: lint typecheck test bandit audit deptry
rulesync:
	npx rulesync generate
clean:
	rm -rf build dist *.egg-info .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage
bootstrap:
	echo "{{ python_version }}" >> .python-version
	uv sync
	git init
	uv run pre-commit install
	uv run pytest tests
	uv run ruff check {{ project_name | snake_case }} tests
	uv run test-cli --name "{{ project_name | snake_case }}"
