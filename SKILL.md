---
name: zero-guess-debugger
description: >-
  Stop AI coding agents from burning your quota with blind trial-and-error. Enforces cross-thread
  context synthesis, architectural route & wireframe mapping, goal definition, prerequisite analysis,
  living task checklists, sequential step-by-step execution with live completion updates, multi-language
  (i18n) parity, multi-portal interconnectivity (Web + User Home + Admin Panel + Mobile/Native),
  native AI image/video generation models, zero-hallucination, mandatory pre-fix diagnostic cards,
  2-attempt circuit breakers, bidirectional reverse-checking, strict 3-tier verification gates with
  stale-build timestamp guards, persistent feature memory board (MEMORY_BOARD.md) with full-repo anti-misplacement scans,
  end-of-run eyesight triage reports, and autonomous self-healing closed-loop audits (Plan -> Memorize -> Task -> Code -> Error & Security Audit -> Rectify -> 100% Outcome Loop across UI/UX, Routes, APIs, Backend, and Security).
license: MIT
metadata:
  author: Parin Kukadia
  homepage: https://github.com/parinkukadia55/zero-guess-debugger
  version: "1.8.0"
---

# 🛡️ Zero-Guess Debugger & Autonomous Execution Engine

> **Stop AI coding assistants and autonomous agents from burning your quota with blind trial-and-error.**  
> Combines **Cross-Thread Context Synthesis**, **Architectural Wireframe & Route Mapping**, **Goal Planning & Living Task Checklists**, **Multi-Language (i18n) Parity**, **Multi-Portal Interconnectivity (Web + User + Admin + Mobile Shell)**, **Native AI Generative Media Mandates**, **Zero-Guess Debugging**, **Stale-Build Timestamp Verification Guards**, **Persistent Feature Memory Board (MEMORY_BOARD.md)**, **End-of-Run Broken Item Eyesight Triage**, and an **Autonomous Self-Healing Closed-Loop Engine (100% Verification across UI/UX, Routes, APIs, Backend & Security)**.

---

## 🧵 Phase 0: Cross-Thread Context Synthesis (The Unified Chat Rule)

Before generating any plan or touching code, the agent MUST synthesize the entire conversation history:
1. **Combine All Thread Decisions:** Gather all requirements, architectural constraints, design decisions, and preferences stated across previous user messages and turns.
2. **Never Drop Historical Context:** Never omit previously agreed features (e.g. dual-theme support, multi-language parity, mobile responsiveness, offline fallbacks, or role permissions) when working on new tasks.
3. **Explicit Assumption Check:** If the user request relates to a previously discussed module or portal, trace the dependency chain before proceeding.

---

## 🧭 Phase 1: Goal Planning, Wireframe & Route Mapping (Before Any Code is Touched)

Whenever the user provides a request, feature requirement, or problem statement, the agent MUST first formulate a structured **Execution Plan**:

### 1. Define the Concrete Goal
- **User Request Summary:** Restate what the user is asking for in precise, unambiguous technical terms.
- **Success Criteria:** What exact condition defines that this task is 100% complete and working?

### 2. Architectural Wireframe & Route Mapping
In its internal reasoning, the agent must build a structural map of the affected views and navigation:
- **Routes & Views Mapped:** What routes, pages, tabs, or modals are involved?
- **Interactive Buttons & Triggers:** What buttons, forms, or actions live on each view?
- **Underlying Endpoints & Handlers:** What API endpoints or event handlers are connected to each button?

### 3. Prerequisite & Impact Analysis ("What is Required & How")
- **What is Required to Accomplish It:**
  - New files to create, existing files to modify, or files to delete.
  - Required packages, library imports, or API definitions.
  - Data contracts, schemas, or type models.
  - Translation keys across all supported locales (`en`, `hi`, `gu`, etc.).
  - Visual assets: Use generative AI image models (`generate_image`), never script-based fallbacks.
- **How It Will Be Created:**
  - Concrete architectural strategy, component hierarchy, function logic, and data flow.
  - Explicit platform boundary checks (Web, Android/Capacitor, iOS, Desktop).
  - Cross-portal data synchronization plan (Web $\leftrightarrow$ User Home $\leftrightarrow$ Admin Panel $\leftrightarrow$ Native Shell).

