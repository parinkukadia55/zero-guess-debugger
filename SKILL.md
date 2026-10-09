---
name: zero-guess-debugger
description: Investigate software defects using reproducible symptoms, explicit hypotheses, bounded experiments, and scoped verification. Use for debugging failures and regressions; broad audits and unrelated feature work do not require this workflow.
license: MIT
metadata:
  author: Parin Kukadia
  homepage: https://github.com/parinkukadia55/zero-guess-debugger
  version: "2.0.0"
---

# 🛡️ Zero-Guess Debugger & Autonomous Execution Engine

> **Stop AI coding assistants and autonomous agents from burning your quota with blind trial-and-error.**
>
> Combines **Cross-Thread Context Synthesis**, **Architectural Wireframe & Route Mapping**, **Goal Planning & Living Task Checklists**, **Multi-Language (i18n) Parity**, **Multi-Portal Interconnectivity (Web + User + Admin + Mobile Shell)**, **Native AI Generative Media**, **Zero-Guess Debugging**, **Stale-Build Verification Guards**, **Persistent Feature Memory Board (MEMORY_BOARD.md)**, **End-of-Run Broken Item Eyesight Triage**, **Autonomous Self-Healing Closed-Loop Audits**, **Notification & Tech Stack Fidelity**, **The Clarification Gate**, and **Lean Code Minimalism**.

Reduce blind retries by making the evidence behind each debugging decision explicit.
These instructions guide an assistant; they do not enforce execution or guarantee correctness.

## Scope and investigate

1. Establish the observed failure and the behavior that would count as fixed. Use accessible conversation context and relevant project instructions; do not claim access to other chats or missing history.
2. Inspect the failing path, actual symbols, and relevant callers before changing behavior. Preserve the user's stack and unrelated work. Use the project's existing check commands rather than assuming a language or framework.
3. Reproduce the symptom when feasible. If reproduction is unavailable, record that limitation and distinguish source inspection from runtime evidence.
4. Separate observation from hypothesis. Choose the smallest useful experiment, state its predicted result, and use the result to confirm or reject the hypothesis. Temporary instrumentation is legitimate; remove it when no longer needed.

For a simple defect, a short explanation is enough. For uncertain or repeated failures, use the [diagnostic example](examples/DIAGNOSTIC_CARD_EXAMPLE.md). Do not invent an exact root cause to fill a template.

## Fix and verify proportionally

- Prefer the smallest coherent fix. There is no line-count cap; correctness and maintainability take priority over brevity.
- A local fix needs focused verification. A shared-contract change also needs consumer and regression checks. Authentication, persistence, and other consequential changes need checks of relevant failure paths.
- Use existing tests where useful. Add a regression test when it captures the failure and provides lasting protection; do not add tests that only restate the implementation.
- Run relevant static, contract, and runtime checks when applicable and available. Record unavailable or inapplicable checks explicitly; passing one layer does not prove the others.
- Before interpreting a runtime result, establish which source/configuration and build are actually running. See [build identity](references/build-identity.md) when compiled, installed, cached, or remote artifacts are involved.
- Ask about unresolved choices that materially affect requirements, data, compatibility, or irreversible actions. Resolve routine reversible implementation choices from evidence and state meaningful assumptions.

## Bound retries and scope

- Do not repeat a failed change without new evidence. After two failed fixes for the same hypothesis, stop patching it and revisit the reproduction, assumptions, and data flow.
- Default investigation budget: three distinct hypotheses or five failed fix attempts in total, whichever comes first. Use a user-specified budget instead when provided. Count attempts across reassessments; renaming a hypothesis does not reset the budget.
- At the budget limit, stop speculative edits and report the evidence, remaining blocker, and next discriminating experiment. Resume dependent work when new evidence, access, or an explicitly revised budget makes progress possible.
- Missing access, an unavailable required environment, or an external failure is a reason to report a limitation, not to repeatedly rewrite working code. Continue independent authorized work when possible.
- Fix defects within the task's scope. Report unrelated findings separately; do not turn a focused change into an unlimited repair campaign.

## Supporting references

The main phase guidance and examples are included below so this skill remains useful on its own. These references provide additional detail when relevant:

- [UI, localization, and connected surfaces](references/ui-and-contracts.md): changed interfaces, translations, shared state, or mobile boundaries.
- [Security-sensitive changes](references/security.md): authentication, authorization, secrets, untrusted inputs, or persistent data changes.
- [Media selection](references/media.md): the task includes generating or modifying visual assets.
- [Evidence memory](examples/MEMORY_BOARD_TEMPLATE.md): ongoing investigations, handoffs, or a user-requested feature audit. Update an existing project record when suitable; a one-line fix does not require a new ledger.

## Finish with evidence

Report what changed, which checks ran and their outcomes, and remaining uncertainty. Use these states for each relevant claim:

