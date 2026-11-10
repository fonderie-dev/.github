# Security and data protection

## Reporting

Open a private security advisory on the affected repository (Security tab,
*Report a vulnerability*), or write to fonderie.dev@outlook.com. Do not open
a public issue for anything involving credentials, personal data, or weights
trained on restricted data.

## Data

- Never commit identifiable or personal data, including in filenames,
  prompts, test fixtures or notebook outputs.
- Training data, evaluation sets and raw outputs belong in an
  access-controlled store, not in git. Git keeps everything you ever
  committed.
- Models can memorise and reproduce training examples. Weights, adapters,
  logits and generated samples from a model trained on restricted data are
  restricted data themselves. They are not published or shared beyond the
  data's approval.
- Evaluation items used for reported results must not appear in the training
  data. Record the check that established this.

## Model files and remote code

- Load weights from `safetensors`. Pickle-based formats (`.bin`, `.pt`,
  `.pth`, `.ckpt`, `.pkl`) can execute code when loaded; open them only from a
  trusted source, and with `torch.load(..., weights_only=True)` where
  possible.
- Keep `trust_remote_code=False`. Enabling it runs code from the model
  repository; review that code and pin its revision first.
- Pin model and dataset downloads to a commit hash.
- Access tokens come from the environment or a credential store, never from
  code, configuration files or notebooks.

## Serving

A local model server bound to a public interface without authentication
exposes the model and the machine. Bind to localhost, or put authentication
in front of it.
