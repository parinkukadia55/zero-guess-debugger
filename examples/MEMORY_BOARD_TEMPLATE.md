# 🧠 Project Feature Memory Board & Rectification Ledger

> **Single Source of Truth for Codebase Features, Routes, Status & Rectifications**  
> *Project:* [Project Name]  
> *Last Scanned / Synced:* [YYYY-MM-DD HH:MM:SS]  
> *Health Summary:* Total Features: 0 | Operational: 0 | Degraded: 0 | Broken: 0 | In Rectification: 0  

---

## 🗺️ Feature Registry Matrix

| ID | Feature Name | Domain / Portal | Route / View File | Backing Logic / Endpoints | Health Status | Known Problems / Notes | Rectification History |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `FEAT-001` | [Feature Name] | [Web / User / Admin / Mobile] | `[/route]`, `[Component.tsx:line]` | `[service.ts::function]` | `🟢 Operational` | None | Initial scan |

---

## 🛠️ Rectification Log & Incident Ledger

### `FEAT-001`: [Feature Name]
- **[Incident Date]:** YYYY-MM-DD
- **[Problem Observed]:** Description of defect or missing link.
- **[Root Cause]:** Exact mechanical failure mechanism.
- **[Rectification Applied]:** Summary of fix, modified files, and verification steps.
- **[Resolution Status]:** `🟢 Resolved` / `🟡 Monitoring` / `🔴 Unresolved`

---

## 🔍 Full-Repo Scan & Anti-Misplacement Protocol
Whenever requested to scan the repository:
1. Load this `MEMORY_BOARD.md` to restore baseline awareness of all known features.
2. Traverse all route tables, pages, components, handlers, and endpoints.
3. Compare live codebase against this matrix:
   - Mark new features with next sequential `FEAT-XXX` ID.
   - Flag misplaced or missing features previously marked as operational.
   - Verify health and document open problems.
4. Save and commit updated `MEMORY_BOARD.md` to prevent context amnesia across future sessions.
