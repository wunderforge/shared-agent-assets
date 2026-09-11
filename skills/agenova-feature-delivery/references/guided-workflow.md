# Guided workflow

Guided mode slows down only at decisions that teach or protect the design. It
does not narrate routine file reads or mechanical edits.

## 1. Readiness checkpoint

Summarize in a few lines:

- the user-visible outcome;
- the acceptance evidence;
- the current dependencies and blockers;
- what is explicitly out of scope.

If the ticket and task packet disagree, stop implementation and resolve the
authoritative requirement first.

## 2. Exploration checkpoint

Report findings as evidence, not as a codebase tour:

- which starting assumptions were confirmed;
- which assumption was wrong or incomplete;
- which existing contract, implementation, or test constrains the solution.

Do not discuss choices that have no effect on the result.

## 3. Design checkpoint

For each consequential question, present:

1. the decision to make;
2. one recommended option and, only when useful, credible alternatives;
3. the effect on public behavior, implementation, tests, and future adapters;
4. the exact task-packet section that will change after approval.

Wait for the user when the decision changes a public contract, MVP scope, or
security boundary. Otherwise record the choice and continue.

## 4. Implementation checkpoint

Before editing code, restate the resulting implementation slice in one short
paragraph. During implementation, surface a new question only if it invalidates
the approved design or acceptance evidence.

## 5. Review and gate checkpoint

Run the independent review lenses, address actionable findings, and then run
focused checks followed by the repository gate. Record:

- what a review changed;
- any issue intentionally deferred and why it is outside the ticket;
- each command or CI gate and the behavior it actually validates;
- any failure that prevented completion.

## 6. Learning closeout

Use the learning-log template to summarize the causal chain. Keep it concise
enough to review during a team meeting. Store it beside the task packet only
when the repository expects a durable artifact; otherwise include it in the
handoff or pull-request discussion.
