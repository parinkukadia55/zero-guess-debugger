"""Preview or merge a managed rule section without replacing project guidance."""

import argparse
import difflib
import os
from pathlib import Path
import stat
import tempfile
import uuid

from build_rules import FORMATS, render

BEGIN = b"<!-- BEGIN ZERO-GUESS DEBUGGER MANAGED -->"
END = b"<!-- END ZERO-GUESS DEBUGGER MANAGED -->"
START = b"\n\n" + BEGIN + b"\n"
FINISH = END + b"\n"
LEGACY = b"<!-- BEGIN ZERO-GUESS DEBUGGER RULES -->"


def merge(original, rules, remove=False):
    """Round-trip unmanaged UTF-8 bytes, including BOM and original newlines."""
    original.decode("utf-8-sig")  # Reject unsupported encodings before any writes.
    if b"\x00" in original:
        raise ValueError("NUL bytes found; convert the instruction file to UTF-8 first")
    if LEGACY in original:
        raise ValueError("Legacy rules found; review and migrate them manually first")
    counts = (original.count(BEGIN), original.count(END))
    if counts not in ((0, 0), (1, 1)):
        raise ValueError("Duplicate or incomplete managed markers; refusing to edit")
    block = b"" if remove else START + rules.encode("utf-8") + FINISH
    if counts == (0, 0):
        return original + block
    # Editors/Git may convert the managed block to CRLF after installation.
    for newline in (b"\n", b"\r\n"):
        opening = newline * 2 + BEGIN + newline
        closing = END + newline
        start = original.find(opening)
        end = original.find(closing)
        if start >= 0 and end >= start + len(opening) and original[end - 1:end] == b"\n":
            return original[:start] + block + original[end + len(closing):]
    raise ValueError("Malformed managed section; refusing to edit")


def install(target, format_name, apply=False, remove=False):
    target = Path(target).expanduser().resolve(strict=True)
    if not target.is_dir():
        raise ValueError("Target must be an existing project directory")
    destination = target / FORMATS[format_name]
    if destination.is_symlink():
        raise ValueError("Symbolic-link destinations are not supported")
    exists = destination.exists()
    if exists and not destination.is_file():
        raise ValueError("Destination is not a regular file")
    original = destination.read_bytes() if exists else b""
    updated = merge(original, render(), remove)
    if updated == original:
        print(f"No changes: {destination}")
        return None
    if not apply:
        print(f"Preview only: {destination}")
        print("".join(difflib.unified_diff(
            original.decode("utf-8-sig").splitlines(keepends=True),
            updated.decode("utf-8-sig").splitlines(keepends=True),
            fromfile=str(destination), tofile=str(destination) + " (proposed)",
        )))
        return None
    # Detect intervening edits before backup and again before replacement.
    def unchanged():
        return (
            not destination.is_symlink()
            and destination.exists() == exists
            and (not exists or destination.read_bytes() == original)
        )

    if not unchanged():
        raise ValueError("Destination changed during preparation; retry after review")
    backup = None
    if exists:
        backup = target / f".zero-guess-backup-{destination.name}-{uuid.uuid4().hex}"
        with os.fdopen(os.open(backup, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600), "wb") as stream:
            stream.write(original)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=target, prefix=".zero-guess-", delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(updated)
            stream.flush()
            os.fsync(stream.fileno())
        if exists:
            temporary.chmod(stat.S_IMODE(destination.stat().st_mode))
        if not unchanged():
            raise ValueError("Destination changed during preparation; backup retained")
        os.replace(temporary, destination)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()
    print(f"Updated: {destination}")
    if backup:
        print(f"Backup: {backup}")
    return backup


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--format", required=True, choices=FORMATS)
    parser.add_argument("--apply", action="store_true", help="Write changes (default: preview)")
    parser.add_argument("--remove", action="store_true", help="Remove only the managed section")
    args = parser.parse_args()
    try:
        install(args.target, args.format, args.apply, args.remove)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Error: {error}\n")


if __name__ == "__main__":
    main()
