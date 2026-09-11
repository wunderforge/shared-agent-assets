# Contributing

## Asset contracts

### Skill

Place each skill in `skills/<skill-name>/`. It must contain a `SKILL.md` with
YAML frontmatter containing `name` and `description`. The folder and `name`
must use lowercase kebab-case and must match.

Optional `scripts/`, `references/`, and `assets/` stay inside the skill folder.
Declare every external command, network destination, and write operation in the
skill instructions. Pin dependencies used by scripts.

### Rule

Place reusable rule sets under `rules/<rule-set>/`. Keep the source rule
vendor-neutral. Vendor-specific renderings belong in an `adapters/` child
directory and must not silently change the source rule's meaning.

### Memory

Place durable, reusable knowledge under `memory/<topic>/`. Include provenance
and a `Last verified` date. Memory must be factual, reviewable, and safe to make
public; do not store chat logs or working-session state.

## Pull request flow

- One coherent asset or security-policy change per pull request.
- Explain the intended consumer and why the asset is reusable.
- For a skill, include a safe invocation example and expected outcome.
- Run the local deterministic checks.
- Wait for the required owner review and CI result.

CI checks Git history for secrets, validates repository structure and Markdown
links, then statically scans every skill with NVIDIA SkillSpector. `CAUTION`,
`DO_NOT_INSTALL`, scan errors, and missing reports all block merging. The CI
scan uses `--no-llm`; it does not send repository contents to an external model
provider. Dependency coordinates may be sent to OSV.dev by SkillSpector for
vulnerability lookup.

Security findings must be fixed. A suppression or threshold change is a
security-policy change and requires a separately explained owner review.
