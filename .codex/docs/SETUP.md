# Studio Champ Gauche — Cross-Agent Development Kit

A single-source professional agent and skill library for **Codex, Claude Code and Gemini CLI**.

## What is included

- `.agents/ARCHITECT.md`, `DESIGNER.md`, `ENGINEER.md`, `AUDITOR.md`, `DEVOPS.md`: one canonical role definition per agent.
- `.agents/skills/<skill>/SKILL.md`: 19 original professional skills, including React and application security, with extra React/security reference files.
- `.codex/agents/*.toml`, `.claude/agents/*.md`, `.gemini/agents/*.md`: native agent definitions generated locally by setup and ignored by Git. They embed canonical agent content, rather than depending on an agent's ability to open a separate file.
- `.codex/scripts/setup.py`: cross-platform setup/validation tool and official GSAP installer for all three AI tools.
- `.codex/tests/test_setup.py`: optional maintenance tests that exercise the installer; these are not needed to run it or develop a product.
- `project/`: the dedicated directory for the website, application, or product built by the AI system. Its `.gitkeep` placeholder keeps the directory in Git until product files are added.
- This checkout includes eight official GSAP skills, their license under `.agents/licenses/`, and their recorded source commit in `.codex/docs/GSAP_UPSTREAM.md`. An installation without GSAP is also supported; download the official skills using the setup command below when needed.

## Workspace layout

The generated directories appear after setup:

```text
workspace/
  .agents/       # Canonical AI roles and skills
  .codex/
    agents/     # Generated Codex agents; ignored by Git
    docs/       # AI kit documentation
    scripts/    # AI kit setup tools for Codex, Claude and Gemini
    tests/      # Optional AI kit maintenance tests
  .claude/       # Local agents and skill links; generated paths ignored
  .gemini/       # Local agents; generated path ignored
  .github/       # Contribution guidance, issue forms and CI
  .gitignore     # Local links, credentials, dependencies and build exclusions
  AGENTS.md      # Shared working instructions
  CLAUDE.md      # Imports AGENTS.md
  GEMINI.md      # Imports AGENTS.md
  project/       # All files belonging to the product being built
```

Open the outer workspace directory in your AI development tool. Keep product source, assets, dependency manifests and lockfiles, configuration, tests, scripts, documentation, and build output inside `project/`. Run product commands from that directory or its relevant subdirectory. The product's internal structure follows its features and the Product Technology policy in `AGENTS.md`.

Product requests default to that application directory even when the chat starts at the outer root. Starting a command inside `project/` must not create `project/project/`. These are shared agent instructions; strict filesystem confinement requires host-tool permissions or a sandbox.

Run the kit's setup command from the outer workspace root. Configure the product's development server, build and deployment to use `project/` or the appropriate output directory inside it. The outer workspace directory can have any name. Remove `project/.gitkeep` when scaffolding the product if the chosen tool requires an empty directory.

## Prepare a project workspace

1. Copy or clone the kit **into the outer workspace directory**, including `project/`. For an existing application, plan its placement under `project/` while preserving its files and integrations. This checkout contains `AGENTS.md`, `CLAUDE.md` and `GEMINI.md`: merge the relevant instructions into existing policy files instead of overwriting them. The setup script itself does not modify these files or move application files.
2. From the outer workspace root, check `python --version`: Python **3.11 or later** is required. If `python` selects an older installation, invoke an installed 3.11+ interpreter by its full path. Git is required when downloading GSAP.
3. Run the required local setup:

```sh
python .codex/scripts/setup.py --sync-agents --link-claude --validate
```

This generates native subagent definitions, links all skills to `.claude/skills/` and validates the installation. The agent definitions and links are intentionally absent from a fresh clone because they are generated outputs. The bundled source skills remain in Git, so this command needs no download.

The script locates the AI kit's workspace root from its own location (`.codex/scripts/setup.py`), independently of the current working directory and outer folder name. To run it from another directory, pass the full path to the script.

For a checkout without the optional GSAP skills, add `--install-gsap` to download the eight official skills and preserve their upstream attribution. If all eight already exist, that option preserves them and their provenance without downloading anything. A partial GSAP installation requires an explicit update.

## Share the kit on GitHub

Keep the canonical roles, skills, generator, documentation, maintenance tests and `project/.gitkeep` in version control. Apply the same policy to all tools: `.codex/agents/`, `.claude/agents/` and `.gemini/agents/` are generated locally and ignored by Git. `.claude/skills/` contains local links and is also ignored. The rest of `.codex/`, including the setup script, remains tracked. The root `.gitignore` also excludes common credentials, caches, dependencies and product build outputs; product source and dependency lockfiles remain tracked.

The source kit can be published without running setup first. After cloning or downloading it, run the full setup command above before using the specialist agents; it generates the native definitions, creates local links and validates the workspace. The [README](../../README.md) is the public entry point; [CONTRIBUTING](../../.github/CONTRIBUTING.md) explains maintenance. The [GitHub workflow](../../.github/workflows/validate.yml) generates agents and links from the committed sources before validating and running isolated installer tests on Linux and Windows.

If you want visitors to start independent product repositories from the kit, enable **Template repository** in the GitHub repository settings after publishing. Each resulting repository owns its copy; future template changes do not propagate automatically.

## Update GSAP skills

To update official GSAP skills intentionally:

