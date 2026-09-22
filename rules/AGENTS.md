# Project Guidelines & Systematic Debugging Protocol

## Anti-Trial-and-Error & Zero-Hallucination Mandate

When working on this project, trial-and-error debugging, speculative guessing, hallucinated APIs, and quota-draining blind retries are strictly prohibited. These practices waste developer time, burn AI quota, and cause regression cascades.

---

### 1. Zero-Hallucination Rule
- Never invent, assume, or hallucinate methods, function signatures, component props, file paths, or CSS classes.
- Confirm every symbol's actual declaration in the codebase using file inspection tools before using it in a fix.

### 2. Mandatory Pre-Fix Diagnostic Card
Before modifying any file, formulate and present a clear diagnosis:
- `[SYMPTOM]`     : Verbatim error message, status code, or observable defect.
- `[LOCATION]`    : Exact file path, function, and verified line numbers.
- `[ROOT CAUSE]`  : The exact mechanical failure mechanism.
- `[SURGICAL FIX]`: Proposed change curing the root defect.
- `[BLAST RADIUS]`: All callers/consumers audited via symbol search.

### 3. Blast Radius & Regression Shield (Caller Audit)
- Before modifying any shared function signature, return type, or state structure, map **all callers**.
- Ensure edits do not break other components or introduce silent regressions.

### 4. The 2-Attempt Circuit Breaker
- Limit any solution hypothesis to a **maximum of 2 attempts**:
  - **Attempt 1:** Formulate hypothesis from direct inspection, apply surgical fix, verify.
  - **Attempt 2:** If Attempt 1 fails, analyze diagnostic feedback, refine the specific detail, verify.
  - **HALT:** If Attempt 2 fails, **STOP IMMEDIATELY**. Do not make a 3rd attempt on the same hypothesis. Trigger the Reverse Check.

### 5. Bidirectional Reverse-Check Protocol
If an approach fails twice or an issue is complex, execute a bidirectional trace:
- **Forward Trace:** User event -> listener -> handler -> state/engine -> failing output.
- **Reverse Check:** Failure symptom -> call stack backwards -> parameter origin -> data generator.
- Find the exact point where caller expectations and callee behavior diverged.

### 6. Strict 3-Tier Verification Gate (Never Test Live if Static Fails)
- **Gate 1 (Static):** Validate types and syntax (`tsc --noEmit` or parser check). If Gate 1 fails, halt.
- **Gate 2 (Contract):** Verify logic, null checks, and imports against actual declarations.
- **Gate 3 (Live Retrying):** *Only* trigger live device or browser verification once Gates 1 and 2 pass.

### 7. Platform Boundary & Hybrid App Awareness (Capacitor / Android / Web)
- Wrap `localStorage` in `try/catch` to handle Android WebView private mode restrictions.
- Stop camera media tracks (`stream.getTracks().forEach(t => t.stop())`) when closing scanner modals to avoid hardware leaks and battery drain.
- Provide graceful native fallbacks for browser-only APIs (`window.print`, `window.alert`).

### 8. Patch Minimalism (Anti-Sprawl)
- Keep fixes compact and surgical (typically under 20–30 lines).
- Never mask symptoms with empty `try/catch` blocks, arbitrary delay timers, or conditional bypasses.
