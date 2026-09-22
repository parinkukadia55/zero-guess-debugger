# Zero-Guess Debugger (CLAUDE.md)
# Guidelines for Claude Code / Anthropic Models

Trial-and-error debugging, speculative guessing, hallucinating APIs, and quota-draining blind retries are strictly prohibited.

## Core Rules:
1. **Zero-Hallucination:** Never assume or invent methods, function signatures, component props, or file paths. Confirm every symbol's actual declaration using file inspection tools before modifying code.
2. **Mandatory Pre-Fix Diagnostic Card:** Before editing any file, state:
   - `[SYMPTOM]`     : Verbatim error message, status code, or observable defect.
   - `[LOCATION]`    : Exact file path, function, and verified line numbers.
   - `[ROOT CAUSE]`  : The exact mechanical failure mechanism.
   - `[SURGICAL FIX]`: Proposed change curing the root defect.
   - `[BLAST RADIUS]`: All callers/consumers audited via search.
3. **Blast Radius & Regression Shield:** Before modifying any shared function signature, return type, or state structure, check all callers. Ensure edits do not break other components.
4. **The 2-Attempt Circuit Breaker:** Limit any solution hypothesis to a maximum of 2 attempts. If Attempt 2 fails, HALT IMMEDIATELY and trigger a Reverse Check.
5. **Bidirectional Reverse-Check:** Trace forward from user event to failing output, and trace backward from error stack to parameter origin. Identify the divergence.
6. **Strict 3-Tier Verification Gate:** Never test live if static checks fail. Gate 1: Static (`tsc --noEmit` or parser check) -> Gate 2: Contract check -> Gate 3: Live verification.
7. **Patch Minimalism:** Keep fixes compact and surgical (typically under 20-30 lines). Never mask symptoms with empty `try/catch` blocks or arbitrary delay timers.
