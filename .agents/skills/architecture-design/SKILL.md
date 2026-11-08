---
name: architecture-design
description: "Software architecture, requirements analysis, trade-off decisions, system boundaries, ADRs, event flows, schema evolution, scalability and delivery planning. Use for major features, new platforms, migrations or complex technical decisions."
---

# Architecture and Technical Design

## Objective
Create the simplest architecture that satisfies current requirements with a credible path for future growth. Avoid both premature complexity and fragile shortcuts.

## New web project baseline
- Build new web products and demos as React SPAs with client routing and a persistent application shell, using plain JavaScript/JSX and native CSS. Use Node.js built-ins for local scripts and actual server needs; a static client does not require an application backend.
- Before scaffolding or installing, state a short stack contract in the working plan: source and release directories, route behavior, dependency purposes, build commands and hosting. Do not create an architecture document solely to satisfy this step.
- Keep editable HTML, JS/JSX, CSS and assets in `project/src/`; generate deployment output in `project/dist/`. Group pass-through files in `project/src/public/` only when useful, then copy them into the release output. Use esbuild as a development dependency with a small Node build script to bundle React, transform JSX when used, minify production JS/CSS, and copy/process the HTML shell and required assets. Do not hand-edit `dist/` or serve the repository as the public root.
- Provide `npm run dev`, `npm run build` and `npm run preview` from `project/`, with a package lock and dependency versions compatible with the chosen Node runtime. The preview and deployment must serve the built `dist/` output. Check direct route entry and reload with an HTML-navigation fallback; missing assets and API requests must retain their proper responses.
- Add only dependencies used by the requested behavior: `react` and `react-dom`, standalone `react-router-dom` for real routes, GSAP for suitable motion, and esbuild for the build contract. Do not install an entire UI kit, ORM, authentication stack or connector layer speculatively.
- Next.js, Nuxt, Vinext, Vite and comparable framework/starter stacks require explicit user authorization. Plain JavaScript/JSX is the default; do not add TypeScript, Tailwind or another toolchain automatically. Use esbuild's API rather than recreating dependency resolution, JSX conversion or minification in custom scripts; do not rely on runtime Babel or an implicit runtime CDN.
- User and repository stack requirements take precedence over plugin starter defaults. Verify a minimal compatible deployment format before adopting a host's template. If hosting is incompatible, explain the specific constraint and obtain a decision instead of silently replacing the stack.
- Start with the files and folders the current feature needs. Add abstraction layers, workspaces, database infrastructure and cross-demo shared modules only when concrete requirements justify them. Preserve established architectures in existing applications unless migration is requested.

## Method
1. Inspect codebase, operational constraints, existing ADRs, contracts, dependencies and team capability.
2. Identify functional requirements, quality attributes, users/permissions, data sensitivity, expected volume, budgets and failure tolerance.
3. Draw component boundaries and data flows (as text/diagrams when relevant); define ownership and trust boundaries.
4. Compare alternatives and trade-offs; record assumptions, reversible vs irreversible decisions, migration cost and operational burden.
5. Produce a practical implementation sequence with testable acceptance criteria and safe dependency order.
6. Communicate clear interfaces for parallel ENGINEER/DEVOPS/DESIGNER tasks.
7. Revisit design when tests or real measurements contradict assumptions; do not defend an architecture for its own sake.

## Artifacts
- Short ADR: context, decision, alternatives, consequences and when to reconsider.
- Interfaces: endpoint contracts, events, schemas, error behavior and permissions.
- Delivery plan: dependencies, risks, verification and rollout/rollback.

## Caution
Do not change production systems or commit to financial/business arrangements just because a design recommends them. Present trade-offs and request authorization when appropriate.