| State | Meaning |
| --- | --- |
| Verified | Named checks passed for a stated scope and revision/environment. |
| Failed | A named check reproduced a defect or regression. |
| Not tested | A relevant check was not run; explain why. |
| Unknown | Evidence is insufficient to judge the behavior. |
| Stale | Evidence predates a relevant code, configuration, or environment change. |
| Not applicable | The check does not apply to the affected behavior. |

Claim the defect is fixed only when the scoped acceptance checks support that conclusion. Otherwise report it as blocked or partially verified, with the remaining limitation. Never equate inspected code, a saved memory entry, or a passing test suite with universal operational or security certainty.

---

## 🧵 Phase 0: Cross-Thread Context Synthesis (The Unified Chat Rule)

Combine available requirements, architectural decisions, and user preferences before planning. Preserve established requirements such as responsiveness, supported locales, themes, offline behavior, and role permissions when they affect the change. Use accessible conversation history and saved project records; identify missing context instead of claiming to have read inaccessible chats.

**Example:** A previous decision says the application supports English, Hindi, and Gujarati. A change to a shared validation message should account for those existing locales. It does not authorize adding translation infrastructure to a different, single-language project.

## 🧭 Phase 1: Goal Planning, Wireframe & Route Mapping

For work spanning several components, define the goal and acceptance criteria, map affected views and triggers, identify required contracts/files, and outline the data flow. A small local fix needs only the relevant subset.

```text
Available context + user request
  -> Concrete goal and acceptance criteria
  -> Affected routes, buttons, modals, handlers, and endpoints
  -> Required files, contracts, assets, and supported locales
  -> Implementation and verification checklist
  -> Scoped result and remaining gaps
```

**Example goal:** Restore the Admin Muhurat toggle so the saved setting appears in the User Home view under the product's intended synchronization behavior. Acceptance checks cover persistence, user-view refresh, and an unauthorized update attempt.

```markdown
### 📋 Task Checklist — illustrative multi-portal task
- [ ] Task 1: Inspect the settings schema, admin handler, and consumer contract.
- [ ] Task 2: Reproduce the missing update and test the leading hypothesis.
- [ ] Task 3: Correct the shared state/update path.
- [ ] Task 4: Update affected en, hi, and gu messages if labels changed.
- [ ] Task 5: Run applicable static, contract, and live checks.
- [ ] Task 6: Report verified behavior, failures, and untested surfaces.
```

## ⚡ Phase 2: Sequential Step-by-Step Execution & Live Progress Tracking

Execute dependent changes in order and keep the active task clear. Independent inspections may run together when supported. Report meaningful milestones and blockers; avoid repeating a full checklist after every minor action. A new failure triggers evidence gathering before further patches.

The following statuses are fictional examples, not results from the current repository:

```markdown
### 📋 Execution Progress
- [x] Task 1: Inspect TypeScript schemas and contracts — caller map recorded.
- [>] Task 2: Trace computation and shared state — hypothesis under test.
- [ ] Task 3: Check affected en, hi, and gu dictionaries.
- [ ] Task 4: Verify Admin Panel to Home Panel synchronization.
- [ ] Task 5: Verify the running build and execute relevant checks.
- [ ] Task 6: Produce the Eyesight report with evidence and gaps.
```

## 🎨 Phase 3: Media & Asset Generation (Native Generative Models)

When the task requests generated raster artwork, a banner, texture, or image transformation, use an available dedicated image capability with the actual supported parameters. Specify composition and aspect ratio where supported. Do not silently substitute crude scripted drawings for requested generative artwork.

**Example:** For a requested 16:9 product banner, provide an art-directed prompt and the supported size/aspect option. For an existing SVG icon, edit the vector asset; for an accurate data chart, use plotting tools. Video requires an available video capability. Do not invent a `generate_image` tool or assume an image tool produces video.

## 🌍 Phase 4: Multi-Language (i18n) Parity Shield

Apply to products that already support localization and to affected text/layouts.

| Check | What to establish |
| --- | --- |
| User-facing strings | Labels, placeholders, validation, and tooltips use the existing translation mechanism. |
| Supported locales | New or changed keys are accounted for in each supported dictionary. |
| Layout resilience | Representative long strings and scripts remain readable in affected views. |
| Connected artifacts | Relevant modals, PDFs, and shared views honor the established locale behavior. |

**Example:** If the Save button uses `t('settings.save')`, verify the corresponding key in `en`, `hi`, and `gu` when those locales are supported. Exercise translated text in the actual layout; a fixed 30% expansion allowance alone does not prove it fits. Reuse the project's locale storage contract rather than imposing an example key such as `jyotish_lang_chosen`.

## 🌐 Phase 5: Multi-Portal Ecosystem Interconnectivity

Trace the producer, transport/storage, and consumers for the changed behavior. Verify existing themes and platform boundaries where affected.

