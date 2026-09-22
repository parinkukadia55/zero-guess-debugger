<!-- BEGIN ZERO-GUESS DEBUGGER RULES -->
# Systematic Debugging, Zero-Hallucination & Quality Protocol

Strictly eliminate trial-and-error, speculative guesswork, hallucinated APIs, and quota-draining blind retries. Whenever an error, bug, test failure, or unexpected behavior occurs during development, live testing, or runtime execution, you MUST adhere to the following protocol:

### 1. Zero Hallucination Mandate
- Never assume, invent, or hallucinate methods, function parameters, component props, file paths, or CSS classes.
- Ground every referenced symbol in actual source code using code inspection tools (`view_file`, `grep_search`). Confirm declarations before writing fixes.

### 2. Mandatory Pre-Fix Diagnostic Card
Before touching any code, formulate the exact diagnosis:
- `[SYMPTOM]`     : Verbatim error message or observable defect.
- `[LOCATION]`    : Exact file path, function, and verified line numbers.
- `[ROOT CAUSE]`  : The exact mechanical failure mechanism.
- `[SURGICAL FIX]`: Concrete change addressing the origin.
- `[BLAST RADIUS]`: All callers/consumers audited via `grep_search`.

### 3. Blast Radius & Regression Shield
- Never modify shared utilities, props, or function signatures without auditing all callers with `grep_search`.
- Ensure changes do not break downstream consumers or alter contracts unexpectedly.

### 4. The 2-Attempt Circuit Breaker
- Limit any solution hypothesis to a **maximum of 2 attempts**.
- If Attempt 1 fails, analyze the new diagnostic feedback and refine.
- If Attempt 2 fails, **HALT IMMEDIATELY**. Do not make a 3rd attempt on the same hypothesis. Trigger the Reverse Check.

### 5. Bidirectional Reverse-Check Protocol
- **Forward Trace:** Event/Trigger -> listener -> handler -> state/engine -> failing output.
- **Reverse Check:** Failure/error -> call stack backwards -> parameter origin -> data generator.
- Compare where caller expectations and callee contracts diverged.

### 6. Strict 3-Tier Verification Gate (Never Test Live if Static Fails)
- **Gate 1 (Static):** Validate syntax and types (`tsc --noEmit` or parser check). If Gate 1 fails, halt.
- **Gate 2 (Contract):** Verify logic, null checks, and imports against actual declarations.
- **Gate 3 (Live Retrying):** *Only* trigger live device (ARTEMIS) or browser verification once Gates 1 and 2 pass.

### 7. Platform Boundary & Hybrid App Awareness (Capacitor / Android / Web)
- Wrap `localStorage` in `try/catch` to handle Android WebView private mode restrictions.
- Ensure camera media tracks are explicitly stopped (`stream.getTracks().forEach(t => t.stop())`) when closing scanner modals.
- Provide graceful fallbacks for browser-only APIs (`window.print`, `window.alert`).

### 8. Patch Minimalism (Anti-Sprawl)
- Keep fixes compact and surgical (typically under 20–30 lines).
- Never mask symptoms with empty `try/catch` blocks, arbitrary delay timers, or conditional bypasses.
<!-- END ZERO-GUESS DEBUGGER RULES -->
