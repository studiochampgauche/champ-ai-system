# Contributing to Champ AI System

Useful improvements start with a concrete task, an observed problem, and evidence that the change helps.

## Where changes belong

| Change | Source |
| --- | --- |
| Specialist responsibilities | `.agents/ARCHITECT.md`, `DESIGNER.md`, `ENGINEER.md`, `AUDITOR.md`, `DEVOPS.md` |
| Reusable procedures | `.agents/skills/<name>/SKILL.md` |
| Shared working instructions | `AGENTS.md` |
| Setup and validation | `.codex/scripts/setup.py` |
| Installer regression scenarios | `.codex/tests/test_setup.py` |
| Your website or application | `project/` in your own project repository |

Keep this template's `project/` directory ready for a new product. Do not submit a client application as a change to the kit.

Generated agent definitions belong in version control, but edit their canonical sources or the generator, then regenerate them. Local Claude skill links are ignored and recreated during setup. Preserve upstream GSAP attribution and license files.

## Develop and verify

Use Python 3.11 or later. No third-party Python packages or API credentials are needed for the installer tests.

```sh
python .codex/scripts/setup.py --sync-agents --link-claude --validate
python -B -m unittest discover -s .codex/tests -v
```

The normal setup command uses the included skills without downloading GSAP. Tests use temporary workspaces and simulated downloads. When changing failure handling, exercise the relevant error path as well as the successful path.

The GitHub workflow runs the same checks on Windows and Linux with Python 3.11 and 3.13. Its results are available after the workflow runs in the published repository.

## Submit a focused change

1. Explain the problem and the expected behavior. For a substantial change, open an issue first to discuss the approach.
2. Keep the change scoped and preserve unrelated work.
3. Update the README when changing public setup instructions or behavior.
4. Run the relevant checks and include the commands and actual results in the pull request.
5. For changes to agent instructions, include an example request and the behavior it should produce. Installer tests do not demonstrate model quality or instruction compliance.

Bug reports should include the operating system, Python version, AI tool/version when relevant, command or minimal prompt, and the observed result. Remove credentials and private client material from examples.
