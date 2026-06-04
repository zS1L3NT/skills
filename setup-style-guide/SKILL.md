---
name: setup-style-guide
description: Creates a private STYLE.md code-style guide from bundled style references and guides the AI-based migration of code-style rules out of AGENTS.md. Use when setting up STYLE.md, separating code style from agent/project instructions, or migrating away from perfect-code-style.
---

# Setup Style Guide

## Quick Start

Resolve the helper path relative to this skill directory, then run it against the target project:

```sh
python3 scripts/setup_style_guide.py --project-root ../my-project
```

If you are already in the target project, run the same helper with `--project-root .` after resolving the helper path from the skill directory. Then review the diff. `STYLE.md` should contain only code style, `.gitignore` should contain `/STYLE.md`, and `AGENTS.md` should point to `STYLE.md` while keeping project shape, commands, generated-file workflows, domain notes, verification, and agent behavior.

## Workflow

1. Read the current `AGENTS.md` and any existing `STYLE.md`.
2. Run the helper script. It detects project languages, writes the base style guide plus matching language references, and adds `/STYLE.md` to `.gitignore`.
3. Compare `AGENTS.md` against `STYLE.md` yourself. Move only code-style rules from `AGENTS.md` into `STYLE.md` when they are missing or sharper than the generic guide.
4. Edit `AGENTS.md` yourself: remove migrated style rules, keep non-style project instructions, and add a short pointer to `STYLE.md`.
5. The `AGENTS.md` pointer should say to read `STYLE.md` for code style and to put future code-style changes in `STYLE.md`, not `AGENTS.md`.

## Boundaries

- `STYLE.md` is code style only: declaration order, density, naming, prop/argument order, comments, local consistency, language/framework conventions, and cleanup preferences.
- `STYLE.md` must not contain commands, setup steps, run scripts, generated-file regeneration instructions, verification workflows, domain glossaries, git behavior, or general agent conduct.
- `AGENTS.md` remains for non-style project instructions and should include a short pointer to `STYLE.md`.
- Do not copy setup-only conflict-resolution wording such as "if `AGENTS.md` and `STYLE.md` differ, prioritize `STYLE.md`" into `AGENTS.md`.
- The helper adds only a narrow root-level `/STYLE.md` gitignore entry.
- Do not use a script to classify or rewrite `AGENTS.md`; that migration requires AI judgment.

## References

The helper copies [base-style.md](references/base-style.md) into every `STYLE.md`, then includes only detected language references:

- [react-typescript.md](references/react-typescript.md)
- [php-laravel.md](references/php-laravel.md)
- [swift-swiftui.md](references/swift-swiftui.md)
- [rust.md](references/rust.md)
