#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path

REFS = Path(__file__).resolve().parents[1] / "references"

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
    parser = argparse.ArgumentParser(description="Create or refresh the private STYLE.md and COMMIT.md guides.")
    parser.add_argument("--project-root", default=".", help="Project to modify. Defaults to cwd.")
    parser.add_argument("--languages", default="auto", help=f"Comma-separated style refs, or auto. Options: {','.join(LANGUAGES)}.")
    parser.add_argument("--force", action="store_true", help="Replace existing guides that have no generated markers.")
    parser.add_argument("--dry-run", action="store_true", help="Report planned changes without writing files.")
    args = parser.parse_args()

    root = Path(args.project_root).expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"Project root is not a directory: {root}")

    languages = parse_languages(args.languages, root)
    current = {name: read(root / name) for name in ("STYLE.md", "COMMIT.md", ".gitignore")}
    planned = {
        "STYLE.md": merge(root / "STYLE.md", current["STYLE.md"], build("Style Guide", STYLE_INTRO, ["base-style.md", *(LANGUAGES[l] for l in languages)]), args.force),
        "COMMIT.md": merge(root / "COMMIT.md", current["COMMIT.md"], build("Commit Guide", COMMIT_INTRO, ["commit.md"]), args.force),
        ".gitignore": with_gitignore(current[".gitignore"]),
    }

    status = {}
    for name, text in planned.items():
        status[name] = "created" if current[name] is None else "unchanged" if text == current[name] else "updated"
        if not args.dry_run and text != current[name]:
            (root / name).write_text(text)

    print(json.dumps({"project_root": str(root), "languages": languages, "dry_run": args.dry_run, "files": status}, indent=2))
    return 0


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


def merge(path: Path, current: str | None, generated: str, force: bool) -> str:
    if current is None:
        return generated
    if MANAGED.search(current):
        block = MANAGED.search(generated).group(0)
        return MANAGED.sub(lambda _: block, current, count=1)
    if force:
        return generated
    raise SystemExit(f"{path} exists without setup-conventions markers. Rerun with --force to replace it.")


def with_gitignore(current: str | None) -> str | None:
    text = current or ""
    lines = {line.strip() for line in text.splitlines()}
    missing = [f"/{name}" for name in ("STYLE.md", "COMMIT.md") if f"/{name}" not in lines and name not in lines]
    if not missing:
        return current

    if text and not text.endswith("\n"):
        text += "\n"
    return text + "".join(f"{entry}\n" for entry in missing)


def demote_headings(markdown: str) -> str:
    return "\n".join("#" + line if line.startswith("#") else line for line in markdown.splitlines())


def read(path: Path) -> str | None:
    return path.read_text() if path.exists() else None


if __name__ == "__main__":
    raise SystemExit(main())
