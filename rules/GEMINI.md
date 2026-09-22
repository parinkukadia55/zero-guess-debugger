<!-- BEGIN ZERO-GUESS DEBUGGER RULES -->
# Systematic Goal Planning, Interconnectivity & Zero-Guess Protocol

Strictly eliminate trial-and-error, speculative guesswork, hallucinated APIs, and quota-draining blind retries. Whenever a user request, feature task, or bug fix is initiated, adhere to the following protocol:

### Phase 0: Cross-Thread Context Synthesis (Unified Chat Rule)
- Synthesize all constraints, design preferences, and architectural decisions from previous chat turns.
- Never drop historical requirements (e.g. responsiveness, dark/light mode, role permissions) when working on new tasks.

### Phase 1: Goal Planning & Task Decomposition (Before Any Code is Touched)
1. **Define Concrete Goal:** Restate user request with unambiguous success criteria.
2. **What is Required:** Detail all files to create/modify, packages, schemas, and API contracts.
3. **How It Will Be Created:** Outline technical strategy, data flow, and architecture.
4. **Living Task Checklist:** Break down the work into discrete, ordered tasks (`Task 1`, `Task 2`, `Task 3`...).

### Phase 2: Sequential Step-by-Step Execution & Live Tracking
1. **One Task at a Time:** Execute tasks strictly sequentially. Never attempt all tasks at once.
2. **Live Status Updates:** After completing each task, show the updated checklist:
   - `[x] Completed: Task 1 (Summary of result)`
   - `[>] In Progress: Task 2`
   - `[ ] Pending: Task 3`

### Phase 3: Full-Surface Interconnectivity Audit (Anti-Partial-Update Shield)
Before considering any task complete, verify all 6 interconnected surfaces:
1. **API Endpoints:** Route, handler, request payload validation, and database updates.
2. **Routing & Navigation:** Router registration, navbar/sidebar links, and deep links.
3. **State Management:** Store, reducers, caching, and reactive propagation.
4. **UI Components (Dual-Mode):** Explicit styling in both Light Mode AND Dark Mode (zero color collisions).
5. **Cross-Panel Interconnectivity:** If connected to an Admin Panel or Home Panel, verify what connects and where. Verify changes in the Admin Panel immediately propagate and render in the Home/User panel.
6. **Error & Fallback States:** Skeletons, empty states, and error toasts.

### Phase 4: Zero-Guess Debugging Safeguards
1. **Zero Hallucination Mandate:** Ground every symbol in actual source code before writing fixes.
2. **Mandatory Pre-Fix Diagnostic Card:**
   - `[SYMPTOM]`     : Verbatim error message or observable defect.
   - `[LOCATION]`    : Exact file path, function, and verified line numbers.
   - `[ROOT CAUSE]`  : The exact mechanical failure mechanism.
   - `[SURGICAL FIX]`: Concrete change addressing the origin.
   - `[BLAST RADIUS]`: All callers/consumers, routes, endpoints, and panels audited via `grep_search`.
3. **Blast Radius & Regression Shield:** Audit all callers before modifying shared utilities.
4. **The 2-Attempt Circuit Breaker:** Max 2 attempts per hypothesis. If Attempt 2 fails, HALT and trigger Reverse Check.
5. **Bidirectional Reverse-Check Protocol:** Forward trace (Admin Panel -> Endpoint -> Router -> Home UI) and reverse check (failure backwards to origin).
6. **Strict 3-Tier Verification Gate:** Gate 1: Static (`tsc --noEmit`) -> Gate 2: Contract/Interconnect check -> Gate 3: Live retrying.
7. **Platform Boundary Awareness:** Sandboxed storage fallbacks, camera track teardown, and native overrides.
8. **Patch Minimalism:** Surgical fixes (under 20-30 lines). No symptom-masking with empty catches or arbitrary delay timers.
<!-- END ZERO-GUESS DEBUGGER RULES -->
