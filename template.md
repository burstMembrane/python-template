# Template Migration Guide

This document explains how to use and extend this kickstart template.

## Template Variables

The following variables are defined in `template.toml`:

| Variable | Default | Description |
|----------|---------|-------------|
| `project_name` | `my-project` | Project name in kebab-case (e.g., `my-awesome-app`) |
| `python_version` | `3.12` | Python version (3.7-3.13) |
| `project_description` | `A short description...` | Project description (min 10 chars) |

## Variable Usage in Templates

### Basic Substitution

Use double curly braces for variable substitution:

```jinja2
{{ project_name }}          -> my-project
{{ python_version }}        -> 3.12
{{ project_description }}   -> Your description here
```

### Filters

Kickstart uses [Tera](https://keats.github.io/tera/) templating (Jinja2-like). Common filters:

```jinja2
{{ project_name | snake_case }}      -> my_project
{{ project_name | upper_camel_case }} -> MyProject
{{ project_name | camel_case }}       -> myProject
{{ project_name | kebab_case }}       -> my-project
{{ project_name | shouty_snake_case }} -> MY_PROJECT
{{ project_name | title_case }}       -> My Project
```

### Directory/File Names

For directory and file names, use `$$` instead of `|` for filters (Windows compatibility):

```jinja2
{{ project_name $$ snake_case }}/     -> my_project/
{{ project_name $$ kebab_case }}.py   -> my-project.py
```

## Files Using Template Variables

### pyproject.toml

- `name` uses `{{ project_name }}`
- `requires-python` uses `{{ python_version }}`
- `python_version` (mypy) uses `{{ python_version }}`
- `packages` uses `{{ project_name | snake_case }}`
- `project.scripts` entry uses `{{ project_name | snake_case }}.cli:main`

### Makefile

- All tool paths use `{{ project_name | snake_case }}`

### README.md

- Title uses `{{ project_name }}`

### .github/workflows/ci.yml

- Python installation uses `{{ python_version }}`

### tests/test_utils.py

- Import uses `{{ project_name | snake_case }}`

### Source Directory

- Directory named `{{ project_name $$ snake_case }}/`

## Adding New Template Variables

1. Add to `template.toml`:

```toml
[[variables]]
name = "author_name"
default = "Your Name"
prompt = "What is your name?"
validation = "^.{2,}$"
help = "Your name for package metadata."
```

2. Use in files:

```jinja2
author = "{{ author_name }}"
```

## Conditional Content

Use Tera conditionals for optional content:

```jinja2
{% if include_docker -%}
# Docker support enabled
COPY requirements.txt .
{%- endif %}
```

Define the variable in `template.toml`:

```toml
[[variables]]
name = "include_docker"
default = false
prompt = "Include Docker support?"
```

## Ignored Files

These paths are not copied to generated projects (configured in `template.toml`):

- `docs/` - Template documentation
- `.venv/`, `venv/`, `.env/`, `env/` - Virtual environments
- `.git/` - Git history
- `uv.lock` - Lock file (regenerated per project)
- `kickstart/` - Kickstart source code

## Testing the Template

```bash
# Generate a test project
kickstart /path/to/python-template /tmp/test-project

# Or from GitHub
kickstart https://github.com/user/python-template /tmp/test-project
```

After generating, set up the project:

```bash
cd /tmp/test-project
make install
pre-commit install
```

**Note:** Pre-commit is not installed in the template repo itself because the templated files (containing `{{ variables }}`) aren't valid Python/TOML until processed by kickstart.

## Common Patterns

### Python Module Names

Always use `{{ project_name | snake_case }}` for Python imports and package names since Python modules cannot contain hyphens.

### CLI Entry Points

```jinja2
[project.scripts]
{{ project_name }} = "{{ project_name | snake_case }}.cli:main"
```

### GitHub Actions Matrix (Multiple Python Versions)

If you want to test against multiple Python versions, consider adding a `python_versions` variable or hardcode the matrix in CI.
