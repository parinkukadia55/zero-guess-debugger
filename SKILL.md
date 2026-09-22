---
name: zero-guess-debugger
description: >-
  Stop AI coding agents from burning your quota with blind trial-and-error. Enforces goal definition,
  prerequisite analysis, living task checklists, sequential step-by-step execution with live completion
  updates, zero-hallucination, mandatory pre-fix diagnostic cards, 2-attempt circuit breakers,
  bidirectional reverse-checking, and strict 3-tier verification gates.
license: MIT
metadata:
  author: Parin Kukadia
  homepage: https://github.com/parinkukadia55/-zero-guess-debugger
  version: "1.1.0"
---

# 🛡️ Zero-Guess Debugger & Autonomous Execution Engine

> **Stop AI coding assistants and autonomous agents from burning your quota with blind trial-and-error.**  
> Combines **Goal Decomposition & Living Task Checklists** with an **Anti-Trial-and-Error Zero-Guess Debugging Protocol**.

---

## 🧭 Phase 1: Goal Decomposition & Planning (Before Any Code is Touched)

Whenever the user provides a request, feature requirement, or problem statement, the agent MUST first formulate a structured **Execution Plan**:

### 1. Define the Concrete Goal
- **User Request Summary:** Restate what the user is asking for in precise, unambiguous technical terms.
- **Success Criteria:** What exact condition defines that this task is 100% complete and working?

### 2. Prerequisite & Impact Analysis ("What is Required & How")
- **What is Required to Accomplish It:**
  - New files to create, existing files to modify, or files to delete.
  - Required packages, library imports, or API definitions.
  - Data contracts, schemas, or type models.
- **How It Will Be Created:**
  - Concrete architectural strategy, component hierarchy, function logic, and data flow.
  - Explicit platform boundary checks (Web, Android/Capacitor, iOS).

### 3. The Living Task Checklist
Break down the implementation into atomic, sequential milestones:
```markdown
### 📋 Task Checklist
- [ ] Task 1: [Short Actionable Title] — Description of deliverables
- [ ] Task 2: [Short Actionable Title] — Description of deliverables
- [ ] Task 3: [Short Actionable Title] — Description of deliverables
- [ ] Task 4: 3-Tier Verification Gate (Static -> Contract -> Live)
```

---

## ⚡ Phase 2: Sequential Step-by-Step Execution & Live Progress Tracking

Execute the task checklist **strictly one-by-one**:

1. **One Task at a Time:** Never attempt to do everything in one massive, chaotic blast. Focus entirely on the active task.
2. **Live Completion Status Updates:** As soon as a task is completed, report the updated checklist to the user with a concise summary of what was accomplished:
   ```markdown
   ### 📋 Execution Progress
   - [x] **Task 1: Define TypeScript schemas and contracts** — *Completed (Added `types/astrology.ts`)*
   - [>] **Task 2: Implement computation logic** — *IN PROGRESS*
   - [ ] Task 3: Build UI view component — *Pending*
   - [ ] Task 4: Run 3-Tier Verification Gate — *Pending*
   ```
3. **If an Error Occurs During a Task:** Pause immediately and invoke the **Zero-Guess Debugging Protocol** (Phase 3) to solve the root cause before moving forward.

---

## 🔒 Phase 3: The Zero-Guess Debugging Protocol

When encountering any error, bug, test failure, or unexpected behavior during execution or live testing:

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

### 1. Zero-Hallucination Mandate
- **Never guess API signatures:** Ground every referenced method, function argument, component prop, and file path in actual source code using `view_file` or `grep_search`.
- **Third-Party Reality Check:** Never assume external libraries export a function without checking `package.json` or `.d.ts` definitions.

### 2. Mandatory Pre-Fix Diagnostic Card
Before touching any source file, the agent MUST output a 5-point proof card:
```markdown
### 🔍 Diagnostic Card
- [SYMPTOM]     : Verbatim error message, status code, or observable defect.
- [LOCATION]    : Exact file path, function name, and verified line numbers.
- [ROOT CAUSE]  : The exact mechanical failure mechanism.
- [SURGICAL FIX]]: Proposed change curing the root defect at the origin.
- [BLAST RADIUS]: All callers and consumers audited via grep_search.
```

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
