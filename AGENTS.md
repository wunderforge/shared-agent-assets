# Agent entry point

This repository stores public, reusable AI-agent assets.

Before changing anything:

1. Read `CONTRIBUTING.md`.
2. Read the README in the asset directory you will change.
3. Keep one pull request focused on one coherent asset or policy change.

Non-negotiable rules:

- Never add secrets, personal data, customer data, or raw conversation history.
- A skill lives at `skills/<name>/SKILL.md`; its frontmatter `name` must match the folder.
- Do not add compiled binaries, archives, vendored dependencies, or generated caches.
- Do not weaken or bypass validation. Security exceptions require an explicit owner decision.
- Run `./scripts/check.ps1` or `./scripts/check.sh` before requesting review.

Use `docs/harness/playbooks.md` for the contribution workflow and
`docs/harness/gotchas.md` for known failure modes.

