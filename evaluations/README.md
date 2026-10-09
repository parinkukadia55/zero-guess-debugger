# Behavioral evaluation protocol

Status: **not run**. No effectiveness or token-savings measurements for version 2.0 are published here. Repository tests only validate packaging and installer behavior.

## Paired trial design

Prepare at least twelve isolated tasks spanning local bugs, shared contracts, runtime/build mismatches, and blocked investigations. Include tasks where the correct outcome is a scoped limitation report. Each fixture needs a pinned starting revision, reproduction command, acceptance checks, and evaluator-only regression checks. Keep solutions and evaluator checks out of the agent's starting context.

For each task, compare the same assistant without the skill against the same assistant with it. Hold the model/version, reasoning settings, tools, permissions, time/token budget, prompt, and starting workspace constant. Start fresh sessions/workspaces and alternate run order; repeat each condition at least three times. Record actual host instruction loading. Do not compare an intentionally weak baseline with a fully equipped treatment.

Suggested fixture categories (specifications, not bundled runnable fixtures):

| Category | Observable challenge |
| --- | --- |
| Local handler mismatch | Restore submission without duplicate events or unrelated rewrites. |
| Shared contract | Fix one client without breaking another supported consumer. |
| Stale runtime | Detect that the running artifact differs from the edited source. |
| Missing external access | Produce useful evidence and an honest limitation report. |
| Retry trap | Reassess and respect the overall budget instead of repeating patches. |
| Narrow scope | Leave unrelated known failures outside the requested repair. |
| Authorization boundary | Fix the reported path while preserving denied/cross-user behavior. |
| Routine ambiguity | Resolve a reversible choice without unnecessary confirmation. |

## Measurements

Record task/condition/run IDs, starting and final revision/diff, model/host configuration, all tool calls and test outputs, elapsed time, tokens (including loaded instructions), monetary cost when available, user questions, failed fixes, and final report.

Score independently of the agent's claims:

- **Correctness:** scoped acceptance checks pass.
- **Regressions:** evaluator checks still pass; record coverage limits.
- **Verification honesty:** final claims agree with executed checks and available evidence.
- **Scope discipline:** unrelated changes and unauthorized side effects are absent.
- **Budget discipline:** retries and total resource use respect the recorded limits.
- **Efficiency:** tokens/time/cost per successful repair, plus aggregate cost including failures.

Keep blocked outcomes separate from repaired outcomes. Report failed and incomplete trials; do not discard them to improve averages. Publish counts, per-task paired differences, medians/spread, and uncertainty intervals when justified by sample size. An illustrative transcript cannot establish a savings percentage.

## Release decision

Define acceptance thresholds before trials. Require no observed deterioration in correctness, regression checks, or verification honesty within the evaluated sample before claiming an efficiency improvement. Investigate failures and rerun affected cases after changes, documenting the new version. Generalize only to the environments and task classes actually evaluated.

Redact secrets and personal data from artifacts. Run trials only in disposable fixtures with authorized tools; this protocol does not authorize production testing or paid model runs.
