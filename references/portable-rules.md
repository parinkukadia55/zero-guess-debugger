# Zero-Guess Debugger

Apply this workflow to defects and regressions. Scale it to the task; unrelated feature work does not require a debugging ceremony. These are instructions, not automated enforcement or a guarantee of correctness.

1. Define the observed failure and scoped acceptance criteria. Use accessible context and project instructions; do not claim access to missing chat history.
2. Inspect actual symbols, contracts, and relevant callers. Preserve the user's stack and unrelated changes. Reproduce when feasible and record when reproduction is unavailable.
3. Separate observations, hypotheses, and confirmed causes. Choose a small experiment with a predicted result; use its outcome to guide the fix. Temporary instrumentation is valid and should be removed when no longer needed.
4. Make the smallest coherent correction, without an arbitrary line-count cap. Use project-native checks. Local fixes need focused checks; shared contracts need consumer/regression checks; consequential changes need relevant failure-path checks.
5. Before interpreting runtime results, establish which source/configuration and artifact are actually running. A recent timestamp alone is insufficient. Use build/deployment identity when available; report missing runtime access rather than repeatedly rewriting code.
6. Do not repeat a failed patch without new evidence. Reassess after two failed fixes for one hypothesis. Default overall budget: three distinct hypotheses or five failed fixes, whichever comes first, unless the user specifies another budget. Counts do not reset during reassessment. At the limit, stop speculative edits, report the blocker and next useful experiment, and resume dependent work only with new evidence/access or a revised budget. Continue independent authorized work where possible.
7. Ask when an unresolved choice materially affects requirements, data, compatibility, or irreversible actions. Resolve routine reversible choices from evidence and state meaningful assumptions. Stay within authorized scope; report unrelated defects separately.
8. Check UI states, supported themes/locales, connected surfaces, or native boundaries only when affected. Do not add new platform requirements. Inspect actual API/tool capabilities rather than inventing tool names or assuming a framework.
9. For affected security boundaries, check authorization, relevant denied cases, safe data handling, and recovery as appropriate. Do not leak secrets into logs or notes. A scan or passing test does not certify universal security.
10. For sustained work, update the project's evidence record with scope, check results, revision/environment, date, and gaps. Treat outdated entries as stale; do not require a new memory file for a small change.
11. Finish with what changed, actual checks and outcomes, and remaining uncertainty. Use verified, failed, not tested, unknown, stale, or not applicable states. Never present inspected code or an unexecuted plan as runtime verification.
