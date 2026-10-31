"""Exercise audit exit codes against isolated harness fixtures."""

import subprocess
import tempfile
import unittest
from pathlib import Path


AUDIT = Path(__file__).resolve().parents[1] / "governance-audit.sh"


class GovernanceAuditTests(unittest.TestCase):
    def setUp(self):
        self.fixture = tempfile.TemporaryDirectory()
        self.addCleanup(self.fixture.cleanup)
        self.root = Path(self.fixture.name)
        self.write("scripts/governance-audit.sh", AUDIT.read_text())
        self.write("AGENTS.md", "Use $example.\n")
        self.write(".agents/skills/example/SKILL.md", "# Example\n")
        self.write("docs/adr/README.md", "# ADRs\n")
        (self.root / "intent").mkdir()
        self.status("done")

    def write(self, path, content):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)

    def status(self, value):
        self.write(".ai/context/project-status.md", f"bootstrap: {value}\n")

    def audit(self, *args, expected=0):
        result = subprocess.run(
            ["bash", str(self.root / "scripts/governance-audit.sh"), *args],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return result

    def test_done_canonical_status_passes(self):
        self.audit()

    def test_done_section_ignores_possible_status_values(self):
        self.write(
            ".ai/context/project-status.md",
            "# Status\n\n## bootstrap\n\n`done`\n\n"
            "Valores possíveis: `pending` | `in_progress` | `done`\n",
        )
        self.audit()

    def test_pending_requires_explicit_template_mode(self):
        self.status("pending")
        self.audit(expected=1)
        self.audit("--template")

    def test_pending_section_passes_only_in_template_mode(self):
        self.write(".ai/context/project-status.md", "## bootstrap\n\n`pending`\n")
        self.audit(expected=1)
        self.audit("--template")

    def test_done_also_passes_in_template_mode(self):
        self.audit("--template")

    def test_invalid_states_fail_in_both_modes(self):
        for state in ("in_progress", "unknown", "", "done trailing text"):
            self.status(state)
            for args in ((), ("--template",)):
                with self.subTest(state=state, args=args):
                    self.audit(*args, expected=1)

    def test_missing_status_fails_in_both_modes(self):
        (self.root / ".ai/context/project-status.md").unlink()
        for args in ((), ("--template",)):
            with self.subTest(args=args):
                self.audit(*args, expected=1)

    def test_only_enum_is_not_a_status(self):
        self.write(".ai/context/project-status.md", "Valores: `pending` | `done`\n")
        self.audit(expected=1)
        self.audit("--template", expected=1)

    def test_conflicting_or_repeated_declarations_fail(self):
        for content in (
            "bootstrap: done\nbootstrap: pending\n",
            "bootstrap: done\nbootstrap: done\n",
            "bootstrap: done\n## bootstrap\n`done`\n",
            "## bootstrap\n`pending`\n## bootstrap\n`pending`\n",
            "bootstrap: done\nbootstrap: \n",
            "bootstrap: \nbootstrap: done\n",
        ):
            self.write(".ai/context/project-status.md", content)
            for args in ((), ("--template",)):
                with self.subTest(content=content, args=args):
                    self.audit(*args, expected=1)

    def test_malformed_section_values_fail(self):
        for value in ("`done", "done`", "`done` extra"):
            self.write(".ai/context/project-status.md", f"## bootstrap\n{value}\n")
            for args in ((), ("--template",)):
                with self.subTest(value=value, args=args):
                    self.audit(*args, expected=1)

    def test_unknown_or_extra_arguments_fail(self):
        self.audit("--unknown", expected=2)
        self.audit("--template", "extra", expected=2)

    def test_help_succeeds_without_running_audit(self):
        self.status("pending")
        result = self.audit("--help")
        self.assertIn("--template", result.stdout)

    def test_template_mode_still_rejects_unlisted_skill(self):
        self.status("pending")
        self.write(".agents/skills/unlisted/SKILL.md", "# Unlisted\n")
        result = self.audit("--template", expected=1)
        self.assertIn("unlisted", result.stdout)

    def test_template_mode_still_rejects_duplicate_adrs(self):
        self.status("pending")
        self.write("docs/adr/ADR-0001-one.md", "# One\n")
        self.write("docs/adr/ADR-0001-two.md", "# Two\n")
        self.write("docs/adr/README.md", "| ADR-0001 | One |\n")
        self.audit("--template", expected=1)

    def test_template_mode_still_requires_adr_index(self):
        self.status("pending")
        self.write("docs/adr/ADR-0001-one.md", "# One\n")
        self.audit("--template", expected=1)

    def test_template_mode_still_rejects_wrong_intent_suffix(self):
        self.status("pending")
        self.write("intent/example_security_review.md", "# Review\n")
        self.audit("--template", expected=1)

    def test_indexed_unique_adr_passes(self):
        self.write("docs/adr/ADR-0001-one.md", "# One\n")
        self.write("docs/adr/README.md", "| ADR-0001 | One |\n")
        self.audit()

    def test_fixture_does_not_change_source_status(self):
        source_status = AUDIT.parent.parent / ".ai/context/project-status.md"
        original = source_status.read_bytes()
        self.status("pending")
        self.audit(expected=1)
        self.assertEqual(source_status.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
