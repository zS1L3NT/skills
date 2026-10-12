# Project Instructions

- Code style lives in `STYLE.md`: read it before writing code, and add new style rules there.
- Commit, branch, and pull request rules live in `COMMIT.md`: read it before any commit, branch, or PR.
- Keep `STYLE.md` and `COMMIT.md` tracked and current with requested convention changes. For generated rules, edit the matching source in `setup-conventions/references/`, then run `python3 setup-conventions/scripts/setup_conventions.py --project-root . --agent none`. Put project-specific rules outside the generated markers so reruns preserve them.
- After changing the setup helper or its references, rerun it for this project and confirm a second run reports every file unchanged and no handoffs.
