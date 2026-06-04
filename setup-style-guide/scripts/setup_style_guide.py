#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

LANGUAGE_REFS = {
    "react-typescript": "react-typescript.md",
    "php-laravel": "php-laravel.md",
    "swift-swiftui": "swift-swiftui.md",
    "rust": "rust.md",
}

SKIP_DIRS = {
    ".git",
    ".next",
    ".turbo",
    ".venv",
    "build",
    "dist",
    "node_modules",
    "public",
    "target",
    "vendor",
}

GENERATED_START = "<!-- setup-style-guide:generated-start -->"
GENERATED_END = "<!-- setup-style-guide:generated-end -->"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create or update a private STYLE.md from bundled style references."
    )
    parser.add_argument("--project-root", default=".", help="Project root to modify. Defaults to cwd.")
    parser.add_argument(
        "--languages",
        default="auto",
        help="Comma-separated language refs to include, or auto. Options: react-typescript,php-laravel,swift-swiftui,rust.",
    )
    parser.add_argument("--force", action="store_true", help="Replace an existing unmarked STYLE.md.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned changes without writing files.")
    parser.add_argument("--no-gitignore", action="store_true", help="Do not add /STYLE.md to .gitignore.")
    args = parser.parse_args()

    root = Path(args.project_root).expanduser().resolve()
    if not root.exists():
        print(f"Project root does not exist: {root}", file=sys.stderr)
        return 2

    skill_root = Path(__file__).resolve().parents[1]
    refs = skill_root / "references"

    languages = parse_languages(args.languages, root)
    style_path = root / "STYLE.md"
    next_style = merge_style(style_path, build_style(refs, languages), args.force)

    next_gitignore = None
    gitignore_path = root / ".gitignore"
    if not args.no_gitignore:
        next_gitignore = with_style_gitignore(gitignore_path.read_text() if gitignore_path.exists() else "")

    summary = {
        "project_root": str(root),
        "languages": languages,
        "style_path": str(style_path),
        "style_updated": True,
        "gitignore_updated": bool(next_gitignore is not None),
        "agents_updated": False,
        "next_step": "AI must compare AGENTS.md to STYLE.md and manually migrate missing code-style rules.",
    }

    if args.dry_run:
        print(json.dumps(summary, indent=2))
        return 0

    style_path.write_text(next_style)
    if next_gitignore is not None:
        gitignore_path.write_text(next_gitignore)

    print(json.dumps(summary, indent=2))
    return 0


def parse_languages(value: str, root: Path) -> list[str]:
    if value != "auto":
        languages = [item.strip() for item in value.split(",") if item.strip()]
        unknown = [item for item in languages if item not in LANGUAGE_REFS]
        if unknown:
            raise SystemExit(f"Unknown language refs: {', '.join(unknown)}")
        return languages

    languages: list[str] = []

    package_json = root / "package.json"
    package_text = package_json.read_text(errors="ignore") if package_json.exists() else ""
    if "react" in package_text or has_file(root, {".tsx"}):
        languages.append("react-typescript")

    composer_json = root / "composer.json"
    composer_text = composer_json.read_text(errors="ignore") if composer_json.exists() else ""
    if "laravel/framework" in composer_text or (root / "artisan").exists():
        languages.append("php-laravel")

    if (root / "Package.swift").exists() or has_file(root, {".swift"}):
        languages.append("swift-swiftui")

    if (root / "Cargo.toml").exists() or has_file(root, {".rs"}):
        languages.append("rust")

    return languages


def has_file(root: Path, suffixes: set[str]) -> bool:
    for _, dirnames, filenames in os.walk(root):
        dirnames[:] = [name for name in dirnames if name not in SKIP_DIRS]
        if any(Path(filename).suffix in suffixes for filename in filenames):
            return True
    return False


def build_style(refs: Path, languages: list[str]) -> str:
    chunks = [
        "# Style Guide",
        "",
        "This file is code style only. It intentionally excludes project commands, setup steps, generated-file workflows, verification procedures, domain glossaries, git behavior, and general agent conduct.",
        "",
        GENERATED_START,
        "",
        demote_headings((refs / "base-style.md").read_text()),
    ]

    for language in languages:
        chunks.extend(["", demote_headings((refs / LANGUAGE_REFS[language]).read_text())])

    chunks.extend(["", GENERATED_END, ""])
    return "\n".join(chunks)


def merge_style(path: Path, generated: str, force: bool) -> str:
    if not path.exists():
        return generated

    current = path.read_text()
    if GENERATED_START in current and GENERATED_END in current:
        pattern = re.compile(
            re.escape(GENERATED_START) + r".*?" + re.escape(GENERATED_END),
            flags=re.DOTALL,
        )
        generated_body = generated.split(GENERATED_START, 1)[1].rsplit(GENERATED_END, 1)[0]
        return pattern.sub(f"{GENERATED_START}{generated_body}{GENERATED_END}", current)

    if force:
        return generated

    raise SystemExit(
        f"{path} already exists and is not managed by setup-style-guide. Rerun with --force to replace it."
    )


def with_style_gitignore(current: str) -> str | None:
    lines = current.splitlines()
    if any(line.strip() in {"/STYLE.md", "STYLE.md"} for line in lines):
        return None

    if current and not current.endswith("\n"):
        current += "\n"
    return current + "/STYLE.md\n"


def demote_headings(markdown: str) -> str:
    return "\n".join("#" + line if line.startswith("#") else line for line in markdown.splitlines())


if __name__ == "__main__":
    raise SystemExit(main())
