---
name: zero-guess-debugger
description: >-
  Stop AI coding agents from burning your quota with blind trial-and-error. Enforces zero-hallucination,
  mandatory pre-fix diagnostic cards, a 2-attempt circuit breaker, bidirectional reverse-checking,
  and strict 3-tier verification gates across all bug fixes and live testing.
license: MIT
metadata:
  author: Parin Kukadia
  homepage: https://github.com/parinkukadia55/-zero-guess-debugger
  version: "1.0.0"
---

# 🛡️ Zero-Guess Debugger (Anti-Trial-and-Error Protocol)

> **Stop AI coding assistants and autonomous agents from burning your quota with blind trial-and-error.**

---

## 🚫 The Problem: The AI Quota-Burning Loop

When AI agents encounter a bug or test failure, their default behavior is often:
1. Guessing what might be broken without reading the code.
2. Making speculative edits across random files hoping something works.
3. Hallucinating methods, parameters, and props that don't exist.
4. Repeatedly retrying failing commands and burning hundreds of thousands of tokens.
5. Introducing silent regressions while attempting to fix the original symptom.

**Zero-Guess Debugger** forces the AI agent into an ironclad, evidence-first engineering discipline.

---

## 📐 The 5-Step Zero-Guess Cognitive Loop

```
                      ┌────────────────────────────────────────┐
                      │ 1. Zero-Hallucination & Identification │
                      │ (Symptom, file location, exact lines)  │
                      └──────────────────┬─────────────────────┘
                                         │
                                         ▼
                      ┌────────────────────────────────────────┐
                      │ 2. Pre-Fix Diagnostic Card             │
                      │ (Proof, root cause & caller audit)     │
                      └──────────────────┬─────────────────────┘
                                         │
                                         ▼
                      ┌────────────────────────────────────────┐
                      │ 3. Surgical Fix (Max 2 Attempts)       │
                      │ (Compact, under 30 lines, root-focused)│
                      └──────────────────┬─────────────────────┘
                                         │
                                         ▼
                      ┌────────────────────────────────────────┐
                      │ 4. If 2 Attempts Fail -> REVERSE CHECK │
                      │ (Bidirectional trace failure -> origin)│
                      └──────────────────┬─────────────────────┘
                                         │
                                         ▼
                      ┌────────────────────────────────────────┐
                      │ 5. Strict 3-Tier Verification Gate     │
                      │ Gate 1: Static (tsc --noEmit)          │
                      │ Gate 2: Contract & Logic Checks        │
                      │ Gate 3: Verified Live Testing          │
                      └────────────────────────────────────────┘
```

---

## 🔒 The 8 Core Protocols

### 1. Zero-Hallucination Mandate
- **Never guess API signatures:** Ground every referenced method, function argument, component prop, and file path in actual source code using `view_file` or `grep_search`.
- **Third-Party Reality Check:** Never assume external libraries export a function without checking `package.json` or `.d.ts` definitions.

### 2. Mandatory Pre-Fix Diagnostic Card
Before touching any source file, the agent MUST present a 5-point proof card:
- `[SYMPTOM]`     : Verbatim error message, status code, or observable defect.
- `[LOCATION]`    : Exact file path, function name, and verified line numbers.
- `[ROOT CAUSE]`  : The exact mechanical failure mechanism.
- `[SURGICAL FIX]`: Proposed change curing the root defect at the origin.
- `[BLAST RADIUS]`: All callers and consumers audited via `grep_search`.

### 3. Blast Radius & Regression Shield
- Before modifying any shared function signature, return type, or state structure, audit all callers using `grep_search`.
- Ensure changes do not break downstream consumers or introduce silent regressions.

### 4. The 2-Attempt Circuit Breaker
- Limit any solution hypothesis to a **maximum of 2 attempts**:
  - **Attempt 1:** Formulate hypothesis from direct inspection, apply surgical fix, verify.
  - **Attempt 2:** If Attempt 1 fails, analyze diagnostic feedback, refine the specific detail, verify.
  - **HALT:** If Attempt 2 fails, **STOP IMMEDIATELY**. Do not make a 3rd attempt on the same hypothesis. Trigger the Reverse Check.

### 5. Bidirectional Reverse-Check Protocol
When an approach fails twice, step back and execute a bidirectional trace:
- **Forward Trace:** User event $\rightarrow$ listener $\rightarrow$ handler $\rightarrow$ state/engine $\rightarrow$ failing output.
- **Reverse Check:** Failure symptom $\rightarrow$ call stack backwards $\rightarrow$ parameter origin $\rightarrow$ data generator.
- Find the exact point where caller expectations and callee behavior diverged.

### 6. Strict 3-Tier Verification Gate (Never Test Live if Static Fails)
- **Gate 1 (Static):** Validate syntax and types (`tsc --noEmit` or parser check). If Gate 1 fails, halt.
- **Gate 2 (Contract):** Verify logic, null checks, and imports against actual declarations.
- **Gate 3 (Live Retrying):** *Only* trigger live device (ARTEMIS) or browser verification once Gates 1 and 2 pass.

### 7. Platform Boundary & Hybrid App Awareness (Capacitor / Android / Web)
- Wrap `localStorage` in `try/catch` to handle Android WebView private mode restrictions.
- Ensure camera media tracks are explicitly stopped (`stream.getTracks().forEach(t => t.stop())`) when closing scanner modals.
- Provide graceful native fallbacks for browser-only APIs (`window.print`, `window.alert`).

### 8. Patch Minimalism (Anti-Sprawl)
- Keep fixes compact and surgical (typically under 20–30 lines).
- Never mask symptoms with empty `try/catch` blocks, arbitrary delay timers, or conditional bypasses.
