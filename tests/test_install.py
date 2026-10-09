import contextlib
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from build_rules import FORMATS
from install import BEGIN, END, FINISH, LEGACY, START, install, merge


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.output = contextlib.redirect_stdout(io.StringIO())
        self.output.__enter__()
        self.addCleanup(self.output.__exit__, None, None, None)

    def test_round_trip_preserves_existing_bytes_and_new_edits(self):
        for original in (b"", b"custom rules", b"custom\r\n", b"\xef\xbb\xbfGujarati: \xe0\xaa\x97\n"):
            with self.subTest(original=original):
                merged = merge(original, "first version\n")
                suffix = b"\r\nLater project instructions\r\n"
                updated = merge(merged + suffix, "second version\n")
                self.assertTrue(updated.startswith(original))
                self.assertNotIn(b"first version", updated)
                self.assertEqual(merge(updated, "", remove=True), original + suffix)

    def test_preview_writes_nothing(self):
        destination = self.root / "AGENTS.md"
        destination.write_bytes(b"Keep these rules")
        install(self.root, "agents")
        self.assertEqual(destination.read_bytes(), b"Keep these rules")
        self.assertEqual(list(self.root.iterdir()), [destination])

    def test_preview_new_target_does_not_create_file(self):
        install(self.root, "agents")
        self.assertEqual(list(self.root.iterdir()), [])

    def test_apply_backup_idempotence_and_removal(self):
        for format_name, filename in FORMATS.items():
            with self.subTest(format_name=format_name):
                destination = self.root / filename
                original = b"# Existing rules\r\nDo not remove."
                destination.write_bytes(original)
                backup = install(self.root, format_name, apply=True)
                self.assertEqual(backup.read_bytes(), original)
                installed = destination.read_bytes()
                count = len(list(self.root.iterdir()))
                self.assertIsNone(install(self.root, format_name, apply=True))
                self.assertEqual(len(list(self.root.iterdir())), count)
                removal_backup = install(self.root, format_name, apply=True, remove=True)
                self.assertEqual(removal_backup.read_bytes(), installed)
                self.assertEqual(destination.read_bytes(), original)

    def test_update_replaces_only_managed_content(self):
        destination = self.root / "AGENTS.md"
        original = b"Before\r\n" + START + b"old content\n" + FINISH + b"After"
        destination.write_bytes(original)
        backup = install(self.root, "agents", apply=True)
        self.assertEqual(backup.read_bytes(), original)
        self.assertEqual(merge(destination.read_bytes(), "", remove=True), b"Before\r\nAfter")

    def test_windows_newline_conversion_still_allows_update_and_removal(self):
        installed = merge(b"Project notes\n", "old rules\n").replace(b"\n", b"\r\n")
        updated = merge(installed, "new rules\n")
        self.assertNotIn(b"old rules", updated)
        self.assertEqual(merge(updated, "", remove=True), b"Project notes\r\n")

    def test_intervening_edit_is_not_overwritten(self):
        destination = self.root / "AGENTS.md"
        destination.write_bytes(b"original")

        def intervening_edit():
            destination.write_bytes(b"concurrent user edit")
            return "new rules\n"

        with patch("install.render", side_effect=intervening_edit):
            with self.assertRaisesRegex(ValueError, "changed during preparation"):
                install(self.root, "agents", apply=True)
        self.assertEqual(destination.read_bytes(), b"concurrent user edit")
        self.assertEqual(list(self.root.iterdir()), [destination])

    def test_symlink_guard_without_platform_privileges(self):
        with patch("install.Path.is_symlink", return_value=True):
            with self.assertRaisesRegex(ValueError, "Symbolic-link"):
                install(self.root, "agents", apply=True)
        self.assertEqual(list(self.root.iterdir()), [])

    def test_new_install_and_empty_removal(self):
        install(self.root, "agents", apply=True)
        self.assertIn(BEGIN, (self.root / "AGENTS.md").read_bytes())
        install(self.root, "agents", apply=True, remove=True)
        self.assertEqual((self.root / "AGENTS.md").read_bytes(), b"")

    def test_malformed_markers_fail_without_writes(self):
        bad_inputs = (
            BEGIN, END, START + b"x\n", START + FINISH + START + FINISH,
            FINISH + START, BEGIN + b"\n" + FINISH, LEGACY,
            b"\xff\xfea\x00", b"a\x00b",
        )
        destination = self.root / "AGENTS.md"
        for original in bad_inputs:
            with self.subTest(original=original):
                destination.write_bytes(original)
                with self.assertRaises(ValueError):
                    install(self.root, "agents", apply=True)
                self.assertEqual(destination.read_bytes(), original)
                self.assertEqual(list(self.root.iterdir()), [destination])

    def test_missing_target_is_not_created(self):
        with self.assertRaises(OSError):
            install(self.root / "missing", "agents", apply=True)
        self.assertEqual(list(self.root.iterdir()), [])

    def test_symlink_destination_is_rejected(self):
        original = self.root / "original.md"
        original.write_bytes(b"preserve")
        try:
            (self.root / "AGENTS.md").symlink_to(original)
        except OSError:
            self.skipTest("Creating symbolic links is not permitted on this host")
        with self.assertRaises(ValueError):
            install(self.root, "agents", apply=True)
        self.assertEqual(original.read_bytes(), b"preserve")

    def test_replacement_failure_keeps_original_and_backup(self):
        destination = self.root / "AGENTS.md"
        destination.write_bytes(b"preserve")
        with patch("install.os.replace", side_effect=OSError("simulated failure")):
            with self.assertRaises(OSError):
                install(self.root, "agents", apply=True)
        self.assertEqual(destination.read_bytes(), b"preserve")
        backups = list(self.root.glob(".zero-guess-backup-*"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_bytes(), b"preserve")
        self.assertEqual(len(list(self.root.iterdir())), 2)

    def test_cli_defaults_to_preview(self):
        script = Path(__file__).resolve().parents[1] / "scripts/install.py"
        result = subprocess.run(
            [sys.executable, str(script), "--target", str(self.root), "--format", "windsurf"],
            capture_output=True, text=True, encoding="utf-8",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Preview only", result.stdout)
        self.assertEqual(list(self.root.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