| Surface | Example responsibilities |
| --- | --- |
| Public Web Portal | Landing pages, guest forms, public results. |
| User / Home Portal | Dashboard, saved charts, history, personal state. |
| Admin Panel | Configuration, translation overrides, feature toggles. |
| Mobile Shell | Native bridges, permissions, device resources, offline cache. |

```text
Admin toggle -> validated API -> persisted setting/shared store
            -> consumer refresh/invalidation -> User Home / Web / Mobile
```

**Example:** An Admin Panel change saves correctly but the Home Panel remains stale. Inspect the consumer subscription or refresh path and intended consistency model before adding a timeout. Do not assume all products need immediate updates or all four surfaces.

## 🔒 Phase 6: The Zero-Guess Debugging Protocol

Keep the diagnostic card, caller audit, two-attempt reassessment, reverse check, and three verification layers. Distinguish a working hypothesis from a proven cause. The overall retry budget defined above also applies.

```text
Observed symptom + verified location
  -> Diagnostic card: evidence, hypothesis, predicted experiment
  -> Small discriminating experiment
  -> Confirm or reject the explanation
  -> Coherent fix and caller checks
  -> Static / contract / runtime verification as applicable
```

### 🔍 Pre-fix diagnostic card — illustrative example

```text
[SYMPTOM]    : Submit raises "app.submitKundliForm is not a function".
[LOCATION]   : Form binding in index.html and the app object declaration;
               record actual line numbers only after inspecting the file.
[EVIDENCE]   : The inspected form calls submitKundliForm(event), while the
               app object exposes computeKundli(). Runtime build identity
               still needs confirmation.
[HYPOTHESIS] : The form retained an old method name after a rename.
[EXPERIMENT] : Confirm the served build, reproduce, inspect the runtime
               object, and search both method names and their callers.
[PREDICTION] : The expected runtime lacks the old method; the replacement
               accepts the inputs needed by the form.
[FIX]        : Update the binding, or retain a compatibility adapter when
               the supported caller contract requires the old name.
[BLAST RADIUS]: Inspect other callers, submit prevention, input validation,
                and duplicate submission behavior.
```

If inspection establishes that preserving the old handler is necessary and the replacement takes no arguments, this adapter is one possible fix:

```javascript
submitKundliForm: function(event) {
  if (event) event.preventDefault();
  return this.computeKundli();
}
```

This is an example object method, not a universal patch. A caller search does not prove the absence of regressions.

After two failed fixes for the same hypothesis, reverse-check the chain: trace forward from the producer to the consumer and backward from the failure to its inputs. Record cumulative attempts; changing hypothesis names does not reset the overall budget.

| Verification layer | Example evidence |
| --- | --- |
| Static | The project's configured syntax/type/lint check; `tsc --noEmit` only where appropriate. |
| Contract / integration | Caller compatibility, request/response shape, affected locale keys, state propagation. |
| Runtime | Reproduced interaction on the identified browser/device/build, with observed results. |

### ⏱️ Stale-Build Guard & Build Identity Verification

Keep timestamps as an initial clue, then establish the actual running artifact:

```text
Identify source + dirty changes + relevant configuration
  -> Identify built artifact and test target
  -> Does the running artifact correspond to the intended inputs?
       YES: run scoped checks and record the identity evidence.
       NO:  rebuild/sync/install through the existing authorized workflow.
       UNKNOWN: investigate identity or report runtime verification blocked.
```

**Example:** Compare the APK's `LastWriteTime` with changed sources to detect an obvious mismatch, but also verify which package/build is installed on the device. A newer APK sitting on disk does not establish that the device is running it. Commands such as `npm run build`, `npx cap sync`, and `./gradlew assembleDebug` are examples only; inspect the project's actual pipeline and authorization first.

## 👁️ Phase 7: End-of-Run Broken Item Eyesight Report

Give the user visibility into the inspected scope, actual results, and remaining gaps. Use verified line references only when available. The following is a fictional reporting example, not an audit of this repository:

```markdown
### 👁️ Broken Buttons, Routes & Endpoints Eyesight Report
- Scope: Admin Muhurat setting and its Home Panel consumer.
- Verified: Authorized update persisted; Home view reflected the saved value
  in the tested local build. Attach the actual test/build evidence.
- Failed: /settings/profile navigation returned 404 during the scoped check.
  Record its inspected route/caller location and reproduction.
- Not tested: Android device flow; no device was available.
- Unknown: Gujarati PDF rendering; outside the executed checks.
- Next step: Resolve the route failure if within scope; otherwise report it
  separately. Test the device path when access becomes available.
```

Other findings may include an undefined `app.missingHandler()`, an unmounted `POST /api/save-kundli`, or a disconnected Admin toggle. Establish each with evidence before listing it as broken. An endpoint without a UI trigger may intentionally serve another client or background job.

