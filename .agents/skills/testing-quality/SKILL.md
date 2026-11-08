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
- Inspect decorative arrows in buttons, links, cards and scroll prompts, including adjacent, hover and focus variants. Apply the `ui-ux` exceptions for genuine directional controls or explicit user requests. Check for automatic eyebrow markers and cosmetic replacements such as a dot instead of a line; selective justified accents remain valid. Source searches across text, SVG/icons and CSS can support, but cannot replace, rendered inspection.
- Check homepage hero fit on tall and short desktop screens, mobile portrait/landscape and text zoom. Unless another treatment was requested, the header, hero and outer spacing should fill the available viewport when content fits. Longer content must grow naturally without clipping, unreachable controls or horizontal overflow; fixed-height underfill/overflow is a defect.
- Treat startup/preloader, first-paint stability and route transitions as separate acceptance criteria. For new websites/demos and loading/navigation redesigns, verify the default required preloader and actual route transitions unless the user opted out; use not-applicable for routes only when no internal routes exist or an opt-out applies. Unrelated existing-site fixes do not require a navigation redesign. Record pass/fail/not-tested plus observed evidence in the existing handoff, without adding a report file merely for process.
- Check cold, warm and slow loads. In a controlled browser test, delay or fail relevant CSS, fonts, hero media and application initialization; check that the loading shell precedes the app, readiness releases promptly, and timeout/error recovery works independently of a failed bundle. Capture initial frames and handoff through a recording, filmstrip or equivalent timed evidence. Distinguish CSS FOUC, font replacement, image shifts and animation/reload flashes. A settled screenshot or source check cannot prove their absence.
- Disable JavaScript and separately block the early bootstrap/watchdog; verify a meaningful HTML/CSS recovery state without a permanent covering loader. A no-JavaScript version of the entire application is not required.
- Exercise actual route changes, direct URLs, refresh, Back/Forward, rapid repeated navigation and menu interruptions. Delay/fail a destination and inspect outgoing/pending/incoming presentation, recovery, focus/scroll restoration, normal link behavior and reduced motion. Check the fallback when the animation API is unavailable. A URL change, anchor scroll or exit timeout followed by a reload is not proof of a coordinated page transition.
- For the default sequential fade, capture the timeline from preparation through entry: the outgoing view stays fully visible during loading, reaches opacity 0 at exit completion, the prepared destination replaces it immediately, and entry starts without an added hold. Check warm and delayed destinations for a partial-opacity plateau, blank pause, abrupt cut or redundant delay. Record timings or equivalent frame evidence; arbitrary durations, a settled screenshot or a changed URL do not prove this sequence. Respect an explicitly requested alternative and verify that reduced motion bypasses the animations.
- Repair failures and retest within scope. If browser fault injection or temporal capture is unavailable, record the specific unverified criteria and concrete limitation; do not mark the experience complete or describe source inspection/build/setup tests as equivalent evidence.
- Review the dependency manifest against the authorized stack. Installer tests prove installation behavior, not that an AI will follow design rules or produce an excellent site.
- For the new-product SPA baseline, build from `src/` and run browser checks against the actual production `dist/` output. Verify normal internal links do not reload the document, direct route entry/refresh works, assets and API/missing-file requests retain correct responses, and deployment contains no source tree or `node_modules/`. Check minified JS/CSS and copied/processed assets, not merely a successful build exit code.

## Protect systems
Never start high-volume load tests or destructive security tests against production without explicit authorization. Use fixtures, cleanup and isolated environments.

## Evidence
Record commands, run times, environment, counts, failures, latency, screenshots/traces when relevant and whether each criterion passed. Distinguish unrun and passed.

Reference: https://playwright.dev/docs/intro and https://testing-library.com/docs/react-testing-library/intro/
