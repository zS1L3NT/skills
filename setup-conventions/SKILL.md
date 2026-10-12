---
name: setup-conventions
description: Set up STYLE.md and COMMIT.md guides in a project and migrate matching rules out of AGENTS.md.
disable-model-invocation: true
---

# Setup Conventions

Gives a project two git-tracked guides, each generated from this skill's references:

- `STYLE.md`: code style only, from [base-style.md](references/base-style.md) plus the detected language references.
- `COMMIT.md`: commit, branch, and pull request rules, from [commit.md](references/commit.md).

## Workflow

1. Read the target project's `AGENTS.md` and any existing `STYLE.md` and `COMMIT.md`.
2. Run the helper, resolving its path from this skill's directory. Add `--dry-run` to preview:

   ```sh
   python3 <skill-dir>/scripts/setup_conventions.py --project-root <project> --agent none
   ```

   It detects languages (override with `--languages`), writes both guides, and removes any `.gitignore` entries for them left by older versions, since worktrees only carry tracked files. Generated content sits between `setup-conventions` markers and is refreshed on every rerun; content outside the markers is preserved. Situations it cannot resolve, such as a guide without markers or an `AGENTS.md` still awaiting migration (including legacy `setup-style-guide` projects), come back as `handoffs`: resolve each one in the steps below. Run by hand from a terminal without `--agent none`, the helper opens `claude` or `codex` with those handoffs instead.
3. Migrate `AGENTS.md` by hand, rule by rule, since sorting rules needs judgement:
   - Code-style rules move to `STYLE.md`; commit, branch, and pull request rules move to `COMMIT.md`.
   - Move a rule only when the guide lacks it or the rule is sharper, and place it after the closing marker so reruns keep it.
   - Everything else stays in `AGENTS.md`: project shape, commands, generated-file workflows, domain notes, verification, agent behavior.
4. Add this pointer to `AGENTS.md`, and nothing about which file wins a conflict:

   ```md
   - Code style lives in `STYLE.md`: read it before writing code, and add new style rules there.
   - Commit, branch, and pull request rules live in `COMMIT.md`: read it before any commit, branch, or PR.
   ```

Done when the helper reports no `handoffs`, every rule from the original `AGENTS.md` is either kept there or present in one of the guides, and the diff shows nothing else changed.
