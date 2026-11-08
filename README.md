# Champ AI System

**Bring an agency workflow to your coding agent.**

Reusable roles, practical skills and a clear workspace for **Codex, Claude Code and Gemini CLI**. Built by **Studio Champ Gauche inc.**, a web design and software development agency in Québec.

**5 specialist roles · 27 skills · One workspace for your next product**

[Quickstart](#quickstart) · [Meet the agents](#meet-the-agents) · [Skills](#skills-for-the-work-at-hand) · [Setup guide](.codex/docs/SETUP.md)

---

## A repeatable way to build

Use Champ AI System to build a website, develop a web application or improve an existing product. Give your coding assistant a brief, and use a shared process for planning, implementation and review.

The kit gives that workflow a shared foundation:

| What you get | Why it matters |
| --- | --- |
| Clear specialist responsibilities | Architecture, design, implementation, review and infrastructure have defined owners. |
| A workflow across three AI tools | Use the same roles and skills with Codex, Claude Code or Gemini CLI. |
| Skills loaded for the task | Bring in relevant procedures without requiring every skill for every request. |
| A dedicated product directory | Keep application files together in `project/`, separate from the AI kit. |
| Verification as part of delivery | Ask for actual checks, evidence and clear reporting of anything unverified. |

The kit runs inside your existing AI coding tool, using your configured model and permissions. Specialist delegation depends on the tool's available features and settings.

## Quickstart

You need **Python 3.11+** and a configured installation of **Codex, Claude Code or Gemini CLI**.

### 1. Start a workspace

Clone or download this repository into a new folder. If the repository is marked as a GitHub template, use **Use this template** to start a separate repository for your product.

### 2. Prepare the kit

From the outer workspace folder, run:

```sh
python --version
python .codex/scripts/setup.py --sync-agents --link-claude --validate
```

Run this required step in each new workspace. It prepares the agents and skills for use and checks the installation. All source skills are included; no additional download is needed.

### 3. Open the workspace and give your brief

Open the **workspace folder containing `AGENTS.md`** in your AI tool and start a new chat.

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

For help with an existing application or an installation issue, see the [setup guide](.codex/docs/SETUP.md).

## Your product has a home

Keep the workspace root open in your AI tool. The instructions direct product work into **`project/`**, where your application code, assets, dependencies and tests belong.

```text
your-workspace/
├── .agents/                Roles and skills
├── .codex/                 Codex configuration and kit tools
├── .claude/                Claude Code configuration
├── .gemini/                Gemini CLI configuration
├── AGENTS.md               Shared working instructions
└── project/                Everything belonging to your product
```

Run your application's development, build and test commands from `project/`. File access restrictions are controlled by your AI tool; the workspace instructions guide the agent's behavior.

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

Browse the [skill library](.agents/skills/) or use the [recommended combinations](.codex/docs/SETUP.md#recommended-skills-by-task). New web projects favor React, plain JavaScript, native CSS and Node.js where needed, with dependencies chosen for the actual features. The [setup guide](.codex/docs/SETUP.md#product-defaults) explains the technical and design defaults.

## Make it your own

Adapt `AGENTS.md` to your team's identity and working practices. It starts with Studio Champ Gauche's operating principles. Customize the roles and skills in `.agents/` as your needs evolve, then rerun the setup command to apply those changes.

Each project has its own copy of the kit, so you can tailor its instructions independently. See the [setup guide](.codex/docs/SETUP.md) for customization, updates and troubleshooting.

## Help improve the workflow

Useful contributions include reproducible bug reports, clearer procedures and examples showing where the workflow succeeds or needs improvement. See [CONTRIBUTING](.github/CONTRIBUTING.md) before changing the kit.

If Champ AI System helps your work, a star makes it easier for others to discover it.

## License and credits

Original kit files are covered by [LICENSE](LICENSE). The eight GSAP skills come from GreenSock's official repository and retain their [upstream license](.agents/licenses/gsap-skills-LICENSE). See [GSAP_UPSTREAM.md](.codex/docs/GSAP_UPSTREAM.md) for their source revision.
