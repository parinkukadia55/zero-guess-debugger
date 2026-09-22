# Project Guidelines & Systematic Execution Protocol

## Anti-Trial-and-Error & Zero-Guess Mandate

When working on this project, trial-and-error debugging, speculative guessing, hallucinated APIs, and quota-draining blind retries are strictly prohibited. These practices waste developer time, burn AI quota, and cause regression cascades.

---

### Phase 0: Cross-Thread Context Synthesis (Unified Chat Rule)
- Synthesize all constraints, design preferences, and architectural decisions from previous chat turns.
- Never drop historical requirements (e.g. responsiveness, dark/light mode, role permissions) when working on new tasks.

---

### Phase 1: Goal Planning & Task Decomposition (Before Any Code is Touched)
1. **Define Concrete Goal:** Restate user request with unambiguous success criteria.
2. **What is Required:** Detail all files to create/modify, packages, schemas, and API contracts.
3. **How It Will Be Created:** Outline technical strategy, data flow, and architecture.
4. **Living Task Checklist:** Break down the work into discrete, ordered tasks (`Task 1`, `Task 2`, `Task 3`...).

---

### Phase 2: Sequential Step-by-Step Execution & Live Tracking
1. **One Task at a Time:** Execute tasks strictly sequentially. Never attempt all tasks at once.
2. **Live Status Updates:** After completing each task, show the updated checklist:
   - `[x] Completed: Task 1 (Summary of result)`
   - `[>] In Progress: Task 2`
   - `[ ] Pending: Task 3`

---

### Phase 3: Full-Surface Interconnectivity Audit (Anti-Partial-Update Shield)
Before considering any task complete, verify all 6 interconnected surfaces:
1. **API Endpoints:** Route, handler, request payload validation, and database updates.
2. **Routing & Navigation:** Router registration, navbar/sidebar links, and deep links.
3. **State Management:** Store, reducers, caching, and reactive propagation.
4. **UI Components (Dual-Mode):** Explicit styling in both Light Mode AND Dark Mode (zero color collisions).
5. **Cross-Panel Interconnectivity:** If connected to an Admin Panel or Home Panel, verify what connects and where. Verify changes in the Admin Panel immediately propagate and render in the Home/User panel.
6. **Error & Fallback States:** Skeletons, empty states, and error toasts.

---

### Phase 4: Zero-Guess Debugging Safeguards
1. **Zero-Hallucination Rule:** Confirm every symbol's declaration in codebase before using it in a fix.
2. **Mandatory Pre-Fix Diagnostic Card:** Before editing code for a bug, state:
   - `[SYMPTOM]`     : Verbatim error message, status code, or observable defect.
   - `[LOCATION]`    : Exact file path, function, and verified line numbers.
   - `[ROOT CAUSE]`  : The exact mechanical failure mechanism.
   - `[SURGICAL FIX]`: Proposed change curing the root defect.
   - `[BLAST RADIUS]`: All callers/consumers, routes, endpoints, and panels audited via symbol search.
3. **Blast Radius & Regression Shield (Caller Audit):** Map all callers before modifying shared utilities.
4. **The 2-Attempt Circuit Breaker:** Max 2 attempts per solution hypothesis. If Attempt 2 fails, STOP and trigger Reverse Check.
5. **Bidirectional Reverse-Check Protocol:** Forward trace (Admin Panel -> Endpoint -> Router -> Home UI) and reverse check (failure backwards to origin).
6. **Strict 3-Tier Verification Gate:** Gate 1: Static (`tsc --noEmit`) -> Gate 2: Contract/Interconnect check -> Gate 3: Live testing.
7. **Platform Boundary Awareness:** Storage sandboxing (`localStorage` fallbacks), camera stream disposal, and native overrides.
8. **Patch Minimalism:** Surgical fixes (under 20-30 lines). Never mask symptoms with empty `try/catch` blocks or arbitrary delay timers.
