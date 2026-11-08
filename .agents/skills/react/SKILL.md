---
name: react
description: "Professional React engineering for React 19+ components, Hooks, state, effects, routing, forms, data fetching, rendering performance, React architecture, and production-quality SPA or full-stack React applications. Use when implementing, refactoring, reviewing, or debugging React code."
---

# React — Professional Engineering

## Mission
Build readable, testable, accessible, secure, maintainable, and responsive React applications at a high professional standard. Use https://react.dev/ as the canonical React reference. Check the installed React version before applying version-specific features. React 19.3 was the current release when this skill was authored (2026-11-08); never assume the project is already on that version.

## Workflow
1. **Inspect**: read package.json and lockfile, React version, framework, router, build tool, existing components, lint rules, tests, styling, and design tokens. Preserve established conventions and integrations. Do not change the framework or dependency stack without justification.
2. **Define outcome**: state expected UI/behavior, loading/empty/error states, accessibility needs, mobile behavior, and acceptance criteria. For defects, reproduce them before editing when feasible.
3. **Design the smallest sound solution**: identify component boundaries, sources of truth, data flow, and server/client responsibilities. Prefer composition over abstraction for its own sake.
4. **Implement**: follow React rules, preserve semantics, isolate external effects, handle asynchronous races/cancellation, and avoid divergent state.
5. **Verify**: type-check if configured; lint; run targeted tests, build, and browser checks when tools allow. Check console errors, navigation, keyboard interaction, responsiveness, and cleanup.
6. **Improve**: fix actionable defects found within the requested scope and rerun relevant checks. Report measured outcomes and blocked checks separately.

## Non-negotiable React rules
- React components and Hooks must remain pure during render. Do not mutate props or state or perform external side effects while rendering.
- Call Hooks only at the top level of React components or custom Hooks. Never call component functions directly as ordinary functions.
- Derive display values from existing props/state during render. Do not duplicate them into state or use `useEffect` merely to synchronize state with itself.
- Treat `useEffect` as synchronization with external systems, not as the default place for business logic; clean up listeners, timers, subscriptions, requests, and third-party integrations.
- Separate server state, URL/navigation state, and ephemeral UI state. Respect the project's chosen data-fetching and router APIs; avoid introducing a second overlapping state system.
- Make errors, retries, pending, empty and success states explicit for user-facing async operations.
- Use stable keys for dynamic lists. Avoid index keys for re-orderable items.
- Prefer clear components and idiomatic JavaScript/TypeScript over clever generic abstractions.

## Quality standards
- Use semantic HTML and accessible labels, focus management and keyboard navigation; validate against WCAG 2.2 AA when applicable.
- Keep styling cohesive: reuse tokens, spacing, typography, responsive breakpoints, and existing Sass/CSS architecture. Do not replace a project's established styling conventions gratuitously.
- Avoid unnecessary effect chains, broad Context providers, event handlers with hidden side effects, and premature memoization.
- Optimize using profiling evidence. Consider React Compiler only when supported/configured; manual memoization should be justified by observed behavior.
- Use virtualized lists only when necessary, code splitting for meaningful bundle boundaries, and stable data-fetching/caching when appropriate.
- Keep secrets and sensitive authorization decisions out of client code. Treat the browser as untrusted.
- For GSAP in React, activate `gsap-react` and related official GSAP skills. Scope selectors, use useGSAP/context cleanup, respect reduced motion; do not run animations during render.

## Read supporting references as relevant
- [Architecture and data boundaries](references/architecture.md)
- [React patterns and anti-patterns](references/patterns.md)
- [Production verification checklist](references/verification.md)

## Authoritative documentation
- https://react.dev/learn
- https://react.dev/reference/rules
- https://react.dev/learn/you-might-not-need-an-effect
- https://react.dev/learn/choosing-the-state-structure
- https://react.dev/learn/react-compiler

## Handoff
Describe files changed, rationale, checks run and their exact results, visual/keyboard checks, performance evidence where applicable, and remaining blockers. Never claim an unrun test passed.
