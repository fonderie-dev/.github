# Shared Fonderie repository infrastructure

This repository supplies the organisation profile, contribution and security
guidance, an issue template for reproducibility failures, the branding mark,
and a reusable Python workflow. It is not a Python package.

## Use in a Fonderie repository

Create `.github/workflows/check.yaml` in a repository that has a
`pyproject.toml` with a `dev` extra providing pytest and ruff:

```yaml
name: Checks
on:
  push:
    branches: [main]
  pull_request:
permissions:
  contents: read
jobs:
  python:
    uses: fonderie-dev/.github/.github/workflows/python-check.yaml@main
```

The workflow installs the package with its `dev` extra, runs `ruff check` and
`ruff format --check` once, and runs pytest on each Python version in
`python-versions`. Set `working-directory` when the package is not at the
repository root. For an immutable pin, replace `@main` with a reviewed commit.

## Validate changes

`self-check.yaml` lints the workflows with actionlint and runs the shared
workflow against the fixture package in `tests/fixture/`. To repeat the
fixture run locally:

```sh
cd tests/fixture
python -m pip install -e ".[dev]"
ruff check . && ruff format --check . && python -m pytest
```

## Branding

`profile/icons/fonderie.svg` is the mark: a crucible pouring into an ingot
mould whose cells read as a weight matrix. `assets/branding/` holds a copy of
the SVG, a 256 px PNG, and the 500 px organisation avatar rendered with
`rsvg-convert -b '#1c1916' -w 500 -h 500`.

## Licence

Apache-2.0; see [LICENSE](LICENSE). The Fonderie mark: © 2026 R. Heller.
