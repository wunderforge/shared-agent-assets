# Review rubric

Use three independent lenses. Findings must identify an observable failure,
contract violation, or missing evidence; style preferences are not findings.

## Correctness and negative cases

- Does the change satisfy every acceptance criterion?
- Are rejection paths and boundary values tested, not only the happy path?
- Could defaults, state transitions, errors, or concurrency produce an invalid
  result?

## Product and architecture boundaries

- Does the implementation preserve the approved governance contract?
- Does backend- or vendor-specific behavior remain behind its adapter boundary?
- Has the change introduced a second source of truth or expanded MVP scope?
- Are security decisions deterministic where the contract requires them to be?

## Evidence and maintainability

- Does each claimed behavior have direct, repeatable evidence?
- Do tests use the shared fixtures or contracts expected by the task packet?
- Do repository gates cover the changed languages and generated artifacts?
- Are names and documentation consistent with the public contract?

Prioritize findings that could change behavior, break integration, weaken a
boundary, or make completion unverifiable. Re-run the affected checks after a
fix, then run the full repository gate.
