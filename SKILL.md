---
name: zero-guess-debugger
description: >-
  Stop AI coding agents from burning your quota with blind trial-and-error. Enforces cross-thread
  context synthesis, goal definition, prerequisite analysis, living task checklists, sequential
  step-by-step execution with live completion updates, multi-language (i18n) parity, multi-portal
  interconnectivity (Web + User Home + Admin Panel + Mobile/Native), zero-hallucination, mandatory
  pre-fix diagnostic cards, 2-attempt circuit breakers, bidirectional reverse-checking, and strict
  3-tier verification gates.
license: MIT
metadata:
  author: Parin Kukadia
  homepage: https://github.com/parinkukadia55/zero-guess-debugger
  version: "1.3.0"
---

# 🛡️ Zero-Guess Debugger & Autonomous Execution Engine

> **Stop AI coding assistants and autonomous agents from burning your quota with blind trial-and-error.**  
> Combines **Cross-Thread Context Synthesis**, **Goal Planning & Living Task Checklists**, **Multi-Language (i18n) Parity**, **Multi-Portal Interconnectivity (Web + User + Admin + Mobile Shell)** with an **Anti-Trial-and-Error Zero-Guess Debugging Protocol**.

---

## 🧵 Phase 0: Cross-Thread Context Synthesis (The Unified Chat Rule)

Before generating any plan or touching code, the agent MUST synthesize the entire conversation history:
1. **Combine All Thread Decisions:** Gather all requirements, architectural constraints, design decisions, and preferences stated across previous user messages and turns.
2. **Never Drop Historical Context:** Never omit previously agreed features (e.g. dual-theme support, multi-language parity, mobile responsiveness, offline fallbacks, or role permissions) when working on new tasks.
3. **Explicit Assumption Check:** If the user request relates to a previously discussed module or portal, trace the dependency chain before proceeding.

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
  - Translation keys across all supported locales (`en`, `hi`, `gu`, etc.).
- **How It Will Be Created:**
  - Concrete architectural strategy, component hierarchy, function logic, and data flow.
  - Explicit platform boundary checks (Web, Android/Capacitor, iOS, Desktop).
  - Cross-portal data synchronization plan (Web $\leftrightarrow$ User Home $\leftrightarrow$ Admin Panel $\leftrightarrow$ Native Shell).

### 3. The Living Task Checklist
Break down the implementation into atomic, sequential milestones:
```markdown
### 📋 Task Checklist
- [ ] Task 1: [Short Actionable Title] — Description of deliverables
- [ ] Task 2: [Short Actionable Title] — Description of deliverables
- [ ] Task 3: Multi-Language (i18n) Parity Audit (All locales updated, zero hardcoded text)
- [ ] Task 4: Multi-Portal Interconnectivity Audit (Web <-> User Home <-> Admin Panel)
- [ ] Task 5: 3-Tier Verification Gate (Static -> Contract -> Live)
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
   - [ ] Task 3: Multi-Language Parity (en, hi, gu) — *Pending*
   - [ ] Task 4: Connect Admin Panel to Home Panel & Endpoints — *Pending*
   - [ ] Task 5: Run 3-Tier Verification Gate — *Pending*
   ```
3. **If an Error Occurs During a Task:** Pause immediately and invoke the **Zero-Guess Debugging Protocol** (Phase 5) to solve the root cause before moving forward.

---

## 🌍 Phase 3: Multi-Language (i18n) Parity Shield

In multilingual applications, AI agents frequently break localization by hardcoding English strings or leaving non-English dictionaries desynchronized. The agent must enforce:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       MULTI-LANGUAGE (i18n) AUDIT                           │
├──────────────────────────────┬──────────────────────────────────────────────┤
│ 1. Zero Hardcoded Strings    │ All UI text wrapped in t('key') / dict lookup│
│ 2. All-Locales Parity        │ Every new key added to en, hi, gu, etc.      │
│ 3. Layout Resilience         │ UI handles 30% text expansion without breaks │
│ 4. Cross-Portal Sync         │ Language switch syncs modals, PDFs, and views│
└──────────────────────────────┴──────────────────────────────────────────────┘
```

1. **Zero Hardcoded Strings:** Every button label, header, input placeholder, validation toast, and tooltip must use the i18n translation system. Raw strings like `<button>Submit</button>` are strictly prohibited.
2. **Simultaneous All-Locales Parity:** When a translation key is added or modified, update **ALL supported language dictionaries** in the same change. Never leave non-English locales missing keys.
3. **Text Expansion & Layout Resilience:** Languages like Hindi and Gujarati frequently require 20%–35% more horizontal space than English. Ensure containers, buttons, and table headers use flexible layouts (`flex-wrap`, `min-w`, truncate with tooltips) to prevent layout overflows.
4. **Export & Deep Artifact Sync:** Ensure language preference dynamically propagates to generated PDFs, printed charts, shared URLs, and local storage (`jyotish_lang_chosen`).

---

## 🌐 Phase 4: Multi-Portal Ecosystem Interconnectivity (Web + Home + Admin + Mobile)

When an application consists of multiple interconnected portals or shells, the agent must map and verify the complete ecosystem wire:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────┐
│                           MULTI-PORTAL INTERCONNECTIVITY MATRIX                                │
├──────────────────────────────┬─────────────────────────────────────────────────────────────────┤
│ 1. Public Web Portal         │ Landing pages, marketing, SEO, guest calculation forms          │
│ 2. User / Home Portal        │ Dashboard, user charts, history, saved dossiers, personal state │
│ 3. Admin Panel               │ Master configs, translation overrides, feature toggles, analytics│
│ 4. Mobile Shell (Capacitor)  │ Native camera bridges, hardware sensors, offline storage cache  │
└──────────────────────────────┴─────────────────────────────────────────────────────────────────┘
```

