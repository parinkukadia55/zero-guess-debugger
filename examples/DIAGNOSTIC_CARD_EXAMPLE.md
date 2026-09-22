# 📖 Real-World Walkthrough: The Diagnostic Card in Action

This walkthrough demonstrates how the **Zero-Guess Debugger** protocol solves a runtime bug in **1 turn** instead of burning 12 turns in a trial-and-error loop.

---

## 🚫 The Default AI Trap (Without Zero-Guess)

### Turn 1:
> **User:** "Clicking 'Submit Birth Details' does nothing on Android!"  
> **Untrained Agent:** "Let me add console.log statements to `App.tsx` and re-run the build." *(Burns tokens, edits wrong file)*

### Turn 3:
> **Untrained Agent:** "The logs didn't show up. Maybe Capacitor bridge is broken? Let me reinstall `@capacitor/core` and retry." *(Burns 15,000 tokens, changes dependencies)*

### Turn 7:
> **Untrained Agent:** "Still not working. Let me wrap the button click in a 500ms `setTimeout` and add `try/catch`." *(Masks symptom, still broken)*

**Total damage:** 8 turns wasted, 140,000 tokens consumed, dependency versions mangled, bug still present.

---

## ✅ The Zero-Guess Protocol (With Zero-Guess Debugger)

### Step 1: Zero-Hallucination & File Discovery
The agent refuses to guess. It asks:
1. *What is the exact symptom?* Button click produces no action.
2. *Where is the entry point?* Grep for the button text or form in the repository.

```bash
# Grep finds:
index.html:4343: <form onsubmit="app.submitKundliForm(event)">
```

### Step 2: Code Inspection & Root Cause Confirmation
The agent reads lines 4330–4350 in `index.html`. Then inspects `const app` at line 12500.
It discovers:
- The form calls `app.submitKundliForm(event)`.
- But inside `const app`, the method is named `computeKundli()`.
- `submitKundliForm` does NOT exist on `app`, throwing an unhandled `TypeError: app.submitKundliForm is not a function`.

### Step 3: Mandatory Pre-Fix Diagnostic Card
Before touching any code, the agent outputs the Diagnostic Card:

```markdown
### 🔍 Diagnostic Card
- [SYMPTOM]     : Clicking "Submit" produces no response; console shows "TypeError: app.submitKundliForm is not a function".
- [LOCATION]    : `index.html`, line 4343 (HTML event binding) and line 12540 (app object declaration).
- [ROOT CAUSE]  : A previous refactoring renamed the calculation method to `computeKundli()`, but the form onsubmit attribute still calls `submitKundliForm()`.
- [SURGICAL FIX]: Add a 3-line delegation shim to `const app`:
  ```javascript
  submitKundliForm: function(event) {
    if (event) event.preventDefault();
    this.computeKundli();
  }
  ```
- [BLAST RADIUS]: Grepped for `submitKundliForm` across repo. Found only 1 call site at line 4343. Zero collateral regressions.
```

### Step 4: Surgical Fix
The agent applies the 4-line change directly into `index.html`.

### Step 5: Verification Gate
- **Gate 1 (Static):** Syntax check passed.
- **Gate 2 (Contract):** `this.computeKundli` confirmed to exist.
- **Gate 3 (Live):** Live click submitted the form and rendered the chart successfully.

**Total outcome:** **1 turn**, **1,800 tokens**, bug permanently resolved, zero side-effects.
