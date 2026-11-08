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

Keep canonical roles and skills in `.agents/` in version control. The native definitions in `.codex/agents/`, `.claude/agents/` and `.gemini/agents/` are generated locally and ignored by Git, as are the local Claude skill links in `.claude/skills/`. Edit the canonical sources or the generator, then run setup to regenerate the native definitions. Do not force-add generated files. Preserve upstream GSAP attribution and license files.

## Develop and verify

Use Python 3.11 or later. No third-party Python packages or API credentials are needed for the installer tests.

```sh
python .codex/scripts/setup.py --sync-agents --link-claude --validate
python -B -m unittest discover -s .codex/tests -v
```

The normal setup command uses the included skills without downloading GSAP. Tests use temporary workspaces and simulated downloads. When changing failure handling, exercise the relevant error path as well as the successful path.

The GitHub workflow generates the native agents, creates skill links and runs these checks from a fresh checkout on Windows and Linux with Python 3.11 and 3.13. Review the run results in the repository's Actions tab when submitting a change. GitHub Actions is optional for local installation and use.

## Submit a focused change

1. Explain the problem and the expected behavior. For a substantial change, open an issue first to discuss the approach.
2. Keep the change scoped and preserve unrelated work.
3. Update the README when changing public setup instructions or behavior.
4. Run the relevant checks and include the commands and actual results in the pull request.
5. For changes to agent instructions, include an example request and the behavior it should produce. Installer tests do not demonstrate model quality or instruction compliance.

Bug reports should include the operating system, Python version, AI tool/version when relevant, command or minimal prompt, and the observed result. Remove credentials and private client material from examples.
