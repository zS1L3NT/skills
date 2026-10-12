#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
from pathlib import Path

SCRIPT = Path(__file__).resolve()
SKILL = SCRIPT.parents[1]
REFS = SKILL / "references"
AGENT_CLIS = ("claude", "codex")

LANGUAGES = {
    "react-typescript": "react-typescript.md",
    "php-laravel": "php-laravel.md",
    "swift-swiftui": "swift-swiftui.md",
    "rust": "rust.md",
}

SKIP_DIRS = {".git", ".next", ".turbo", ".venv", "build", "dist", "node_modules", "public", "target", "vendor"}

START = "<!-- setup-conventions:generated-start -->"
END = "<!-- setup-conventions:generated-end -->"
# Also matches markers written under the skill's old setup-style-guide name.
MANAGED = re.compile(
    r"<!-- setup-(?:conventions|style-guide):generated-start -->.*?<!-- setup-(?:conventions|style-guide):generated-end -->",
    flags=re.DOTALL,
)

STYLE_INTRO = "Code style only. Project commands, setup, verification, domain notes, and agent conduct live in AGENTS.md; commit, branch, and pull request rules live in COMMIT.md."
COMMIT_INTRO = "Rules for every commit, branch, and pull request an AI agent makes in this repository."


def main() -> int:
    parser = argparse.ArgumentParser(description="Create or refresh the STYLE.md and COMMIT.md guides.")
    parser.add_argument("--project-root", default=".", help="Project to modify. Defaults to cwd.")
    parser.add_argument("--languages", default="auto", help=f"Comma-separated style refs, or auto. Options: {','.join(LANGUAGES)}.")
    parser.add_argument("--force", action="store_true", help="Replace existing guides that have no generated markers.")
    parser.add_argument("--dry-run", action="store_true", help="Report planned changes without writing files.")
    parser.add_argument("--agent", default="auto", choices=["auto", *AGENT_CLIS, "none"], help="Agent CLI to hand unresolved situations to. Agents running this skill pass none.")
    args = parser.parse_args()

    root = Path(args.project_root).expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"Project root is not a directory: {root}")

    languages = parse_languages(args.languages, root)
    current = {name: read(root / name) for name in ("STYLE.md", "COMMIT.md", ".gitignore")}
    planned = {
        "STYLE.md": merge(current["STYLE.md"], build("Style Guide", STYLE_INTRO, ["base-style.md", *(LANGUAGES[l] for l in languages)]), args.force),
        "COMMIT.md": merge(current["COMMIT.md"], build("Commit Guide", COMMIT_INTRO, ["commit.md"]), args.force),
        ".gitignore": without_gitignore(current[".gitignore"]),
    }

    status = {}
    for name, text in planned.items():
        status[name] = "unchanged" if text == current[name] else "needs-agent" if text is None else "created" if current[name] is None else "updated"
        if not args.dry_run and text not in (None, current[name]):
            (root / name).write_text(text)

    handoffs = find_handoffs(root, planned)
    print(json.dumps({"project_root": str(root), "languages": languages, "dry_run": args.dry_run, "files": status, "handoffs": handoffs}, indent=2))
    if not handoffs or args.dry_run or args.agent == "none":
        return 0
    return run_agent(args.agent, root, handoffs)


def parse_languages(value: str, root: Path) -> list[str]:
    if value == "auto":
        return detect_languages(root)

    languages = [item.strip() for item in value.split(",") if item.strip()]
    unknown = [item for item in languages if item not in LANGUAGES]
    if unknown:
        raise SystemExit(f"Unknown language refs: {', '.join(unknown)}")
    return languages


def detect_languages(root: Path) -> list[str]:
    suffixes = set()
    for _, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        suffixes.update(Path(f).suffix for f in files)

    package = read(root / "package.json") or ""
    composer = read(root / "composer.json") or ""
    detected = {
        "react-typescript": '"react"' in package or ".tsx" in suffixes,
        "php-laravel": "laravel/framework" in composer or (root / "artisan").exists(),
        "swift-swiftui": (root / "Package.swift").exists() or ".swift" in suffixes,
        "rust": (root / "Cargo.toml").exists() or ".rs" in suffixes,
    }
    return [name for name, hit in detected.items() if hit]


def build(title: str, intro: str, refs: list[str]) -> str:
    body = "\n\n".join(demote_headings((REFS / ref).read_text().strip()) for ref in refs)
    return f"# {title}\n\n{intro}\n\n{START}\n\n{body}\n\n{END}\n"


def merge(current: str | None, generated: str, force: bool) -> str | None:
    if current is None:
        return generated
    if MANAGED.search(current):
        block = MANAGED.search(generated).group(0)
        return MANAGED.sub(lambda _: block, current, count=1)
    return generated if force else None


def find_handoffs(root: Path, planned: dict[str, str | None]) -> list[str]:
    handoffs = [
        f"{name} exists without generated markers. Restructure it as: `# Title`, intro line, an empty `{START}` / `{END}` block for the helper to fill, then the existing rules the references do not already cover."
        for name in ("STYLE.md", "COMMIT.md")
        if planned[name] is None
    ]

    agents = read(root / "AGENTS.md")
    if agents is not None and not ("STYLE.md" in agents and "COMMIT.md" in agents):
        # A STYLE.md pointer without a COMMIT.md one is what the older setup-style-guide skill left behind.
        legacy = " It was set up by the older setup-style-guide skill, so expect a STYLE.md-only pointer and git rules that now belong in COMMIT.md." if "STYLE.md" in agents else ""
        handoffs.append(f"AGENTS.md needs migrating: move style and git rules into the guides and add the pointer from SKILL.md.{legacy}")
    return handoffs


def run_agent(choice: str, root: Path, handoffs: list[str]) -> int:
    situations = "\n".join(f"- {h}" for h in handoffs)
    prompt = f"""Use the setup-conventions skill at {SKILL} (read its SKILL.md) in {root}. Its helper script wrote what it could and left these situations:

{situations}

Resolve each one following SKILL.md, then rerun `python3 {SCRIPT} --project-root {root} --agent none` and confirm it reports no handoffs."""

    cli = next((c for c in AGENT_CLIS if shutil.which(c)), None) if choice == "auto" else choice
    if cli is None or shutil.which(cli) is None:
        raise SystemExit(f"No agent CLI found ({', '.join(AGENT_CLIS)}). Resolve these by hand:\n{situations}")
    return subprocess.run([cli, prompt], cwd=root).returncode


def without_gitignore(current: str | None) -> str | None:
    # Older versions gitignored the guides; worktrees need them tracked.
    if current is None:
        return None
    ignored = {f"{prefix}{name}" for name in ("STYLE.md", "COMMIT.md") for prefix in ("", "/")}
    return "".join(line for line in current.splitlines(keepends=True) if line.strip() not in ignored)


def demote_headings(markdown: str) -> str:
    return "\n".join("#" + line if line.startswith("#") else line for line in markdown.splitlines())


def read(path: Path) -> str | None:
    return path.read_text() if path.exists() else None


if __name__ == "__main__":
    raise SystemExit(main())
