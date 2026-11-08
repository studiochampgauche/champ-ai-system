# Champ AI System

**Bring an agency workflow to your coding agent.**

Reusable roles, practical skills and a clear workspace for **Codex, Claude Code and Gemini CLI**. Built by **Studio Champ Gauche inc.**, a web design and software development agency in Québec.

**5 specialist roles · 27 skills · 3 tool formats · Your product in `project/`**

[Quickstart](#quickstart) · [Meet the agents](#meet-the-agents) · [Skills](#skills-for-the-work-at-hand) · [Setup guide](.codex/docs/SETUP.md)

---

## A repeatable way to build

Give the main agent a product brief. It can delegate focused work, apply relevant skills, review the result and correct issues within the task's scope.

The kit gives that workflow a shared foundation:

| What you get | Why it matters |
| --- | --- |
| Clear specialist responsibilities | Architecture, design, implementation, review and infrastructure have defined owners. |
| One source for three tools | Edit canonical roles once, then generate native agent definitions. |
| Skills loaded for the task | Bring in relevant procedures without requiring every skill for every request. |
| A dedicated product directory | Keep application files together in `project/`, separate from the AI kit. |
| Verification as part of delivery | Ask for actual checks, evidence and clear reporting of anything unverified. |

These are instructions and tooling for your existing coding agent. Your chosen model, tool access and permissions provide the execution capabilities. Delegation depends on the host tool's support and settings.

## Quickstart

You need **Python 3.11+** and a configured installation of **one** supported AI tool. Git is needed to clone the repository or download GSAP updates.

### 1. Start a workspace

Clone or download this repository into a new folder. If the repository is marked as a GitHub template, use **Use this template** to start a separate repository for your product.

The outer folder can have any name. Keep the kit's internal structure intact.

### 2. Prepare the kit

From the outer workspace folder, run:

```sh
python --version
python .codex/scripts/setup.py --sync-agents --link-claude --validate
```

This generates the five roles in all three native formats, creates Claude's local skill links and validates the installation. The bundled skills make this setup step available without a download.

On Windows, if `python` selects an older installation, invoke your installed Python 3.11+ executable by its full path. The setup script reports an unsupported version explicitly.

### 3. Open the workspace and give your brief

Open the **outer workspace folder** in Codex, Claude Code or Gemini CLI. Start a new chat there. Keep your normal model and account configuration in the selected tool.

Try this starter prompt:

```text
Read AGENTS.md and apply this workspace's instructions.

Build [product] for [audience].
The main outcome is [user or business objective].
Required pages and features: [list].
Visual direction and available content: [details].
Technical and hosting constraints: [details].

Keep all product work inside project/.
Clarify essential missing information, then implement the agreed scope.
Use the relevant specialist agents and skills when useful.
Verify the result, address issues found and report the checks actually run.
```

For existing applications, plan their placement under `project/` and preserve their integrations. The installer does not move application files.

## Your product has a home

```text
your-workspace/
├── .agents/                Canonical roles, skills and upstream licenses
├── .codex/
│   ├── agents/             Generated Codex agents
│   ├── docs/               Kit documentation
│   ├── scripts/            Setup and maintenance tools
│   └── tests/              Installer regression tests
├── .claude/                Generated Claude agents and local skill links
├── .gemini/                Generated Gemini agents
├── .github/                Contribution guidance and CI
├── AGENTS.md               Shared working instructions
├── CLAUDE.md               Imports AGENTS.md
├── GEMINI.md               Imports AGENTS.md
└── project/                Everything belonging to your product
```

Product requests target **`project/` by default**, even when the chat is opened at the outer root. Source code, assets, dependency manifests, configuration, tests, documentation and build output belong there. Product commands run there or in the relevant subdirectory. Working from `project/` does not mean creating another `project/project/`.

Kit maintenance is a separate, explicit task. The main agent and generated specialist instructions carry this distinction. Before editing, agents are instructed to resolve their target directory; their final review should check the changed paths.

**This is a working rule, not filesystem confinement.** An instruction-following model can make mistakes. Strict write restrictions require permissions or a sandbox configured in the host tool. Open the outer workspace so its instructions and agent definitions are available.

The included `.gitkeep` keeps `project/` in Git. Remove it when scaffolding if your chosen tool requires an empty directory. Configure your product's hosting and build paths for `project/` or its appropriate output directory.

## Meet the agents

| Agent | Focus | Typical work |
| --- | --- | --- |
| [ARCHITECT](.agents/ARCHITECT.md) | Structure and technical decisions | Boundaries, contracts, data flows and implementation plans |
| [DESIGNER](.agents/DESIGNER.md) | Experience and visual quality | User journeys, responsive layouts, component states and accessibility |
| [ENGINEER](.agents/ENGINEER.md) | Implementation | Features, integrations, debugging, refactoring and tests |
| [AUDITOR](.agents/AUDITOR.md) | Independent verification | Correctness, security, performance and regression evidence |
| [DEVOPS](.agents/DEVOPS.md) | Operations and delivery | Environments, deployments, observability and recovery |

The main agent coordinates the work. Use the specialists that help the task; a small change does not require all five.

## Skills for the work at hand

The library includes **19 original skills** and **8 official GSAP skills**. Roles describe responsibilities; skills provide procedures for specific kinds of work.

| Area | Included skills |
| --- | --- |
| Frontend and experience | React, TypeScript, CSS/SCSS, UI/UX, accessibility |
| Backend and integration | Node.js, PHP, API design, database engineering |
| Security and transactions | Application security, multi-tenant authorization, Stripe payments |
| Architecture and delivery | Architecture design, code review, testing, Git workflows, DevOps, technical SEO, web performance |
| Motion | GSAP core, timelines, ScrollTrigger, plugins, utilities, React, frameworks and performance |

Browse the [skill library](.agents/skills/) or use the [recommended combinations](.codex/docs/SETUP.md#recommended-skills-by-task). The kit leaves framework selection to the project's requirements.

## Edit once, keep tools aligned

Update a canonical role such as `.agents/ENGINEER.md`, then regenerate its native definitions:

```sh
python .codex/scripts/setup.py --sync-agents --validate
```

Edit skills in `.agents/skills/`. After adding a skill directory, run:

```sh
python .codex/scripts/setup.py --link-claude --validate
```

`AGENTS.md` includes Studio Champ Gauche's operating principles and identity. Review and deliberately adapt that context when adopting the kit for another team. Keep local project requirements consistent with the shared rules.

Each workspace owns its copy of the kit. Changes to a template do not automatically update projects created from it.

## What gets checked

```sh
# Check the current installation
python .codex/scripts/setup.py --validate

# Exercise installer behavior in temporary workspaces
python -B -m unittest discover -s .codex/tests -v
```

Validation checks required skills, the canonical roles, generated agent synchronization, Codex TOML and Claude skill links. Regression tests exercise incomplete installations, incorrect links, GSAP provenance and recovery after simulated failures.

The [GitHub Actions workflow](.github/workflows/validate.yml) defines checks on Ubuntu and Windows with Python 3.11 and 3.13. Its run results appear in the repository's Actions tab after publication.

These checks cover the kit's installation tooling. Product quality, agent instruction adherence and model effectiveness need their own evaluation on real tasks. Maintenance tests are optional for everyday use and do not run your product.

## GSAP attribution and updates

The eight bundled GSAP skills come from GreenSock's official repository. Their recorded source commit is in [GSAP_UPSTREAM.md](.codex/docs/GSAP_UPSTREAM.md), and their license is preserved in [.agents/licenses/](.agents/licenses/gsap-skills-LICENSE).

For deliberate upstream updates, conflict resolution and detailed setup behavior, see the [setup guide](.codex/docs/SETUP.md).

## Help improve the workflow

Useful contributions include reproducible bug reports, clearer procedures and examples showing where the workflow succeeds or needs improvement. See [CONTRIBUTING](.github/CONTRIBUTING.md) before changing the kit.

If Champ AI System helps your work, a star makes it easier for others to discover it.

Original kit files are covered by [LICENSE](LICENSE). Bundled GSAP files retain their upstream license and attribution.
