"""Validate distribution files and local Markdown link targets, without network access."""

import re
from urllib.parse import unquote, urlsplit

from build_rules import ROOT, check_rules, version

REQUIRED = (
    "README.md", "SKILL.md", "LICENSE", "references/portable-rules.md",
    "references/build-identity.md", "references/ui-and-contracts.md",
    "references/security.md", "references/media.md",
    "examples/DIAGNOSTIC_CARD_EXAMPLE.md", "examples/MEMORY_BOARD_TEMPLATE.md",
    "evaluations/README.md", "scripts/build_rules.py", "scripts/install.py",
    "scripts/validate.py", "tests/test_install.py", "tests/test_validate.py",
    ".github/workflows/validate.yml",
)


def local_link_errors(path, root):
    errors = []
    text = path.read_text(encoding="utf-8")
    # Current docs use simple inline links. Ignore code fences and URL/anchor targets.
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    for match in re.finditer(r"\[[^\]\n]+\]\(([^)\n]+)\)", text):
        href = match.group(1).strip().strip("<>")
        url = urlsplit(href)
        if url.scheme or url.netloc or not url.path:
            continue
        target = (path.parent / unquote(url.path)).resolve()
        if not target.is_relative_to(root.resolve()):
            errors.append(f"Link escapes package: {path.relative_to(root)} -> {href}")
        elif not target.exists():
            errors.append(f"Missing link target: {path.relative_to(root)} -> {href}")
    return errors


def validate(root=ROOT):
    errors = [f"Missing required file: {name}" for name in REQUIRED if not (root / name).is_file()]
    try:
        errors.extend(check_rules(root))
        readme = (root / "README.md").read_text(encoding="utf-8")
        if f"Version **{version(root)}**" not in readme:
            errors.append("README version differs from SKILL.md")
    except (OSError, ValueError) as error:
        errors.append(str(error))
    docs = [root / "README.md", root / "SKILL.md"]
    for folder in ("references", "examples", "evaluations", "rules"):
        docs.extend((root / folder).glob("*.md"))
    for path in docs:
        if path.is_file():
            errors.extend(local_link_errors(path, root))
    return errors


if __name__ == "__main__":
    failures = validate()
    print("\n".join(failures) if failures else "Repository validation passed.")
    raise SystemExit(bool(failures))
