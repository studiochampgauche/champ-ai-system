"""Installer regressions, isolated from the installed kit and the network.

Run with Python 3.11+: python -B -m unittest discover -s .codex/tests -v
"""
import contextlib
import importlib.util
import io
import os
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


PROJECT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("kit_setup", PROJECT / ".codex/scripts/setup.py")
setup = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(setup)
NEW_SHA = "1234567890abcdef1234567890abcdef12345678"
OLD_MANIFEST = "# Existing provenance\nCommit: `old-commit`\n"


def remove_link(path):
    if os.name == "nt" and getattr(path.lstat(), "st_reparse_tag", 0) == stat.IO_REPARSE_TAG_MOUNT_POINT:
        path.rmdir()
    else:
        path.unlink()


def directory_link(source, target):
    try:
        target.symlink_to(source, target_is_directory=True)
    except OSError:
        if os.name != "nt":
            raise
        subprocess.run(
            ["cmd", "/c", "mklink", "/J", str(target), str(source)],
            check=True, capture_output=True,
        )


class RootTests(unittest.TestCase):
    def test_root_is_the_project_containing_the_script(self):
        self.assertEqual(setup.ROOT, PROJECT)


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="champ-setup-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.skills = self.root / ".agents/skills"
        self.skills.mkdir(parents=True)
        (self.root / ".codex/scripts").mkdir(parents=True)
        shutil.copy2(PROJECT / ".codex/scripts/setup.py", self.root / ".codex/scripts/setup.py")
        (self.root / ".codex/docs").mkdir()
        shutil.copy2(PROJECT / ".codex/docs/SETUP.md", self.root / ".codex/docs/SETUP.md")
        shutil.copy2(PROJECT / "AGENTS.md", self.root / "AGENTS.md")
        for name in setup.AGENTS:
            shutil.copy2(PROJECT / f".agents/{name}.md", self.root / f".agents/{name}.md")
        for source in (PROJECT / ".agents/skills").iterdir():
            if source.is_dir() and not source.name.startswith("gsap-"):
                shutil.copytree(source, self.skills / source.name)
        patches = mock.patch.multiple(
            setup, ROOT=self.root, AGENT_ROOT=self.root / ".agents", SKILLS_ROOT=self.skills,
        )
        patches.start()
        self.addCleanup(patches.stop)
        self.output = io.StringIO()
        stdout = contextlib.redirect_stdout(self.output)
        stderr = contextlib.redirect_stderr(self.output)
        stdout.__enter__()
        stderr.__enter__()
        self.addCleanup(stdout.__exit__, None, None, None)
        self.addCleanup(stderr.__exit__, None, None, None)
        setup.sync_agents()
        setup.link_claude()

    def install_existing_gsap(self):
        for name in setup.GSAP:
            self.write_skill(self.skills / name, name, "old content")
        license_path = self.root / ".agents/licenses/gsap-skills-LICENSE"
        license_path.parent.mkdir(parents=True)
        license_path.write_text("old license\n", encoding="utf-8")
        (self.root / ".codex/docs/GSAP_UPSTREAM.md").write_text(OLD_MANIFEST, encoding="utf-8")

    @staticmethod
    def write_skill(folder, name, content):
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: Test skill for installer regression.\n---\n\n{content}\n",
            encoding="utf-8",
        )

    @contextlib.contextmanager
    def upstream(self, invalid_skill=False, missing_license=False, empty_license=False, readonly_object=False):
        """Only the transport is simulated; actual staging/copies/renames run."""
        def clone(command, **kwargs):
            self.assertEqual(command[:2], ["git", "clone"])
            repository = Path(command[-1])
            for name in setup.GSAP:
                self.write_skill(repository / "skills" / name, name, "new content")
            if invalid_skill:
                (repository / "skills" / setup.GSAP[0] / "SKILL.md").write_text("invalid", encoding="utf-8")
            if not missing_license:
                (repository / "LICENSE").write_text(" \n" if empty_license else "new license\n", encoding="utf-8")
            if readonly_object:
                readonly = repository / "readonly-object"
                readonly.write_text("simulated read-only Git object", encoding="utf-8")
                readonly.chmod(stat.S_IREAD)
            return subprocess.CompletedProcess(command, 0)

        with mock.patch.object(setup.shutil, "which", return_value="git"), \
                mock.patch.object(setup.subprocess, "run", side_effect=clone), \
                mock.patch.object(setup.subprocess, "check_output", return_value=NEW_SHA + "\n"):
            yield

    def installed_snapshot(self):
        paths = [self.skills / name / "SKILL.md" for name in setup.GSAP]
        paths += [self.root / ".agents/licenses/gsap-skills-LICENSE", self.root / ".codex/docs/GSAP_UPSTREAM.md"]
        return {str(p.relative_to(self.root)): p.read_bytes() if p.exists() else None for p in paths}

    def test_complete_offline_kit_validates(self):
        setup.validate()

    def test_empty_kit_fails_validation_and_mutation_preflight(self):
        empty = self.root / "empty"
        empty.mkdir()
        with mock.patch.multiple(setup, ROOT=empty, AGENT_ROOT=empty / ".agents", SKILLS_ROOT=empty / ".agents/skills"):
            with mock.patch.object(setup.subprocess, "run") as run:
                for action in (setup.validate, setup.sync_agents, setup.link_claude, lambda: setup.install_gsap(False)):
                    with self.subTest(action=action), self.assertRaises(RuntimeError):
                        action()
                run.assert_not_called()
        self.assertEqual(list(empty.iterdir()), [])

    def test_missing_canonical_role_fails(self):
        (self.root / ".agents/ENGINEER.md").unlink()
        with self.assertRaises(RuntimeError):
            setup.validate()

    def test_missing_internal_skill_fails(self):
        (self.skills / "react/SKILL.md").unlink()
        with self.assertRaises(RuntimeError):
            setup.validate()

    def test_additional_directory_requires_skill_manifest(self):
        (self.skills / "custom-skill").mkdir()
        with self.assertRaises(RuntimeError):
            setup.validate()

    def test_malformed_skill_metadata_fails(self):
        path = self.skills / "react/SKILL.md"
        original = path.read_bytes()
        for bad in ("no metadata", "---\nname: wrong-name\ndescription: wrong\n---\n", "---\nname: react\n---\n"):
            with self.subTest(content=bad):
                path.write_text(bad, encoding="utf-8")
                with self.assertRaises(RuntimeError):
                    setup.validate()
        path.write_bytes(original)

    def test_partial_gsap_installation_fails(self):
        self.write_skill(self.skills / setup.GSAP[0], setup.GSAP[0], "partial")
        setup.link_claude()
        with self.assertRaises(RuntimeError):
            setup.validate()

    def test_all_three_native_formats_require_each_agent(self):
        for runtime, extension in ((".codex", "toml"), (".claude", "md"), (".gemini", "md")):
            path = self.root / runtime / "agents" / f"engineer.{extension}"
            original = path.read_bytes()
            with self.subTest(runtime=runtime):
                path.unlink()
                with self.assertRaises(RuntimeError):
                    setup.validate()
                path.write_bytes(original)

    def test_all_three_native_formats_detect_stale_content(self):
        for runtime, extension in ((".codex", "toml"), (".claude", "md"), (".gemini", "md")):
            path = self.root / runtime / "agents" / f"engineer.{extension}"
            original = path.read_text(encoding="utf-8")
            with self.subTest(runtime=runtime):
                path.write_text(original.replace("Full-Stack", "Stale"), encoding="utf-8")
                with self.assertRaises(RuntimeError):
                    setup.validate()
                path.write_text(original, encoding="utf-8")

    def test_canonical_change_requires_regeneration(self):
        path = self.root / ".agents/ENGINEER.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nNew requirement.\n", encoding="utf-8")
        with self.assertRaises(RuntimeError):
            setup.validate()
        setup.sync_agents()
        setup.validate()

    def test_missing_claude_link_fails(self):
        remove_link(self.root / ".claude/skills/react")
        with self.assertRaises(RuntimeError):
            setup.validate()

    def test_wrong_claude_link_fails_and_is_preserved(self):
        link = self.root / ".claude/skills/react"
        remove_link(link)
        wrong = self.skills / "php"
        directory_link(wrong, link)
        with self.assertRaises(RuntimeError):
            setup.validate()
        with self.assertRaises(RuntimeError):
            setup.link_claude()
        self.assertEqual(link.resolve(), wrong)

    def test_real_claude_directory_conflict_is_preserved(self):
        link = self.root / ".claude/skills/react"
        remove_link(link)
        link.mkdir()
        marker = link / "my-work.txt"
        marker.write_text("keep", encoding="utf-8")
        with self.assertRaises(RuntimeError):
            setup.link_claude()
        with self.assertRaises(RuntimeError):
            setup.validate()
        self.assertEqual(marker.read_text(encoding="utf-8"), "keep")

    def test_existing_gsap_is_preserved_without_network(self):
        self.install_existing_gsap()
        before = self.installed_snapshot()
        with mock.patch.object(setup.subprocess, "run") as run:
            setup.install_gsap(False)
            run.assert_not_called()
        self.assertEqual(self.installed_snapshot(), before)

    def test_partial_gsap_requires_explicit_update_without_mutation(self):
        self.write_skill(self.skills / setup.GSAP[0], setup.GSAP[0], "old")
        before = self.installed_snapshot()
        with mock.patch.object(setup.subprocess, "run") as run:
            with self.assertRaises(RuntimeError):
                setup.install_gsap(False)
            run.assert_not_called()
        self.assertEqual(self.installed_snapshot(), before)

    def test_gsap_preparation_failure_keeps_every_old_file(self):
        self.install_existing_gsap()
        before = self.installed_snapshot()
        real_copy = setup.shutil.copytree
        count = 0

        def fail_copy(source, destination, *args, **kwargs):
            nonlocal count
            count += 1
            if count == 3:
                raise OSError("simulated disk failure during preparation")
            return real_copy(source, destination, *args, **kwargs)

        with self.upstream(), mock.patch.object(setup.shutil, "copytree", side_effect=fail_copy):
            with self.assertRaises((OSError, RuntimeError)):
                setup.install_gsap(True)
        self.assertEqual(self.installed_snapshot(), before)

    def test_gsap_replacement_failure_restores_previous_installation(self):
        self.install_existing_gsap()
        before = self.installed_snapshot()
        real_rename = Path.rename
        failed = False

        def fail_replacement(source, target):
            nonlocal failed
            if Path(target) == self.skills / setup.GSAP[2] and not failed:
                failed = True
                raise OSError("simulated replacement failure")
            return real_rename(source, target)

        with self.upstream(), mock.patch.object(Path, "rename", new=fail_replacement):
            with self.assertRaises((OSError, RuntimeError)):
                setup.install_gsap(True)
        self.assertTrue(failed, "Test must exercise an actual replacement failure")
        self.assertEqual(self.installed_snapshot(), before)

    def test_gsap_update_commits_skills_license_and_matching_provenance(self):
        self.install_existing_gsap()
        with self.upstream():
            setup.install_gsap(True)
        for name in setup.GSAP:
            self.assertIn("new content", (self.skills / name / "SKILL.md").read_text(encoding="utf-8"))
        self.assertEqual((self.root / ".agents/licenses/gsap-skills-LICENSE").read_text(encoding="utf-8"), "new license\n")
        self.assertIn(NEW_SHA, (self.root / ".codex/docs/GSAP_UPSTREAM.md").read_text(encoding="utf-8"))
        self.assertFalse((self.root / ".agents/GSAP_UPSTREAM.md").exists())
        setup.link_claude()
        setup.validate()

    def test_fresh_gsap_installation_succeeds(self):
        with self.upstream():
            setup.install_gsap(False)
        setup.link_claude()
        setup.validate()
        self.assertIn(NEW_SHA, (self.root / ".codex/docs/GSAP_UPSTREAM.md").read_text(encoding="utf-8"))

    def test_invalid_upstream_is_rejected_before_replacement(self):
        self.install_existing_gsap()
        before = self.installed_snapshot()
        for options in ({"invalid_skill": True}, {"missing_license": True}, {"empty_license": True}):
            with self.subTest(options=options), self.upstream(**options):
                with self.assertRaises(RuntimeError):
                    setup.install_gsap(True)
                self.assertEqual(self.installed_snapshot(), before)

    def test_metadata_directory_conflicts_are_preserved_before_download(self):
        for relative in (".codex/docs/GSAP_UPSTREAM.md", ".agents/licenses/gsap-skills-LICENSE"):
            conflict = self.root / relative
            conflict.mkdir(parents=True)
            marker = conflict / "my-work.txt"
            marker.write_text("keep", encoding="utf-8")
            with self.subTest(path=relative), mock.patch.object(setup.subprocess, "run") as run:
                with self.assertRaises(RuntimeError):
                    setup.install_gsap(True)
                run.assert_not_called()
                self.assertEqual(marker.read_text(encoding="utf-8"), "keep")
            marker.unlink()
            conflict.rmdir()

    def test_failed_fresh_installation_restores_absence(self):
        before = self.installed_snapshot()
        real_rename = Path.rename
        failed = False

        def fail_replacement(source, target):
            nonlocal failed
            if Path(target) == self.skills / setup.GSAP[2] and not failed:
                failed = True
                raise OSError("simulated replacement failure")
            return real_rename(source, target)

        with self.upstream(), mock.patch.object(Path, "rename", new=fail_replacement):
            with self.assertRaises((OSError, RuntimeError)):
                setup.install_gsap(False)
        self.assertTrue(failed)
        self.assertEqual(self.installed_snapshot(), before)
        self.assertEqual(list(self.root.glob(".setup-gsap-*")), [])

    def test_incomplete_fresh_rollback_retains_recovery_workspace(self):
        real_rename = Path.rename
        failed = False

        def fail_replacement_and_rollback(source, target):
            nonlocal failed
            if Path(target) == self.skills / setup.GSAP[2] and not failed:
                failed = True
                raise OSError("simulated replacement failure")
            if Path(target).name.startswith("failed-"):
                raise OSError("simulated rollback failure")
            return real_rename(source, target)

        with self.upstream(), mock.patch.object(Path, "rename", new=fail_replacement_and_rollback):
            with self.assertRaisesRegex(RuntimeError, "recovery incomplete") as error:
                setup.install_gsap(False)
        self.assertTrue(failed)
        workspaces = list(self.root.glob(".setup-gsap-*"))
        self.assertEqual(len(workspaces), 1)
        self.assertIn(str(workspaces[0]), str(error.exception))
        self.assertTrue((workspaces[0] / "prepared").is_dir())
        self.assertEqual(list((workspaces[0] / "backups").iterdir()), [])

    def test_readonly_clone_files_are_cleaned_after_success(self):
        with self.upstream(readonly_object=True):
            setup.install_gsap(False)
        self.assertEqual(list(self.root.glob(".setup-gsap-*")), [])

    def test_script_can_validate_from_another_working_directory(self):
        different_cwd = self.root / "elsewhere"
        different_cwd.mkdir()
        result = subprocess.run(
            [sys.executable, "-B", str(self.root / ".codex/scripts/setup.py"), "--validate"],
            cwd=different_cwd, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("19", result.stdout)


if __name__ == "__main__":
    unittest.main()
