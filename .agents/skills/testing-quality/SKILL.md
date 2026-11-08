---
name: testing-quality
description: "Testing strategy and hands-on verification for unit, integration, browser E2E, concurrency, performance regressions and security negative tests. Use when creating tests, fixing a bug, auditing quality or validating a release."
---

# Testing and Quality Assurance

## Testing pyramid is a tool, not a quota
Choose the cheapest trustworthy test that verifies the risk: unit tests for isolated rules, integration tests for data/permission boundaries, E2E for essential user journeys, load tests for performance requirements.

## Workflow
1. Write acceptance criteria for requested behavior and important negative cases.
2. Reproduce bugs first where possible; create regression tests that fail before the fix.
3. Test the service boundary, state transitions, auth/tenant isolation, validation and failure handling.
4. For UI, verify mobile/desktop, keyboard, focus, empty/loading/error states and reduced motion.
5. Run configured test suites, lint, typecheck and build. Do not invent unavailable scripts.
6. When load testing: define environment, concurrency, ramp, duration, data, error rate, throughput and latency percentiles (P50/P95/P99). Respect approved target and rate limits.
7. For every failed criterion within scope, diagnose, fix and retest. Escalate only real constraints or required authorization.

## Web experience checks
- Inspect desktop and mobile views across the whole page and its relevant states, including controls, forms, cards/lists, menus and overlays. Compare the result with the chosen art direction and its actual references, not a generic component checklist.
- Check cold and warm loads, initial styles, font/image layout changes and any preloader's readiness, failure and timeout paths. Capture the first visible states when tooling permits; a settled screenshot cannot establish absence of FOUC.
- Exercise actual route changes, direct URLs, Back/Forward, rapid repeated navigation and menu open/close interruptions. Check focus and scroll restoration, keyboard operation and reduced-motion behavior. Anchor scrolling alone is not a route-transition test.
- Review the dependency manifest against the authorized stack. Installer tests prove installation behavior, not that an AI will follow design rules or produce an excellent site.

## Protect systems
Never start high-volume load tests or destructive security tests against production without explicit authorization. Use fixtures, cleanup and isolated environments.

## Evidence
Record commands, run times, environment, counts, failures, latency, screenshots/traces when relevant and whether each criterion passed. Distinguish unrun and passed.

Reference: https://playwright.dev/docs/intro and https://testing-library.com/docs/react-testing-library/intro/