### 4. The Living Task Checklist
Break down the implementation into atomic, sequential milestones:
```markdown
### 📋 Task Checklist
- [ ] Task 1: [Short Actionable Title] — Description of deliverables
- [ ] Task 2: [Short Actionable Title] — Description of deliverables
- [ ] Task 3: Multi-Language (i18n) Parity Audit (All locales updated, zero hardcoded text)
- [ ] Task 4: Multi-Portal Interconnectivity Audit (Web <-> User Home <-> Admin Panel)
- [ ] Task 5: 3-Tier Verification Gate (Static -> Contract -> Live with Stale-Build Guard)
- [ ] Task 6: Broken Button, Route & Endpoint Eyesight Report
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
   - [ ] Task 5: Run 3-Tier Verification Gate (with Stale-Build Guard) — *Pending*
   - [ ] Task 6: Eyesight Triage Audit — *Pending*
   ```
3. **If an Error Occurs During a Task:** Pause immediately and invoke the **Zero-Guess Debugging Protocol** (Phase 6) to solve the root cause before moving forward.

---

## 🎨 Phase 3: Media & Asset Generation (Native Generative Model Mandate)

When the user requests to generate an image, video, banner, mockup, icon, or visual asset:

- **MANDATORY: Dedicated Generative AI Model:**
  - Always invoke the native image generation tool / model (`generate_image`).
  - Provide a rich, art-directed prompt, descriptive `ImageName`, and appropriate `AspectRatio` (`1:1`, `16:9`, `9:16`, `4:3`, `3:2`).
- **STRICTLY PROHIBITED: No Python Scripts for Visuals:**
  - Never write or execute Python scripts (e.g. using `PIL`/`Pillow`, `matplotlib`, `opencv`, `moviepy`, `pygame`, or canvas rendering scripts) to programmatically draw, generate, or simulate images or videos.
  - *Exception:* Script-based plotting is permitted *only* when the user explicitly requests mathematical data charts or statistical plots.

---

## 🌍 Phase 4: Multi-Language (i18n) Parity Shield

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

1. **Zero Hardcoded Strings:** Every button label, header, input placeholder, validation toast, and tooltip must use the translation key system.
2. **All-Locales Parity:** When a translation key is added or modified, update **ALL supported language dictionaries** in the same change.
3. **Text Expansion Resilience:** Indic scripts (Hindi, Gujarati) require 20%–35% more space than English. Layouts must gracefully prevent text truncation or broken line wraps.
4. **Deep Artifact Sync:** Ensure language preference dynamically propagates to generated PDFs, printed charts, shared URLs, and local storage (`jyotish_lang_chosen`).

---

## 🌐 Phase 5: Multi-Portal Ecosystem Interconnectivity (Web + Home + Admin + Mobile)

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

1. **Trace What Connects and Where:**
   * **Producer Portal:** Where is the data configured? (e.g. Admin Panel toggle, User form input).
   * **Transport & Storage:** Which API endpoint validates, persists, and broadcasts the change?
   * **Consumer Portals:** How do the Public Web, User Home, and Mobile Shell invalidate cache and reflect the update?
2. **Single Source of Truth:** Changes saved in the **Admin Panel** must propagate through the shared API/store and immediately reflect in the **User / Home Panel** without manual database intervention.
3. **Dual-Theme UI Component Audit:** Every component across all portals must be styled for **both Light Mode AND Dark Mode** (no color collisions, zero unstyled backgrounds).

---

## 🔒 Phase 6: The Zero-Guess Debugging Protocol

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
                      │         (with Stale-Build Guard)       │
                      └────────────────────────────────────────┘
