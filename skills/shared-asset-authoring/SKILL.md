---
name: shared-asset-authoring
description: Add or revise a reusable skill, rule set, or sanitized memory asset in this repository while following its contribution and security contracts.
---

# Shared asset authoring

Use this skill when contributing an AI asset to this repository.

1. Read `CONTRIBUTING.md` and the README in the target asset directory.
2. Confirm the content is reusable and safe to publish. Exclude credentials,
   personal data, customer data, private chats, and internal-only history.
3. Start from the relevant file in `docs/templates/`.
4. Keep the change focused on one coherent asset.
5. Make commands, network access, filesystem writes, and dependencies explicit.
6. Run the repository check command documented in `README.md`.
7. Report the changed files, validation result, and one usage example.

Do not change validation or security policy as part of an unrelated asset change.