### The 4-Portal Synchronization Rules:
1. **Trace What Connects and Where:**
   - **Producer Portal:** Where is the data configured or initiated? (e.g. Admin Panel toggle, User form input).
   - **Transport & Storage:** Which API endpoint validates, persists, and broadcasts the change?
   - **Consumer Portals:** How do the Public Web, User Home, and Mobile Shell invalidate cache and reflect the update?
2. **Single Source of Truth:** Changes saved in the **Admin Panel** must propagate through the shared API/store and immediately reflect in the **User / Home Panel** without requiring manual database edits or code redeployment.
3. **Cross-Portal Routing & Auth Guards:** Verify that admin-only routes remain protected against unauthenticated users, while deep links between the web portal and mobile app resolve to the correct view.
4. **Dual-Theme UI Component Audit:** Every component across all portals must be styled for **both Light Mode AND Dark Mode** (no color collisions, zero unstyled backgrounds).

---

## 🔒 Phase 5: The Zero-Guess Debugging Protocol

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
                      │ Gate 2: Contract & Interconnect Checks │
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
- [SURGICAL FIX]: Proposed change curing the root defect at the origin.
- [BLAST RADIUS]: All callers, routes, endpoints, locales, and portals audited via grep_search.
```

### 3. Blast Radius & Regression Shield
- Before modifying any shared function signature, return type, state structure, or translation key, audit all callers using `grep_search`.
- Ensure changes do not break downstream consumers or introduce silent regressions across other portals.

### 4. The 2-Attempt Circuit Breaker
- Limit any solution hypothesis to a **maximum of 2 attempts**:
  - **Attempt 1:** Formulate hypothesis from direct inspection, apply surgical fix, verify.
  - **Attempt 2:** If Attempt 1 fails, analyze diagnostic feedback, refine the specific detail, verify.
  - **HALT:** If Attempt 2 fails, **STOP IMMEDIATELY**. Do not make a 3rd attempt on the same hypothesis. Trigger the Reverse Check.

### 5. Bidirectional Reverse-Check Protocol
When an approach fails twice, step back and execute a bidirectional trace:
- **Forward Trace:** Admin Panel Event $\rightarrow$ Endpoint $\rightarrow$ Store/State $\rightarrow$ Router $\rightarrow$ Home Panel UI (Light & Dark, all Locales).
- **Reverse Check:** Failure symptom $\rightarrow$ call stack backwards $\rightarrow$ parameter origin $\rightarrow$ data generator.
- Find the exact point where caller expectations and callee behavior diverged.

### 6. Strict 3-Tier Verification Gate (Never Test Live if Static Fails)
- **Gate 1 (Static):** Validate syntax and types (`tsc --noEmit` or parser check). If Gate 1 fails, halt.
- **Gate 2 (Contract, i18n & Interconnect Checks):** Verify logic, null checks, import validity, all locale keys, and Admin $\leftrightarrow$ Home portal data flow.
- **Gate 3 (Live Retrying):** *Only* trigger live device (ARTEMIS) or browser verification once Gates 1 and 2 pass.

### 7. Platform Boundary & Hybrid App Awareness (Capacitor / Android / Web)
- Wrap `localStorage` in `try/catch` to handle Android WebView private mode restrictions.
- Ensure camera media tracks are explicitly stopped (`stream.getTracks().forEach(t => t.stop())`) when closing scanner modals.
- Provide graceful native fallbacks for browser-only APIs (`window.print`, `window.alert`).

### 8. Patch Minimalism (Anti-Sprawl)
- Keep fixes compact and surgical (typically under 20–30 lines).
- Never mask symptoms with empty `try/catch` blocks, arbitrary delay timers, or conditional bypasses.
