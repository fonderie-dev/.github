# Contributing to Fonderie

This file applies to every repository in the organisation that does not
provide its own.

## Naming

- Repositories are named `fonderie-<mot>`: a lowercase French noun from the
  foundry or metalworking trade that describes the repository's role
  (`affinage`, `burin`, `essai`). Drop accents in the repository name
  (`fonderie-coulee`) and keep them in titles and prose (*Coulée*).
- The Python distribution matches the repository name (`fonderie-essai`); the
  import package uses an underscore (`fonderie_essai`).
- Code identifiers, docstrings and documentation are in English. The French
  word names the tool, not the API.

Unused words for later repositories: *coulée* (casting), *creuset*
(crucible), *moule* (mould), *alliage* (alloy, for model merging), *lingot*
(ingot, for a packaged model), *trempe* (quench), *poinçon* (hallmark).

## Python house style

- Python ≥ 3.11, `src/` layout, `pyproject.toml` built with hatchling. The
  version lives in `__init__.py` and nowhere else.
- `ruff check` and `ruff format` clean; tests with pytest. Development tools
  come from the `dev` extra: `python -m pip install -e ".[dev]"`.
- Type hints on public functions.
- Heavy dependencies (PyTorch, Transformers and similar) are optional extras
  until a module needs them, so the package imports and its tests run without
  a GPU.
- Tests use tiny synthetic models, tensors and datasets. A test must not
  download weights or data.

## Runs and artefacts

- A run is described by a configuration file under version control.
- Its record is written next to its outputs: base model id and revision (a
  commit hash, not a branch), data manifest with checksums, configuration,
  seed, package versions, hardware, start and end time.
- Do not commit checkpoints, datasets, caches or run directories. Each
  repository's `.gitignore` excludes the common weight, checkpoint and
  run-output formats; extend it rather than force-adding files.
- Report a metric together with the record that produced it. A number that
  cannot be traced to a record is not reported.

## Shared workflow

Do not copy workflow YAML between repositories. Call the shared one:

```yaml
jobs:
  python:
    uses: fonderie-dev/.github/.github/workflows/python-check.yaml@main
```

Inputs: `python-versions` (JSON list, default `["3.11", "3.12", "3.13", "3.14"]`)
and `working-directory` (default `.`).

## Automation

Scripted changes across repositories may create files or replace whole files.
They may not edit structured fields in place. Identify an edit target by
ownership, not by pattern.