```

### The 9 Core Safeguards

1. **Zero-Hallucination Mandate:** Never assume API signatures, props, or file paths without verifying source code.
2. **Mandatory Pre-Fix Diagnostic Card:**
   ```markdown
   ### 🔍 Diagnostic Card
   - [SYMPTOM]     : Verbatim error message or observable defect.
   - [LOCATION]    : Exact file path, function, and verified line numbers.
   - [ROOT CAUSE]  : Mechanical failure explanation.
   - [SURGICAL FIX]: Concrete change addressing the origin.
   - [BLAST RADIUS]: All callers, routes, endpoints, locales, and portals audited via grep_search.
   ```
3. **Blast Radius & Regression Shield:** Audit all consumers before altering shared functions.
4. **The 2-Attempt Circuit Breaker:** Maximum 2 attempts per solution hypothesis. If Attempt 2 fails, **HALT** and trigger a Reverse Check.
5. **Bidirectional Reverse-Check:** Trace forward: `Admin Panel -> Endpoint -> Store -> Router -> Home UI (Light/Dark, all Locales)`; trace backward from error stack to data origin.
6. **Strict 3-Tier Verification Gate:** Gate 1 (Static: `tsc --noEmit`) $\rightarrow$ Gate 2 (Contract, i18n & Interconnect checks) $\rightarrow$ Gate 3 (Live device/browser testing with Stale-Build Guard).
7. **Platform Boundary Awareness:** Storage sandboxing (`localStorage` fallbacks), camera stream teardown (`track.stop()`), and native overrides for Android/Capacitor.
8. **Patch Minimalism:** Surgical fixes (under 20–30 lines). No symptom-masking with empty catches or arbitrary timeouts.
9. **Stale-Build Guard & Timestamp Verification:** Always verify debug/release app date and timestamp against source code edits before live testing. If the binary is older or missing, trigger a fresh rebuild before running any test.

### ⏱️ The Stale-Build Guard & Timestamp Verification Protocol (Before ANY Live Testing)

Never run automated or manual live tests (ARTEMIS, Playwright, Espresso, Android APK, or browser preview) against a stale build artifact:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 STALE-BUILD GUARD & TIMESTAMP DECISION TREE                 │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Check Target Artifact Timestamp  (e.g. app-debug.apk / dist/index.html)  │
│ 2. Check Latest Source Timestamp    (e.g. src/**, public/**, config files)  │
│                                                                             │
│ [ Artifact Time < Source Time ] ──► STALE BUILD DETECTED!                   │
│                                     • BANNED: Do NOT run tests              │
│                                     • ACTION: Trigger clean rebuild & sync  │
│                                     • VERIFY: Check new timestamp > source  │
│                                     • DEPLOY: Install fresh binary to device│
│                                     • ONLY THEN execute live testing        │
│                                                                             │
│ [ Artifact Time >= Source Time ] ─► BUILD FRESH & UP-TO-DATE!               │
│                                     • Proceed safely to live verification   │
└─────────────────────────────────────────────────────────────────────────────┘
```

1. **Compare Timestamps Prior to Test Execution:**
   - **Target Artifact:** Query `LastWriteTime` of the active debug or release app binary (`android/app/build/outputs/apk/debug/app-debug.apk`, `android/app/build/outputs/apk/release/app-release.apk`, `dist/index.html`, etc.).
   - **Source Code Changes:** Query `LastWriteTime` of the latest modified source files (`src/`, `www/`, `android/`, etc.).
2. **Prevent False-Failure Spirals:**
   - Testing against an outdated APK or bundle causes agents to see bugs that were already fixed in code, leading to phantom regressions, false diagnostic cards, and quota exhaustion.
3. **Mandatory Fresh Rebuild Action:**
   - If the artifact is older than source changes or missing, immediately execute the build pipeline (`npm run build`, `npx cap sync`, `./gradlew assembleDebug` or `./gradlew assembleRelease`).
   - Confirm the new binary's timestamp is strictly newer than the source changes.
   - Deploy/reinstall the fresh binary to the connected device or emulator before running assertions.

---

## 👁️ Phase 7: End-of-Run Broken Item Eyesight Report

At the end of any conversation, build session, or audit turn, the agent MUST summarize its architectural findings and give the user clear **"Eyesight"** into all operational vs broken elements:

```markdown
### 👁️ Broken Buttons, Routes & Endpoints Eyesight Report

#### 🟢 Verified & Operational Elements:
- [Route/View]: Path or View name -> Confirmed operational.
- [Button/Trigger]: Action name -> Correctly calls handler/endpoint.

#### 🔴 Broken / Dead / Unlinked Elements Found:
- [Broken Button]: `<button onclick="app.missingHandler()">` in `index.html:4343` -> Handler is undefined.
- [Unregistered Route]: `/settings/profile` in `Navbar.tsx:42` -> Not declared in router configuration.
- [Dead Endpoint]: `POST /api/save-kundli` -> Route returns 404 / handler unmounted.
- [Desynced Panel]: Admin toggle "Enable Muhurat" has no listener in User Home Panel.

#### 🛠️ Immediate Remediation Roadmap:
1. Priority 1: Add shim/implementation for missing button handlers.
2. Priority 2: Register missing routes in router table.
3. Priority 3: Mount dead endpoints in server controller.
```

This guarantees that the user is never left wondering what remains broken behind the scenes.

---

## 🧠 Phase 8: Persistent Feature Memory Board & Rectification Ledger (`MEMORY_BOARD.md`)

