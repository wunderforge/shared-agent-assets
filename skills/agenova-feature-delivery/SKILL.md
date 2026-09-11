---
name: agenova-feature-delivery
description: Guide an Agenova ticket from an approved task packet through exploration, design, implementation, independent review, and evidence-backed verification while making AIDLC decisions visible.
---

# Agenova feature delivery

Use this skill to implement a bounded Agenova ticket without replacing the
project's existing source of truth.

## Choose a mode

- **Guided mode:** use for first-time contributors, process exercises, or when
  the user wants to inspect how decisions affect implementation. Read
  [the guided workflow](references/guided-workflow.md).
- **Delivery mode:** use for routine work with an approved task packet. Follow
  the same gates, but report only material decisions, risks, and evidence.

At review time, read [the review rubric](references/review-rubric.md). In guided
mode, use [the learning-log template](references/learning-log-template.md) to
make the process inspectable without creating a second requirements document.

## Source of truth

Use this order when instructions conflict:

1. The repository's routing and contribution instructions.
2. Current product and architecture contracts.
3. The linked GitHub ticket.
4. Its approved task packet and design specification.
5. Conversation guidance for the current run.

Do not silently broaden the ticket, reopen an approved product decision, or
turn the learning log into an authority. Record an approved implementation
decision in the task packet before relying on it in code.

## Delivery loop

1. **Establish readiness.** Identify the ticket, active task packet, acceptance
   criteria, dependencies, and required evidence. If the planning gate has not
   passed, complete only the missing planning work and request review.
2. **Explore selectively.** Inspect the smallest set of product contracts,
   adjacent code, tests, fixtures, and prior decisions needed to test the task
   packet's assumptions.
3. **Resolve consequential uncertainty.** Surface only questions whose answers
   change public behavior, architecture boundaries, security, data shape, or
   acceptance evidence. Recommend the smallest compatible option.
4. **Update the plan.** Put approved decisions and their implementation impact
   into the task packet or design specification before changing code.
5. **Implement narrowly.** Make the smallest coherent change that satisfies the
   acceptance criteria. Preserve unrelated work and established contracts.
6. **Review independently.** Apply the rubric's correctness, architecture, and
   evidence lenses. When delegation is available and the user has authorized
   it, these may be separate read-only review lanes; otherwise run them in
   sequence.
7. **Verify progressively.** Run focused checks while editing, then the
   repository's full required quality gate. Fix failures or report the exact
   blocker; never weaken a gate to make the change pass.
8. **Close the evidence loop.** Map every acceptance criterion to observable
   evidence and state what the gates proved. Do not claim that a passing gate
   proves behavior it does not exercise.

## Operating boundaries

- Read only the repository material relevant to the active ticket.
- Write only ticket-scoped planning, implementation, test, and evidence files.
- Run only the repository's documented local build and validation commands.
- Do not access credentials, private data, customer data, or secret-bearing
  files.
- Do not push branches, update GitHub, merge code, install dependencies, or use
  external network services unless the user has authorized that action.
- Stop for a human decision when alternatives materially change public
  contracts, MVP scope, security posture, or irreversible external state.

## Safe invocation example

> Use `agenova-feature-delivery` in guided mode for the linked ticket. Inspect
> the approved task packet, show me the design checkpoint before implementation,
> then implement and explain what each quality gate proves.

Expected outcome: a ticket-scoped change, updated authoritative planning when a
decision changed, passing evidence, and a concise learning trail.
