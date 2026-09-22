# Project Guidelines & Systematic Execution Protocol

## Anti-Trial-and-Error & Zero-Guess Mandate

When working on this project, trial-and-error debugging, speculative guessing, hallucinated APIs, and quota-draining blind retries are strictly prohibited. These practices waste developer time, burn AI quota, and cause regression cascades.

---

### Phase 0: Cross-Thread Context Synthesis (Unified Chat Rule)
- Synthesize all constraints, design preferences, and architectural decisions from previous chat turns.
- Never drop historical requirements (e.g. responsiveness, dark/light mode, multi-language parity, role permissions) when working on new tasks.

---

### Phase 1: Goal Planning & Task Decomposition (Before Any Code is Touched)
1. **Define Concrete Goal:** Restate user request with unambiguous success criteria.
2. **What is Required:** Detail all files to create/modify, packages, schemas, translation keys, and API contracts.
3. **How It Will Be Created:** Outline technical strategy, data flow, architecture, and multi-portal sync plan.
4. **Living Task Checklist:** Break down the work into discrete, ordered tasks (`Task 1`, `Task 2`, `Task 3`...).

---

### Phase 2: Sequential Step-by-Step Execution & Live Tracking
1. **One Task at a Time:** Execute tasks strictly sequentially. Never attempt all tasks at once.
2. **Live Status Updates:** After completing each task, show the updated checklist:
   - `[x] Completed: Task 1 (Summary of result)`
   - `[>] In Progress: Task 2`
   - `[ ] Pending: Task 3`

---

### Phase 3: Multi-Language (i18n) & Multi-Portal Interconnectivity Audit
Before considering any task complete, verify all interconnected layers:
1. **Multi-Language (i18n) Parity:**
   - Zero hardcoded user-facing strings; all text wrapped in translation lookups (`t('key')`).
   - Simultaneous parity across all supported locales (`en`, `hi`, `gu`, etc.).
   - Layout resilience: Containers handle 30% text expansion without breaking.
2. **Multi-Portal Interconnectivity (Web + Home + Admin + Mobile Shell):**
   - Single source of truth: Changes in Admin Panel immediately propagate through API/store to Home/User view.
   - Cross-portal route and auth guards: Verify deep links and role restrictions.
   - Dual-Theme UI: Explicit styling in both Light Mode AND Dark Mode (zero color collisions).
3. **API & Routing Integrity:** Route registration, navbar/sidebar links, error toasts, and empty states.

---

### Phase 4: Zero-Guess Debugging Safeguards
1. **Zero-Hallucination Rule:** Confirm every symbol's declaration in codebase before using it in a fix.
2. **Mandatory Pre-Fix Diagnostic Card:** Before editing code for a bug, state:
   - `[SYMPTOM]`     : Verbatim error message, status code, or observable defect.
   - `[LOCATION]`    : Exact file path, function, and verified line numbers.
   - `[ROOT CAUSE]`  : The exact mechanical failure mechanism.
   - `[SURGICAL FIX]`: Proposed change curing the root defect.
   - `[BLAST RADIUS]`: All callers/consumers, routes, endpoints, locales, and panels audited via symbol search.
3. **Blast Radius & Regression Shield (Caller Audit):** Map all callers before modifying shared utilities, props, or translation keys.
4. **The 2-Attempt Circuit Breaker:** Max 2 attempts per solution hypothesis. If Attempt 2 fails, STOP and trigger Reverse Check.
5. **Bidirectional Reverse-Check Protocol:** Forward trace (Admin Panel -> Endpoint -> Router -> Home UI across all locales) and reverse check (failure backwards to origin).
6. **Strict 3-Tier Verification Gate:** Gate 1: Static (`tsc --noEmit`) -> Gate 2: Contract/i18n/Interconnect check -> Gate 3: Live testing.
7. **Platform Boundary Awareness:** Storage sandboxing (`localStorage` fallbacks), camera stream disposal, and native overrides.
8. **Patch Minimalism:** Surgical fixes (under 20-30 lines). Never mask symptoms with empty `try/catch` blocks or arbitrary delay timers.
