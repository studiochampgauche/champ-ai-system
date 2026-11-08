---
name: architecture-design
description: "Software architecture, requirements analysis, trade-off decisions, system boundaries, ADRs, event flows, schema evolution, scalability and delivery planning. Use for major features, new platforms, migrations or complex technical decisions."
---

# Architecture and Technical Design

## Objective
Create the simplest architecture that satisfies current requirements with a credible path for future growth. Avoid both premature complexity and fragile shortcuts.

## New web project baseline
- Prefer React with plain JavaScript and native CSS. Use Node.js built-ins for an actual server requirement; a static client does not need an application backend.
- Before scaffolding or installing, state a short stack contract in the working plan: runtime, rendering/navigation approach, dependency purposes, browser delivery and hosting. Do not create an architecture document solely to satisfy this step.
- Add only dependencies used by the requested behavior: `react` and `react-dom` for React rendering, `react-router-dom` when routing is needed, GSAP when motion calls for it. Do not install an entire UI kit, ORM, authentication stack or connector layer speculatively.
- Next.js, Nuxt, Vinext, Vite and comparable framework/scaffolding/build stacks require explicit user authorization. Plain JavaScript is the default; do not add TypeScript, Tailwind or another toolchain automatically. Do not recreate a bundler/framework under local scripts to evade this constraint.
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
