---
name: zero-guess-debugger
description: >-
  Stop AI coding agents from burning your quota with blind trial-and-error. Enforces cross-thread
  context synthesis, goal definition, prerequisite analysis, living task checklists, sequential
  step-by-step execution with live completion updates, multi-language (i18n) parity, multi-portal
  interconnectivity (Web + User Home + Admin Panel + Mobile/Native), native AI image/video generation
  models (no Python PIL/matplotlib scripts for visuals), zero-hallucination, mandatory pre-fix
  diagnostic cards, 2-attempt circuit breakers, bidirectional reverse-checking, and strict 3-tier
  verification gates.
license: MIT
metadata:
  author: Parin Kukadia
  homepage: https://github.com/parinkukadia55/zero-guess-debugger
  version: "1.4.0"
---

# 🛡️ Zero-Guess Debugger & Autonomous Execution Engine

> **Stop AI coding assistants and autonomous agents from burning your quota with blind trial-and-error.**  
> Combines **Cross-Thread Context Synthesis**, **Goal Planning & Living Task Checklists**, **Multi-Language (i18n) Parity**, **Multi-Portal Interconnectivity (Web + User + Admin + Mobile Shell)**, **Native AI Generative Media Mandates**, and an **Anti-Trial-and-Error Zero-Guess Debugging Protocol**.

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
  - Visual assets: Use generative AI image models (`generate_image`), never script-based fallbacks.
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
                      └────────────────────────────────────────┘
```

### The 8 Core Safeguards

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
6. **Strict 3-Tier Verification Gate:** Gate 1 (Static: `tsc --noEmit`) $\rightarrow$ Gate 2 (Contract, i18n & Interconnect checks) $\rightarrow$ Gate 3 (Live device/browser testing).
7. **Platform Boundary Awareness:** Storage sandboxing (`localStorage` fallbacks), camera stream teardown (`track.stop()`), and native overrides for Android/Capacitor.
8. **Patch Minimalism:** Surgical fixes (under 20–30 lines). No symptom-masking with empty catches or arbitrary timeouts.
