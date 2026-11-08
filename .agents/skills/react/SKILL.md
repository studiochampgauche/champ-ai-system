---
name: react
description: "Professional React engineering for React 19+ components, Hooks, state, effects, routing, forms, data fetching, rendering performance, React architecture, and production-quality SPA or full-stack React applications. Use when implementing, refactoring, reviewing, or debugging React code."
---

# React — Professional Engineering

## Mission
Build readable, testable, accessible, secure, maintainable, and responsive React applications at a high professional standard. Use https://react.dev/ as the canonical React reference. Check the installed React version and current documentation before applying version-specific features; do not infer the project's version from this skill.

## Workflow
1. **Inspect**: read package.json and lockfile, React version, framework, router, build tool, existing components, lint rules, tests, styling, and design tokens. Preserve established conventions and integrations; a stack migration needs user authorization.
2. **Define outcome**: state expected UI/behavior, loading/empty/error states, accessibility needs, mobile behavior, and acceptance criteria. For defects, reproduce them before editing when feasible.
3. **Design the smallest sound solution**: identify component boundaries, sources of truth, data flow, and server/client responsibilities. Prefer composition over abstraction for its own sake.
4. **Implement**: follow React rules, preserve semantics, isolate external effects, handle asynchronous races/cancellation, and avoid divergent state.
5. **Verify**: type-check if configured; lint; run targeted tests, build, and browser checks when tools allow. Check console errors, navigation, keyboard interaction, responsiveness, and cleanup.
6. **Improve**: fix actionable defects found within the requested scope and rerun relevant checks. Report measured outcomes and blocked checks separately.

## Default setup for new applications
- Build new web products and demos as React SPAs with client routing and a persistent shell. Use plain JavaScript/JSX, native CSS and only the dependencies required by the requested behavior: React/React DOM, standalone `react-router-dom` for real routes and GSAP for suitable motion.
- Work in `project/src/` for editable HTML, JS/JSX, CSS and assets. Use esbuild as a minimal development dependency through a small Node build script; generate the deployable application in `project/dist/`. Production JS/CSS must be bundled/minified as appropriate, and the HTML shell and required assets copied or processed explicitly. Never hand-edit the generated output.
- Provide `npm run dev`, `npm run build` and `npm run preview` from `project/`, and retain a package lock. Verify the exact `dist/` output in preview and production, including direct URLs, refresh and asset/API behavior under the SPA fallback.
- Do not bootstrap Next.js, Nuxt, Vinext, Vite or equivalent framework/starter stacks, nor add TypeScript or a complete UI suite, without explicit user authorization. A deployment plugin or example command does not override this constraint.
- Let esbuild resolve/bundle the selected package formats and transform JSX when used. Do not ship JSX or raw CommonJS to the browser, add runtime Babel/CDNs implicitly, or replace esbuild with a homemade bundler. Follow the [source-to-dist contract](references/architecture.md#source-to-dist-delivery).

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

## Startup and route presentation
- Apply these defaults to new websites/demos and relevant loading/navigation redesigns. Unrelated fixes in an existing application must not trigger a migration or loading-system rebuild.
- Implement the workspace's default startup preloader unless the user opts out. The initial HTML/loading shell and essential styles must work before React or GSAP loads. Hand off after the first usable commit, critical presentation and animation start states are ready; independently arm bounded error/timeout recovery before app initialization. Do not use a late `useEffect` to create the first loading screen after content has flashed.
- Keep meaningful HTML/CSS recovery usable if JavaScript is disabled or every bootstrap/watchdog script is blocked. A JavaScript timeout cannot be the only escape from the loader; `<noscript>` alone does not cover enabled JavaScript with blocked scripts. A recovery message or retry/help action is sufficient; do not promise the complete React application without JavaScript.
- Use client routing for real internal routes in new React sites and keep the shared shell mounted. Coordinate destination rendering/data and critical presentation with exit/pending/entry states; retain a stable view while waiting and recover from failed or superseded navigation. Do not replace this with a timed `location.assign()` and call it a coordinated route transition.
- Apply the `ui-ux` default sequence unless the user requests another treatment: prepare the destination while the current route stays fully visible, finish its fade-out completely, commit the prepared route at exit completion, and start its entry immediately. Coordinate router readiness, the committed render and animation completion; do not wait on data or lazy modules halfway through a fade, add a post-exit delay, or expose a blank gap. Keep route preparation cancellable so a superseded destination cannot replace the latest requested view.
- Integrate with the chosen router lifecycle instead of intercepting every anchor globally. Preserve deep links, Back/Forward, focus, scroll restoration, downloads, external links and modified/new-tab clicks. Reduced motion and unsupported animation APIs must provide immediate usable navigation; clean up interrupted animations.
- Verify startup/preloader, first-paint stability and real route transitions separately in the browser, including slow/failed resources and rapid navigation. A first-render animation or passing build alone does not satisfy these criteria. Preserve an existing architecture unless migration is authorized.

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
