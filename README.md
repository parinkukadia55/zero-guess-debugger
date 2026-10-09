# Zero-Guess Debugger

An evidence-driven debugging workflow for AI coding assistants. Version **2.0.0** · MIT license.

Investigate before editing, test explicit hypotheses, limit blind retries, and report what was actually verified.

This repository contains a skill, portable instruction files, and packaging helpers. It is not an executable debugger or a security certification system. Results depend on the assistant, available tools, task, and environment. No token savings or regression-free outcomes are guaranteed.

## The workflow

**Scope → Reproduce → Gather evidence → Test hypothesis → Fix → Verify → Report**

- Separate observed facts, hypotheses, experiments, and confirmed causes.
- Match verification to the affected behavior and risk.
- Reassess after two failed fixes for one hypothesis. By default, stop speculative edits at three hypotheses or five failed fixes overall; report the blocker and next useful experiment.
- Preserve the existing stack and unrelated work. Ask only when an unresolved choice materially affects the outcome.
- Record verified, failed, not tested, unknown, stale, and not applicable states honestly.

Start with [SKILL.md](SKILL.md). It retains the main principles, eleven-phase guidance, and worked examples inline, with a quick workflow first. Linked references add detail for build identity, UI/contracts, security, media, and persistent evidence when relevant.

## Installation

### Skill-capable assistants

Place this complete folder in a skill location supported by your assistant, or attach/invoke its `SKILL.md` using your assistant's documented workflow. Keep the linked `references/` and `examples/` directories with it. Discovery locations and supported formats vary by host; this repository does not certify compatibility with every product/version.

### Project instruction files

The installer requires Python 3.10 or later and uses only the standard library. Run it from this checkout. Choose the instruction filename your assistant actually loads:

| Format | Destination | Portable file |
| --- | --- | --- |
| `agents` | `AGENTS.md` | [AGENTS.md](rules/AGENTS.md) |
| `claude` | `CLAUDE.md` | [CLAUDE.md](rules/CLAUDE.md) |
| `gemini` | `GEMINI.md` | [GEMINI.md](rules/GEMINI.md) |
| `cursor` | `.cursorrules` | [.cursorrules](rules/.cursorrules) |
| `windsurf` | `.windsurfrules` | [.windsurfrules](rules/.windsurfrules) |

The filenames are distribution options, not a guarantee that a particular host/version discovers them. Confirm loading in the destination assistant. The portable rules contain the essential workflow without requiring this repository's references.

Preview a merge (no files are written):

```sh
python scripts/install.py --target "/path/to/project" --format agents
```

Apply the reviewed merge:

```sh
python scripts/install.py --target "/path/to/project" --format agents --apply
```

The installer appends or updates one marked section. It preserves bytes outside that section and saves an exact, uniquely named backup before changing an existing file. Repeating an unchanged install does nothing. Backups are kept beside the destination as `.zero-guess-backup-*`; they can contain private project instructions, so keep them out of commits and shared folders as appropriate.

Preview removal; add `--apply` to perform it:

```sh
python scripts/install.py --target "/path/to/project" --format agents --remove
```

Removal only removes the managed section and its two leading separator newlines. An otherwise empty destination is retained. To restore a backup, inspect it and the current file, then copy the chosen backup back; restoration can discard later edits.

UTF-8 files (including a UTF-8 BOM) and LF/CRLF managed sections are supported. Symbolic-link destinations and malformed/duplicate markers are rejected. Close other writers before applying; the installer detects changes during its preparation but is not a concurrent file editor.

### Upgrading from 1.x

Old versions instructed users to copy whole files. Such installations are not automatically identified or deleted: the installer preserves unmarked content, which may leave conflicting old rules in place. Review and remove only the obsolete Zero-Guess instructions after keeping a backup, then use the managed installation. Legacy Gemini markers also need manual review before installation.

## What changed in 2.0

The main principles and eleven phases remain in the skill, together with inline checklists, diagnostic cards, build checks, reporting examples, and the feature registry example. A quick workflow introduces the detailed guidance. Hypotheses and instrumentation are allowed; retry budgets are explicit. Verification is scoped, build identity replaces timestamp-only confidence, and memory records evidence rather than permanent health guarantees. Unsupported performance claims and mandatory line-count limits have been removed.

The README describes the product; [portable-rules.md](references/portable-rules.md) is the canonical text for the five generated rule files. Change that source and regenerate instead of independently editing each adapter.

## Validation and evaluation

```sh
python scripts/build_rules.py
python scripts/validate.py
python -m unittest discover -s tests -v
```

Repository validation checks local documentation targets, required distribution files, version consistency, and generated-rule drift. Tests exercise installation preservation, updates, removal, refusal cases, and validator failures. CI runs these checks on Windows and Linux. These are packaging checks, not proof that an assistant follows the workflow.

[Evaluation protocol](evaluations/README.md) defines paired debugging trials for correctness, regressions, cost, and verification honesty. **No behavioral benchmark has been run or published for version 2.0.** The diagnostic walkthrough is illustrative, not a measured result.

## Contributing

Keep changes tied to a demonstrated failure or useful decision rule. Run validation and tests, and include their results with the change. Behavioral claims need reproducible evaluation artifacts; additional mandatory phases need evidence that their benefit exceeds their cost.

Created by Parin Kukadia. See [LICENSE](LICENSE).
