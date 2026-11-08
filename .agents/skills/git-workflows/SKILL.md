---
name: git-workflows
description: "Git branch hygiene, collaborative editing, conflict prevention, commits, diffs, pull requests, safe rollbacks and parallel agent worktrees. Use for multi-agent code coordination, PR preparation and version control tasks."
---

# Git Collaboration and Worktrees

## Safe collaboration
- Inspect git status, branch and outstanding changes before editing. Preserve unrelated user work.
- For parallel agents that may edit files, prefer isolated worktrees or clearly disjoint file ownership. Agree on interfaces first.
- Keep changes scoped to the request. Review diffs for accidental secrets, generated files and broad formatting noise.
- Do not rebase/force-push shared branches, delete worktrees or reset unrelated changes without explicit approval.
- Run relevant checks before commit; use descriptive, narrowly scoped commits.
- Resolve merge conflicts deliberately; avoid blindly selecting one side if both include independent work.

## Handoff
Provide branch/worktree name, files affected, integration dependencies, commands/checks and outstanding conflicts. Never claim a commit or merge succeeded unless Git confirms it.

Reference: https://git-scm.com/docs
