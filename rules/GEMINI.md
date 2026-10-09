<!-- BEGIN ZERO-GUESS DEBUGGER RULES -->
# Systematic Goal Planning, Multi-Language, Multi-Portal & Eyesight Protocol

Strictly eliminate trial-and-error, speculative guesswork, hallucinated APIs, and quota-draining blind retries. Whenever a user request, feature task, or bug fix is initiated, adhere to the following protocol:

### Phase 0: Cross-Thread Context Synthesis (Unified Chat Rule)
- Synthesize all constraints, design preferences, and architectural decisions from previous chat turns.
- Never drop historical requirements (e.g. responsiveness, dark/light mode, multi-language parity, role permissions) when working on new tasks.

### Phase 1: Goal Planning & Wireframe Mapping (Before Any Code is Touched)
1. **Define Concrete Goal:** Restate user request with unambiguous success criteria.
2. **Wireframe & Route Mapping:** In your internal reasoning, map all views, routes, interactive buttons, form triggers, and endpoints.
3. **What is Required (Tech & Notification Fidelity):** Detail all files to create/modify, packages, schemas, translation keys, visual assets, and API contracts. Strictly honor user-specified tech stack and notification tools (zero library swapping).
4. **The Clarification Gate:** If requirements, notification schedules, or technical directions are ambiguous or confusing, stop and ask the user for confirmation (`ask_question`). Never take speculative automatic decisions.
5. **How It Will Be Created (Lean Code Mandate):** Outline technical strategy, data flow, architecture, and multi-portal sync plan. Enforce lean code minimalism: direct, idiomatic implementations without over-engineered boilerplate ("use less coding, don't write too much code").
6. **Living Task Checklist:** Break down the work into discrete, ordered tasks (`Task 1`, `Task 2`, `Task 3`...).


### Phase 2: Sequential Step-by-Step Execution & Live Tracking
1. **One Task at a Time:** Execute tasks strictly sequentially. Never attempt all tasks at once.
2. **Live Status Updates:** After completing each task, show the updated checklist:
   - `[x] Completed: Task 1 (Summary of result)`
   - `[>] In Progress: Task 2`
   - `[ ] Pending: Task 3`

### Phase 3: Media & Visual Asset Generation (Native Generative Model Mandate)
- When generating images, videos, mockups, or UI visuals:
  - **MANDATORY:** Always use the dedicated generative AI image model / tool (`generate_image`).
  - **STRICTLY PROHIBITED:** Never use Python scripts (PIL, Pillow, matplotlib, OpenCV, MoviePy) to draw or simulate images or videos. Script plotting is permitted only for mathematical data charts.

### Phase 4: Multi-Language (i18n) & Multi-Portal Interconnectivity Audit
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

### Phase 5: Zero-Guess Debugging Safeguards
1. **Zero Hallucination Mandate:** Ground every symbol in actual source code before writing fixes.
2. **Mandatory Pre-Fix Diagnostic Card:**
   - `[SYMPTOM]`     : Verbatim error message or observable defect.
   - `[LOCATION]`    : Exact file path, function, and verified line numbers.
   - `[ROOT CAUSE]`  : The exact mechanical failure mechanism.
   - `[SURGICAL FIX]`: Concrete change addressing the origin.
   - `[BLAST RADIUS]`: All callers/consumers, routes, endpoints, locales, and panels audited via `grep_search`.
3. **Blast Radius & Regression Shield:** Audit all callers before modifying shared utilities, props, or translation keys.
4. **The 2-Attempt Circuit Breaker:** Max 2 attempts per hypothesis. If Attempt 2 fails, HALT and trigger Reverse Check.
5. **Bidirectional Reverse-Check Protocol:** Forward trace (Admin Panel -> Endpoint -> Router -> Home UI across all locales) and reverse check (failure backwards to origin).
6. **Strict 3-Tier Verification Gate:** Gate 1: Static (`tsc --noEmit`) -> Gate 2: Contract/i18n/Interconnect check -> Gate 3: Live testing with Stale-Build Guard.
7. **Platform Boundary Awareness:** Sandboxed storage fallbacks, camera track teardown, and native overrides.
8. **Patch Minimalism:** Surgical fixes (under 20-30 lines). No symptom-masking with empty catches or arbitrary delay timers.
9. **Stale-Build Guard & Timestamp Verification:** Always check debug or release app date and timestamp before testing. If the build artifact is older than recent source code changes, build a fresh new version and sync/install to device before running any tests.