## 🧠 Phase 8: Persistent Feature Memory Board & Rectification Ledger

For sustained work, handoffs, or requested full-repository audits, maintain an existing project record or `MEMORY_BOARD.md`. Preserve the feature registry and fix history, but treat the board as an evidence index that can become stale.

```text
Read relevant memory -> inspect requested scope -> reconcile code and record
  -> note findings, evidence, and gaps -> persist updated investigation state
```

### Feature registry example (fictional)

| ID | Feature / surface | Route / logic | State | Evidence / environment | Problem / next step |
| --- | --- | --- | --- | --- | --- |
| FEAT-001 | Lagna Kundli Calculator / Web | /kundli; engine/chart.ts::computeLagna | Verified for tested inputs | Named calculation tests at a recorded revision | Other inputs remain outside those checks. |
| FEAT-002 | Admin Muhurat Manager / Admin + Home | /admin/muhurat; api/admin.ts::toggleMuhurat | Failed | Recorded reproduction: save succeeds, Home stays stale | Trace the consumer refresh path. |
| FEAT-003 | PDF Dossier Export / User | /export/pdf; services/pdf.ts::buildPdf | Not tested | Gujarati font rendering has not been exercised | Generate and inspect an authorized test PDF. |

During a requested full-repo scan, reconcile routes, handlers, services, and known consumers; identify missing or disconnected features without assuming every endpoint needs a UI. Track stable feature IDs where useful. Record the actual revision, dirty changes, environment, timestamp, check results, and rectification history. Mark affected evidence stale after relevant changes; default to unknown where evidence is missing. Never copy the example rows as actual project findings.

Before creating a potentially duplicate feature, consult the relevant record and confirm against code. Small fixes do not require initializing a full feature board.

## 🔄 Phase 9: Autonomous Self-Healing Closed-Loop & Full-Stack Security Audit

Preserve the plan, code, inspect, rectify, and verify cycle within the user's task and the overall investigation budget. Complete the intended implementation without placeholder behavior, then execute the applicable acceptance checks.

```text
Plan and consult relevant memory -> ordered tasks -> implement
  -> inspect affected dimensions -> record evidence
  -> defect remains within scope and budget? Reassess and correct.
  -> scoped acceptance checks pass? Report verified completion.
  -> budget/access blocks verification? Report limitation and next experiment.
```

### Four-dimensional inspection matrix

| Dimension | Checks when affected |
| --- | --- |
| UI / UX | Loading/disabled/error/empty states; existing themes; keyboard access; supported viewport and translated text behavior. |
| Routes / navigation | Registered affected routes, deep links, query preservation, auth redirects, and handler wiring. |
| API / backend | Payload validation, meaningful status/error handling, persistence, optimistic state reconciliation, resource disposal. |
| Security | Relevant server-side authorization and denied cases, secret handling, context-appropriate encoding, parameterized queries, and recovery. |

**Example:** A camera-view fix may require stopping camera tracks on exit and checking denied permissions. It does not by itself require scanning every unrelated backend endpoint. A security check passing is evidence about that check, not a certification that the system is universally secure.

## 🎯 Phase 10: Notification & Tech Stack Fidelity, Clarification & Lean Code

### Notification and tech stack fidelity

Honor the user's established libraries and mechanisms, including Capacitor LocalNotifications, FCM, Web Notifications, or a custom notification service when present. Inspect actual signatures, permissions, and channel configuration; do not swap libraries merely because another is familiar.

**Example:** If the project already uses Capacitor LocalNotifications, implement its requested reminder through that existing integration. Verify applicable permissions such as `POST_NOTIFICATIONS` against the actual target/API configuration instead of blindly adding manifest entries.

### The clarification gate

Ask when missing information materially changes behavior or commits the user to a consequential choice. Check accessible requirements first and continue independent authorized work while an answer is pending.

- **Notification schedule:** A request for daily reminders lacks a time/timezone and there is no established default. Clarify the schedule before scheduling notifications.
- **Competing implementations:** Two installed libraries serve different platforms. Inspect their current usage; ask only if the intended target remains unresolved.
- **Architectural fork:** A choice changes a public contract or persistence model. Make the consequence concrete before seeking a decision.
- **Destructive change:** Establish authorization before deleting routes/data or applying an irreversible migration.

Routine reversible implementation details can be resolved from evidence without a confirmation round.

### Lean code minimalism

> **When Need Less Coding in Creation or Rectification, Use Less Coding — Don't Write Too Much Code.**

Prefer direct, idiomatic solutions and avoid gratuitous wrappers, factories, and repeated boilerplate. A ten-line correction may be ideal for a local defect, but a larger change is justified when the contract, tests, or maintainability require it. Do not omit necessary behavior or leave an unfinished implementation merely to fit an arbitrary line limit.
