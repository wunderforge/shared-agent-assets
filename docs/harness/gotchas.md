# Gotchas

- `npx skills add` discovers exact `SKILL.md` files; templates deliberately use a
  different filename so they are not published as skills.
- SkillSpector exit code `0` includes both `SAFE` and `CAUTION`; our wrapper reads
  the JSON recommendation and accepts only `SAFE`.
- A `SAFE` label is not enough if analysis is partial; the wrapper also requires
  successful execution and complete file/reference coverage.
- Static scanning cannot prove runtime safety. Consumers still use least privilege.
- Public memory means sanitized durable knowledge, not chat logs or secret storage.
