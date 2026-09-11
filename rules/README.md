# Rules

Store reusable instruction or policy sets in `rules/<rule-set>/`.

Keep the canonical rule vendor-neutral. If Codex, Claude Code, Cursor, or another
client needs a different file layout, place that rendering under
`rules/<rule-set>/adapters/<client>/` and document how it maps to the source.

Rules guide or constrain behavior. They are not a substitute for runtime access
control when a requirement must be enforced deterministically.