### Phase 6: End-of-Run Broken Item Eyesight Report
At the end of every conversation or audit, output a clear Eyesight Report:
- **🟢 Verified & Operational Elements:** Confirmed routes and working buttons.
- **🔴 Broken / Dead / Unlinked Elements Found:** Broken buttons, unhandled onclicks, missing routes, and 404 endpoints with exact file locations.
- **🛠️ Remediation Roadmap:** Prioritized action items to fix remaining broken items.

### Phase 7: Persistent Feature Memory Board (`MEMORY_BOARD.md`)
- Maintain `./MEMORY_BOARD.md` in repository root as the persistent source of truth for all features, routes, and health states.
- **Full-Repo Scan Mandate:** When scanning repository or folders, traverse all views, routes, handlers, and APIs; cross-check against `MEMORY_BOARD.md` to catch misplaced, unlinked, or forgotten features.
- **Problem & Rectification Ledger:** Log all discovered defects, track health (`🟢 Operational`, `🟡 Degraded`, `🔴 Broken`), and record fix histories for every feature.
- **Pre-Action Check:** Always inspect the Memory Board before adding or refactoring features to prevent duplicate reinvention or route collisions.

### Phase 8: Autonomous Self-Healing Closed-Loop & Full-Stack Security Engine
- **Universal Mandate:** Applies across any AI CLI, API, script, or IDE workflow.
- **Closed-Loop Cycle:** Plan & Memorize (`MEMORY_BOARD.md`) ➔ Atomic Task List ➔ Exhaustive Coding ➔ 4-Dimensional Audit ➔ Memory Board Rectification ➔ Loop until 100% result achieved.
- **4-Dimensional Audit Matrix:**
  1. `🎨 UI/UX Logic:` Loading/disabled/error states, explicit **Light AND Dark Mode** contrast parity, viewport safe-areas.
  2. `🛣️ Routes & Navigation:` Router table registration, deep links, auth guards, zero unhandled `onclick` stubs.
  3. `⚙️ API & Backend:` Schema validation, explicit HTTP status codes (`200`/`400`/`401`/`500`), resource teardown (listeners, streams).
  4. `🛡️ Security & Hardening:` Zero hardcoded secrets, input sanitization (XSS/injection defense), CORS/storage sandboxing.
- **Loop to 100% Success:** Never stop at first-draft code. If flaws or vulnerabilities exist, log on `MEMORY_BOARD.md`, fix immediately, re-audit, and repeat until 100% operational certainty.

---

### Phase 9: Notification & Tech Stack Fidelity, The Clarification Gate & Lean Code Minimalism
1. **Tech Stack & Notification Grounding:**
   - Honor exact notification channels (Capacitor LocalNotifications, Push, FCM, Web Notifications) and libraries specified by user or repo.
   - Zero hallucination or unrequested library swapping.
2. **The Clarification Gate (Mandatory Confirmation Over Speculation):**
   - If requirements, triggers, schedules, or architectural directions are unclear or ambiguous: **DO NOT guess or make auto-decisions**.
   - Directly ask the user for confirmation via interactive prompt (`ask_question`) before writing code.
3. **Lean Code Minimalism ("Use Less Coding — Don't Write Too Much Code"):**
   - Maximum functional signal with minimal lines of clean, idiomatic code.
   - Ban over-engineering, gratuitous wrappers, and redundant boilerplate.
   - Keep bug fixes surgical (under 20–30 lines) while maintaining 100% production completeness (zero placeholders).
<!-- END ZERO-GUESS DEBUGGER RULES -->