```sh
python .codex/scripts/setup.py --install-gsap --update-gsap --link-claude --validate
```

## Edit once; distribute to all tools

- Edit `.agents/ENGINEER.md` (or another agent source), then run `python .codex/scripts/setup.py --sync-agents`.
- Edit `.agents/skills/react/SKILL.md` (or any other skill). Codex and Gemini read `.agents/skills/` directly; Claude accesses the same files via its `.claude/skills/` links.
- When adding a new skill directory, rerun `python .codex/scripts/setup.py --link-claude --validate`.
- Native generated files stay local and are recreated by setup; do not edit or commit their copies. After pulling changes to canonical roles or the generator, rerun `python .codex/scripts/setup.py --sync-agents --validate`.

## Existing project policy files

Your custom `AGENTS.md` stays as the project instruction source for Codex. Claude Code and Gemini CLI can import it via their root files:

`CLAUDE.md`: `@AGENTS.md`

`GEMINI.md`: `@AGENTS.md`

Review your existing files rather than allowing an installer to overwrite them. Ensure the company-wide rules are given to specialized agents, either by platform inheritance or explicitly through the task context.

## Security and operational boundaries

- Skills are **procedures**, not automatic permissions. Sensitive shell tools, production servers and external services still require real tool access and authorization.
- A fresh GSAP installation or explicit update fetches the current official repository revision. The recorded commit describes the files installed by that operation; this command does not pin future downloads to that commit.
- GSAP updates prepare and validate all new skills, the license and provenance before replacing existing files. If replacement fails, the installer attempts to restore the previous files. If restoration also fails, it reports where the backups were retained. This protects against handled copy/replacement errors; it is not a crash-recovery mechanism for a power loss or forcibly terminated process.
- The installer preserves existing Claude skill folders and links. Incorrect targets or ordinary folders in place of links are reported as conflicts; inspect and resolve those conflicts before rerunning `--link-claude`.
- Windows links use symbolic links if available, or local directory junctions as fallback. Junctions are machine-local. After moving or cloning a project, inspect existing links and recreate any obsolete ones, then rerun `--link-claude --validate`.
- No tests of your live application, server or model runtime are implied by the skill validation script.

## Validation and regression tests

Complete setup first. `--validate` checks the existing installation; it does not generate missing files.

```sh
python .codex/scripts/setup.py --validate
python -B -m unittest discover -s .codex/tests -v
```

Validation requires the five canonical roles, the 19 internal skills, all 15 generated agent files synchronized with their sources, and Claude links targeting the corresponding skill directories. Additional skill directories must contain valid `SKILL.md` metadata. GSAP may be absent for offline setup; if present, all eight skills are required. An empty or incomplete installation fails validation.

For kit maintenance, the regression suite exercises the installer in temporary workspaces with simulated GSAP downloads. It covers missing or stale files, incorrect links, provenance preservation and recovery after failures. Product tests belong in `project/`.

The GitHub Actions workflow runs setup and these regression tests automatically when the kit changes in the repository. It is a maintenance check; local installation and everyday use do not require GitHub Actions.

## Product defaults

New web products start with React, plain JavaScript and native CSS; use Node.js when a server is needed. Choose only libraries required by the features. Frameworks and bundlers such as Next.js, Nuxt, Vinext and Vite require explicit authorization, including when a publishing plugin suggests its own starter. Browser dependency delivery must be verified; the [React architecture guide](../../.agents/skills/react/references/architecture.md) explains the no-bundler constraints. Existing applications are preserved unless migration is requested.

The shared art-direction rules cover the complete experience and its states. Use the [UI/UX skill](../../.agents/skills/ui-ux/SKILL.md) to inspect relevant live references, define a distinct direction, and review the full rendered product, including first paint, loading and navigation. These instructions guide future work; they do not retrain a model or guarantee a visual result without review.

## Recommended skills by task

| Task | Skills |
| --- | --- |
| React app or frontend | `architecture-design`, `react`, `css-scss`, `accessibility`, `ui-ux`; `typescript` only when the project uses it |
| GSAP animations in React | `gsap-react`, `gsap-core`, `gsap-timeline`, `gsap-performance`, `gsap-scrolltrigger` as relevant |
| SaaS backend | `nodejs`, `api-design`, `database-engineering`, `application-security` |
| Multi-company authorization | `multi-tenant-authorization`, `application-security`, `testing-quality` |
| Stripe SaaS/marketplace | `stripe-payments`, `api-design`, `testing-quality`, `application-security` |
| Performance audit | `web-performance`, `testing-quality`, `database-engineering`, relevant stack |
| Linux/cPanel deployment | `devops-infrastructure`, `application-security`, `web-performance` |
| Premium UI/UX | `ui-ux`, `css-scss`, `accessibility`, `react` |
| Release/readiness | `code-review`, `testing-quality`, `git-workflows` |

## Official references

- React: https://react.dev/
- GSAP official skills: https://github.com/greensock/gsap-skills
- Agent Skills specification: https://agentskills.io/specification
- OWASP ASVS: https://asvs.owasp.org/
- OWASP Top 10 2025: https://owasp.org/projects/top-ten
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- Web Vitals: https://web.dev/articles/vitals

All original files are provided as editable project guidelines. GSAP skill code/instructions remain upstream-owned and must retain the upstream license.
