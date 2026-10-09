from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from build_rules import ROOT
from validate import validate


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "package"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__", ".zero-guess-backup-*"))

    def test_current_distribution_passes(self):
        self.assertEqual(validate(self.root), [])

    def test_missing_advertised_adapter_fails(self):
        (self.root / "rules/.windsurfrules").unlink()
        self.assertTrue(any("Missing rule file" in error for error in validate(self.root)))

    def test_adapter_drift_fails(self):
        (self.root / "rules/CLAUDE.md").write_text("outdated", encoding="utf-8")
        self.assertTrue(any("Rule drift" in error for error in validate(self.root)))

    def test_broken_local_link_fails(self):
        with (self.root / "README.md").open("a", encoding="utf-8") as stream:
            stream.write("\n[Missing reference](references/missing.md)\n")
        self.assertTrue(any("Missing link target" in error for error in validate(self.root)))

    def test_missing_reference_and_escaping_link_fail(self):
        (self.root / "references/security.md").unlink()
        with (self.root / "README.md").open("a", encoding="utf-8") as stream:
            stream.write("\n[Outside](../outside.md)\n")
        errors = validate(self.root)
        self.assertTrue(any("Missing required file" in error for error in errors))
        self.assertTrue(any("Link escapes package" in error for error in errors))

    def test_version_mismatch_fails(self):
        path = self.root / "README.md"
        path.write_text(path.read_text(encoding="utf-8").replace("Version **2.0.0**", "Version **1.9.0**"), encoding="utf-8")
        self.assertIn("README version differs from SKILL.md", validate(self.root))


if __name__ == "__main__":
    unittest.main()
