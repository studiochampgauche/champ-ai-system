# React Release and Review Checklist

## Baseline
- [ ] Versions, packages, router and build scripts inspected.
- [ ] Scope and acceptance criteria are explicit.
- [ ] Existing interaction, accessibility and design conventions preserved.

## Correctness
- [ ] Hook and render purity rules respected.
- [ ] No redundant/contradictory state or effect feedback loop.
- [ ] API requests handle errors, cancellation/stale data and empty state.
- [ ] No console errors or hydration warnings in checked paths.
- [ ] Permissions enforced server-side; UI-only hiding is not authorization.

## UX and visual
- [ ] Keyboard/focus, labels, visible validation and accessible status notifications checked.
- [ ] Responsive layouts inspected at representative mobile/tablet/desktop sizes.
- [ ] Typography, spacing, loading skeletons and motion are coherent.
- [ ] Reduced-motion support checked where animation is used.

## Performance
- [ ] Bundle and route loading patterns inspected; no obvious duplicate data fetches.
- [ ] React profiler and browser traces used when diagnosing slowness.
- [ ] Before/after measurements recorded when performance changes are the task.

## Evidence
- [ ] Lint/typecheck/build/targeted tests run when available; record commands and outcomes.
- [ ] Relevant integration or E2E flow checked when possible.
- [ ] Remaining issues and unrun checks explicitly marked, not called complete.
