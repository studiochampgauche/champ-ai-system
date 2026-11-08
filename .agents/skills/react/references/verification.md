# React Release and Review Checklist

## Baseline
- [ ] Versions, packages, router and build scripts inspected.
- [ ] Scope and acceptance criteria are explicit.
- [ ] Existing interaction, accessibility and design conventions preserved.

## New-project source and release contract
- [ ] New web products use React SPA navigation; existing applications retain their architecture unless migration is authorized.
- [ ] Editable HTML, JS/JSX, CSS and assets live in `project/src/`; `project/dist/` is generated from them, with no manual output edits or unnecessary framework starter.
- [ ] A minimal esbuild/Node build and package lock support `npm run dev`, `npm run build` and `npm run preview` from `project/`. Production JS/CSS is minified, and emitted files match the HTML's references and required copied assets.
- [ ] The release preview serves `dist/` without hidden development transforms. Direct URLs and reloads load the SPA, while missing assets and API requests keep correct status/content types; no repository files or server secrets are exposed.
- [ ] Changes to source HTML, styles and assets reach a fresh build; stale output is removed only within the verified generated directory.

## Correctness
- [ ] Hook and render purity rules respected.
- [ ] No redundant/contradictory state or effect feedback loop.
- [ ] API requests handle errors, cancellation/stale data and empty state.
- [ ] No console errors or hydration warnings in checked paths.
- [ ] Permissions enforced server-side; UI-only hiding is not authorization.

## UX and visual
- [ ] New-site and relevant loading/navigation-redesign requirements applied within scope; unrelated existing-app fixes did not introduce a migration or loading-system rebuild.
- [ ] Keyboard/focus, labels, visible validation and accessible status notifications checked.
- [ ] Responsive layouts inspected at representative mobile/tablet/desktop sizes.
- [ ] Typography, spacing, loading skeletons and motion are coherent.
- [ ] Reduced-motion support checked where animation is used.
- [ ] Required startup preloader works before React mounts, releases on critical readiness, and recovers when application initialization or critical assets fail; cached entry adds no artificial wait.
- [ ] JavaScript-disabled entry and an enabled-JavaScript entry with all bootstrap/watchdog scripts blocked both leave meaningful HTML/CSS recovery usable; no permanent blocking overlay depends solely on a JavaScript timeout.
- [ ] Cold/slow first frames inspected for unstyled content, font/media shifts and late animation resets; a settled screenshot is insufficient.
- [ ] Real route exit/pending/entry states, delayed or failed destinations, direct URLs, Back/Forward and rapid navigation checked; reduced motion and unavailable animation APIs remain usable. Mark non-applicable or unverified cases explicitly.
- [ ] Unless another treatment was requested, timed/frame evidence shows a fully visible outgoing view during preparation, a complete fade-out, destination switch at exit completion and immediate entry, with no partial-opacity stall or blank pause.

## Performance
- [ ] Bundle and route loading patterns inspected; no obvious duplicate data fetches.
- [ ] React profiler and browser traces used when diagnosing slowness.
- [ ] Before/after measurements recorded when performance changes are the task.

## Evidence
- [ ] Lint/typecheck/build/targeted tests run when available; record commands and outcomes.
- [ ] Relevant integration or E2E flow checked when possible.
- [ ] Remaining issues and unrun checks explicitly marked, not called complete.
