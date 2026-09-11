# Shared Agent Assets

Security-reviewed, reusable assets for AI agents used by the team.

| Directory | Purpose |
| --- | --- |
| `skills/` | Executable agent skills in the open Agent Skills layout |
| `rules/` | Reusable instruction and policy text that a project can adopt |
| `memory/` | Sanitized, durable knowledge that is safe to share publicly |

This repository is public. Never add credentials, customer data, personal data,
private conversation exports, or internal-only project history.

## Install skills

List the available skills:

```sh
npx skills add wunderforge/shared-agent-assets --list
```

Install one skill for a supported agent:

```sh
npx skills add wunderforge/shared-agent-assets --skill <skill-name> --agent codex
```

The same repository can target Claude Code, Cursor, and other clients supported
by the [`skills` CLI](https://github.com/vercel-labs/skills).

## Contribute

1. Create a branch and add one coherent asset or change.
2. Run `./scripts/check.ps1` on Windows or `./scripts/check.sh` on macOS/Linux.
3. Open a pull request using the repository template.
4. Merge only after owner review and the required CI gate pass.

Every skill is scanned with
[NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector). The gate is
fail-closed: only a `SAFE` recommendation is accepted.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the asset contracts and review flow.

