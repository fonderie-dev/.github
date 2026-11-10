<p align="center"><img src="https://raw.githubusercontent.com/fonderie-dev/.github/main/profile/icons/fonderie.svg" alt="Fonderie" width="112"></p>
<h1 align="center">Fonderie</h1>
<p align="center">AI model engineering for scientific work.<br>By R. Heller.</p>
<p align="center"><a href="https://fonderie-dev.github.io/website/">Website</a> · <a href="https://fonderie-dev.github.io/website/methode/">Méthode</a> · <a href="https://fonderie-dev.github.io/website/a-propos/">À propos</a></p>

Fonderie trains and fine-tunes open models on domain data, inspects and edits their weights, builds customised local models and evaluates them reproducibly on scientific tasks.

The workshop is at an early stage. The repositories below are scaffolds that state their intended scope; none of that scope is implemented yet. No model, dataset or benchmark result has been published.

## Projects

> **Status** &nbsp; ●●● released &nbsp;·&nbsp; ●●○ usable &nbsp;·&nbsp; ●○○ draft &nbsp;·&nbsp; ○○○ scaffold

| Project | Intended purpose | Status |
|---|---|:---:|
| [**Affinage**](https://github.com/fonderie-dev/fonderie-affinage) | Training and fine-tuning open models on domain data, and packaging the results as customised local models. | ○○○ |
| [**Burin**](https://github.com/fonderie-dev/fonderie-burin) | Inspecting and editing model weights: tensor statistics, checkpoint comparison and recorded edits. | ○○○ |
| [**Essai**](https://github.com/fonderie-dev/fonderie-essai) | Reproducible evaluation of models on scientific tasks, with pinned models, data and seeds. | ○○○ |
| [**.github**](https://github.com/fonderie-dev/.github) | Organisation profile, contribution and security guidance, shared Python CI workflow. | — |
| [**website**](https://github.com/fonderie-dev/website) | Source of the [Fonderie website](https://fonderie-dev.github.io/website/). | — |

The names come from the foundry. *Affinage* is the refining of molten metal, a *burin* is the engraver's chisel, and an *essai* is the assay that establishes what a casting actually contains.

## Principles

- **Open weights, local first.** Work starts from models whose weights and licence permit inspection, modification and local use. Training and evaluation run on hardware under our control.
- **Reproducible by record.** Every training or evaluation run records the base model and its exact revision, the data manifest, configuration, seed, software versions and hardware. A result without its record is not reported.
- **Weights are artefacts, not source.** Checkpoints, datasets and run outputs stay out of git. Released artefacts go to an archive with a persistent identifier and a model card.
- **Safe loading.** Weights are read from `safetensors`. Pickle-based checkpoints and `trust_remote_code` are not used without review.
- **Stated scope.** Each README says what is implemented and verified, and what is not.

## Data and model licensing

A fine-tuned model inherits obligations from its base model and from its training data. Open-weight licences differ in what they permit; check them before training and again before release. Models can memorise training examples, so weights trained on restricted or personal data carry that data's restrictions and are not published. See [SECURITY.md](https://github.com/fonderie-dev/.github/blob/main/SECURITY.md).

## Development

Repositories are Python packages (≥ 3.11) with a `src/` layout, tested with pytest and linted with ruff through the [shared workflow](https://github.com/fonderie-dev/.github/blob/main/.github/workflows/python-check.yaml). Tests use tiny synthetic models and run without a GPU or downloads. [CONTRIBUTING.md](https://github.com/fonderie-dev/.github/blob/main/CONTRIBUTING.md) covers naming and house style.

## Elsewhere

- Website: [fonderie-dev.github.io/website](https://fonderie-dev.github.io/website/) — source at [fonderie-dev/website](https://github.com/fonderie-dev/website)
- Overview of all projects: [r-heller.github.io/website/projects](https://r-heller.github.io/website/projects/)
- Related organisations: [CTTIR](https://github.com/CTTIR) (computational trauma and tissue injury research) · [Établi](https://github.com/etabli-dev) (tools for research and local knowledge work)

## Licensing

Code is released under Apache-2.0 unless a repository states otherwise. Model weights and datasets keep their own licences. © 2026 R. Heller.
