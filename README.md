# TechMart Data Pipeline

![Teaching](https://img.shields.io/badge/module-DE5M4-blue)
![Python Version](https://img.shields.io/badge/python-3.9--3.12-blue.svg)

![CI Pipeline](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/ci.yml/badge.svg)
![Lint](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/lint.yml/badge.svg)
![Last Commit](https://img.shields.io/github/last-commit/YOUR_USERNAME/YOUR_REPO)

<mark>*Replace `YOUR_USERNAME/YOUR_REPO` with your details*</mark>

## Project Overview

A small Python project for TechMart's order data. This scaffold exists to show
what a real, version-controlled Python project looks like: how it is laid out,
how it is tested, and how GitHub runs those checks automatically.

The functions in `src/techmart/` are deliberately minimal - the focus is the
shape of the project, not the pipeline logic.

## Setup

### Local Development

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: .\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the tests
pytest

# Run the tests with a coverage report
pytest --cov=src --cov-report=term-missing

# Check the code style
ruff check .
```

## Project Structure

```
src/techmart/    the package - importable Python code
tests/           the tests that check the package works
pyproject.toml   project metadata and tool configuration (ruff, pytest, coverage)
requirements.txt the packages this project needs
.github/         the automation that runs on GitHub
```

## Testing

Tests live in `tests/` and are run with `pytest`. See `tests/test_example.py`
for the pattern to copy.

## CI/CD

This project uses GitHub Actions for continuous integration:

- `.github/workflows/ci.yml` - runs the tests on every push and pull request
- `.github/workflows/lint.yml` - checks code style with ruff

When a check fails, the pull request is blocked from merging.