To completely eliminate **AI Context Amnesia**—where agents scan a repository, forget previously implemented features across chat turns, misplace components, or re-implement duplicate/conflicting logic—the agent MUST maintain a persistent **Feature Memory Board**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 PERSISTENT FEATURE MEMORY BOARD LIFECYCLE                   │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Read MEMORY_BOARD.md (Load complete mental model of all existing features│
│ 2. Full-Repo Scan (Detect new features, verify known routes & handlers)    │
│ 3. Reconciliation (Catch misplaced, disconnected, or desynced features)    │
│ 4. Rectification & Problem Audit (Track defects, record fixes, log health) │
│ 5. Persist MEMORY_BOARD.md (Write back to disk for cross-thread permanence)│
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1. The Standard Memory Board Schema (`MEMORY_BOARD.md`)
The file lives in the repository root (`./MEMORY_BOARD.md`) and acts as the project's permanent feature knowledge base:

```markdown
# 🧠 Project Feature Memory Board & Rectification Ledger

> **Single Source of Truth for Codebase Features, Routes, Status & Rectifications**
> Last Scanned / Synced: YYYY-MM-DD HH:MM | Total Features: N | Operational: X | In Rectification: Y

## 🗺️ Feature Registry Matrix

| ID | Feature Name | Domain / Portal | Route / View File | Backing Logic / Endpoints | Health Status | Known Problems / Notes | Rectification History |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `FEAT-001` | Lagna Kundli Calculator | Web / User | `/kundli`, `KundliView.tsx` | `engine/chart.ts::computeLagna` | 🟢 Operational | None | Fixed timezone offset in v1.2 |
| `FEAT-002` | Admin Muhurat Manager | Admin | `/admin/muhurat` | `api/admin.ts::toggleMuhurat` | 🟡 Degraded | Toggle desynced from Home Panel | In Rectification: adding store listener |
| `FEAT-003` | PDF Dossier Export | User Dashboard | `/export/pdf` | `services/pdf.ts::buildPdf` | 🔴 Broken | Missing Gujarati font rendering | Issue logged; pending font asset embed |
```

### 2. Full-Repo Scan & Anti-Misplacement Protocol
Whenever the user asks to **"scan full repo"**, **"scan all files"**, or **"audit features"**:
1. **Load Memory Board:** Check for an existing `MEMORY_BOARD.md`. If missing, initialize one immediately.
2. **Deep Architectural Traversal:** Walk all route configs, page components, button handlers, API controllers, and state stores.
3. **Reconcile Against Memory Board:**
   - **Discover New Features:** Register newly created views/features with a unique ID (`FEAT-XXX`).
   - **Detect Misplaced Features:** Flag features that exist in code but disappeared from navigation menus, routes, or dashboards.
   - **Detect Orphaned Endpoints:** Flag APIs or backend functions that have no UI trigger.
4. **Health State Classification:**
   - `🟢 Operational`: Fully wired, route works, handler operational, Light/Dark mode styled, i18n keys present.
   - `🟡 Degraded`: Functional but has minor flaws (e.g. missing translation key, UI styling glitch in dark mode).
   - `🔴 Broken`: Button throws error, route 404s, or backend endpoint missing.
   - `🔵 In Progress`: Actively being created or refactored.
5. **Rectification Tracking:**
   - Log any diagnosed problem in the `Known Problems / Notes` column.
   - When a bug fix or surgical change is applied, append a concrete note to `Rectification History` with the commit or file change summary.
6. **Persist & Update:** Write the updated `MEMORY_BOARD.md` back to disk before finishing the turn.

### 3. Pre-Action Cross-Check Mandate
Before creating any new component, altering routes, or debugging:
- **ALWAYS inspect `MEMORY_BOARD.md` first.**
- Never blindly recreate an existing feature or overwrite an established route without verifying its registry on the board.

---

## 🔄 Phase 9: Autonomous Self-Healing Closed-Loop & Full-Stack Security Engine (The 100% Outcome Loop)

> **Mandatory Universal Execution Rule:** Applies across **any AI agent, CLI (`agy`, Claude Code, Cursor, Windsurf), API integration, automated runner, or script**. First Plan & Memorize, construct atomic task lists, code exhaustively, run 4-layer audits (including deep security vulnerability scans), record findings in `MEMORY_BOARD.md`, and **continuously loop until 100% operational and security certainty is achieved**.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              AUTONOMOUS SELF-HEALING CLOSED LOOP (100% OUTCOME GATE)        │
├─────────────────────────────────────────────────────────────────────────────┤
│  1. PLAN & MEMORIZE     ──► Read & sync MEMORY_BOARD.md, historical context │
│            │                                                                │
│            ▼                                                                │
│  2. ATOMIC TASK LIST    ──► Ordered task checklist, explicit deliverables   │
│            │                                                                │
│            ▼                                                                │
│  3. EXHAUSTIVE CODING   ──► 100% complete production code (zero truncation) │
│            │                                                                │
│            ▼                                                                │
│  4. 4-DIMENSIONAL AUDIT ──► UI/UX + Routes/APIs + Backend + Security Scans  │
│            │                                                                │
│            ▼                                                                │
│  5. RECTIFY IN MEMORY   ──► Log defects/security findings on MEMORY_BOARD   │
│            │                                                                │
│      Errors/Flaws Found?                                                    │
│       YES ───────────────► Re-enter Stage 3 (Surgical Fix & Code)           │
│       NO  (100% Pass)   ──► Verification Gate Passed ──► COMPLETE           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### The 6-Stage Autonomous Loop Cycle:

1. **Stage 1: Plan & Memorize:**
   - Consult `MEMORY_BOARD.md` to load the current system state, registered features, routes, and past incident rectifications.
   - Absorb all cross-thread constraints so no established behavior is dropped.
2. **Stage 2: Atomic Task Checklist:**
   - Deconstruct user intent into sequential, ordered tasks (`Task 1`, `Task 2`, ...).
3. **Stage 3: Exhaustive Production Coding:**
   - Author 100% complete, fully articulated code. No placeholders, no `// TODO` stubs, no omissions.
4. **Stage 4: 4-Dimensional Full-Stack & Security Audit:**
   - Concurrently audit all 4 critical software dimensions (UI/UX, Routes/APIs, Backend/State, Security).
5. **Stage 5: Memory Board Task Rectification:**
   - Update `MEMORY_BOARD.md`: Log all newly identified bugs, edge cases, and security vulnerabilities under `Known Problems / Notes` and update their health states.
6. **Stage 6: The 100% Closed Loop Gate:**
   - If ANY test fails, lint errors arise, routes 404, dark/light themes collide, or security flaws are discovered:
     - **DO NOT STOP.** Re-enter Stage 3, apply surgical fixes, re-audit, and update the rectification log.
     - **Continue the loop until every layer achieves a 100% operational score.**

---

### The 4-Dimensional Full-Stack & Security Inspection Matrix

Every change must pass all 4 dimensions before completion:

#### 1. 🎨 UI / UX Experience & Interactive Logic
- **Interactive States:** Loading skeletons/spinners, disabled button states during async calls, error toast feedback, and empty data states.
- **Dual-Theme Contrast Parity:** Explicit styling for **both** Light Mode and Dark Mode. Verify text legibility, card backgrounds, and border colors in both modes.
- **Viewport & Touch Layout:** Safe areas (notch, dynamic island, status bar), Android keyboard resize behavior, mobile tap targets ($\ge 44 \times 44\text{px}$), and text expansion tolerance ($+30\%$ Indic/multilingual buffer).

#### 2. 🛣️ Routes, Navigation & Deep-Link Integrity
- **Route Table Verification:** All route paths (`/path`), deep links (`#view-*`, parameters), and modal triggers explicitly registered in the router table.
- **Navigation & Guard Logic:** Auth protection, unauthenticated redirects, history back-button behavior, and query string state preservation.
- **Broken Element Prohibition:** Zero dead links, zero unhandled `onclick` stubs, zero unmounted view templates.

#### 3. ⚙️ API Contracts, Backend & State Hygiene
- **Schema & Payload Contracts:** Parameter typing, request validation, response parsing, and explicit status code handling (`200 OK`, `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `500 Server Error`).
- **State Synchronization:** Optimistic updates vs server state reconciliation, cache invalidation, and race condition prevention.
- **Resource & Lifecycle Safety:** Unsubscribe event listeners, close SSE/WebSocket streams, stop camera tracks (`track.stop()`), clear timers/intervals, and provide graceful offline fallback (`localStorage`).

#### 4. 🛡️ Security Vulnerability & Hardening Defense
- **Zero Hardcoded Secrets:** No API keys, database passwords, private tokens, or JWT secrets exposed in client-side code, git tracking, or public bundles.
- **Injection & XSS Sanitization:** All user inputs escaped before DOM insertion or query execution (`textContent` over `innerHTML`, parameterized queries).
- **CORS, Auth & Storage Hardening:** Token storage validation (secure cookie / sandboxed storage), origin verification, permission/role boundary enforcement.
- **Safe Fallbacks:** Graceful degradation on network failure, preventing stack trace or sensitive error disclosure to client UI.

