# Investigation evidence board

Use an existing project record when possible. Create a board for sustained investigations, handoffs, or requested audits; do not require one for every edit.

Project:
Scope and acceptance criteria:
Last updated (include timezone):

| Behavior / contract | Source or owner | State | Evidence / check result | Revision + dirty changes / environment | Checked at | Gap / next step |
| --- | --- | --- | --- | --- | --- | --- |

States: **verified**, **failed**, **not tested**, **unknown**, **stale**, **not applicable**.

- Every verified claim needs a check and bounded scope. Default to unknown when evidence is missing.
- Mark affected entries stale when relevant source, configuration, dependencies, or runtime changes. Recheck before relying on them.
- A source inspection and an end-to-end test establish different things; label each explicitly.
- Keep code, tests, and runtime observations authoritative. This board indexes evidence and can be wrong or outdated.
- Record durable decisions and unresolved gaps; link existing issues or test artifacts instead of copying large logs. Do not store credentials or sensitive user data.

## Active investigation

Observed failure:
Hypotheses tested and results:
Failed fix attempts (cumulative):
Budget and stopping condition:
Changes made / recovery notes:
Remaining blocker / next experiment:

## Handoff

Available context and missing access:
Checks passed, failed, or not run:
Unrelated findings (outside current scope):
