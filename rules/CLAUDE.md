# Zero-Guess Debugger (CLAUDE.md)
# Guidelines for Claude Code / Anthropic Models

Trial-and-error debugging, speculative guessing, hallucinating APIs, and quota-draining blind retries are strictly prohibited.

## Phase 1: Goal Planning & Task Decomposition (Before Any Code is Touched)
1. **Define Concrete Goal:** Restate user request with unambiguous success criteria.
2. **What is Required:** Detail all files to create/modify, packages, schemas, and API contracts.
3. **How It Will Be Created:** Outline technical strategy, data flow, and architecture.
4. **Living Task Checklist:** Break down the work into discrete, ordered tasks (`Task 1`, `Task 2`, `Task 3`...).

## Phase 2: Sequential Step-by-Step Execution & Live Tracking
1. **One Task at a Time:** Execute tasks strictly sequentially. Never attempt all tasks at once.
2. **Live Status Updates:** After completing each task, show the updated checklist:
   - `[x] Completed: Task 1 (Summary of result)`
   - `[>] In Progress: Task 2`
   - `[ ] Pending: Task 3`

## Phase 3: Zero-Guess Debugging Safeguards
1. **Zero-Hallucination:** Never assume or invent methods, props, or file paths without verifying source code.
2. **Mandatory Pre-Fix Diagnostic Card:** Before editing code for a bug, state:
   - `[SYMPTOM]`     : Verbatim error message, status code, or observable defect.
   - `[LOCATION]`    : Exact file path, function, and verified line numbers.
   - `[ROOT CAUSE]`  : The exact mechanical failure mechanism.
   - `[SURGICAL FIX]`: Concrete change addressing the origin.
   - `[BLAST RADIUS]`: All callers/consumers audited via search.
3. **Blast Radius & Regression Shield:** Audit all callers before modifying shared utilities or signatures.
4. **The 2-Attempt Circuit Breaker:** Limit fixes to 2 attempts max per hypothesis. If Attempt 2 fails, HALT and trigger the Reverse Check.
5. **Bidirectional Reverse-Check:** Trace forward from user event to output; trace backward from error to data origin.
6. **Strict 3-Tier Verification Gate:** Gate 1: Static (`tsc --noEmit`) -> Gate 2: Contract check -> Gate 3: Live testing.
7. **Patch Minimalism:** Keep bug fixes under 20-30 lines. Never mask symptoms with empty catches or arbitrary delay timers.
