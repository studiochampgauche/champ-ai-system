---
name: web-performance
description: "Web and backend performance engineering using profiling, Core Web Vitals LCP/INP/CLS, bundle analysis, query traces, load testing, caching and measured P95/P99 latency. Use when a user requests speed, scalability, high traffic or performance fixes."
---

# Web and Service Performance

## Never stop at a poor benchmark
A test revealing unacceptable P95 or low throughput is a diagnostic result, not task completion. Identify the bottleneck, apply safe targeted changes, retest and compare against agreed objectives.

## Baseline and success criteria
- State tested environment, host/resources, software versions, traffic profile and response correctness.
- Establish baseline LCP, INP and CLS for real user/browser performance; separately measure API/server P50/P95/P99, requests/sec, error rate and resource saturation.
- Use published Core Web Vitals guidance as a default (good at 75th percentile: LCP <= 2.5s, INP <= 200ms, CLS <= 0.1), but explicit project requirements take precedence.
- Performance is not acceptable if high throughput comes at the cost of correctness, lost messages or cross-tenant data leakage.

## Triage
1. Identify whether delay is in network/TLS, CDN/caching, render path, JavaScript, query layer, server concurrency, external APIs or storage.
2. Gather waterfall, traces, CPU/memory, slow queries, queues, connection pools and event-loop utilization where applicable.
3. Prioritize high-impact changes: eliminate N+1 queries, reduce blocking assets, cache safely, right-size query indexes, bound concurrency, code split and remove redundant work.
4. Re-run the **same** representative test profile. Watch cold vs warm cache, p99 outliers, resource saturation and regressions.
5. Stop when acceptance criteria are met, risk/effort is disproportionate, or a real blocker is documented; don't optimize endlessly.

## First paint and transitions
- Inspect the initial render sequence on cold and warm loads, including slow or failed critical requests. Distinguish missing/late styles, font swaps, image-induced shifts and late animation initialization; a single settled screenshot cannot establish the cause of FOUC.
- Make essential styles, fonts and first-viewport media discoverable early. Avoid unnecessary font families/weights and late CSS import chains; tune fallback metrics, reserve asset dimensions and preload selectively. Verify the rendered result as well as the request waterfall.
- Honor the workspace's default startup preloader for new websites/demos and loading/navigation redesigns unless the user opts out; do not remove it merely because a cached load is fast. Treat it as a bounded interface state, not a performance optimization. Deliver its essential shell early, release it on actual critical readiness or a usable fallback, and arm recovery independently of the application bundle. Preserve meaningful HTML/CSS recovery if JavaScript or the bootstrap is unavailable. Do not add fake progress, artificial waits or a dependency on every page asset; measure perceived usability and LCP with the implemented loader.
- Verify client navigation and browser history separately from initial loading. Check actual outgoing/pending/incoming presentation and destination readiness: an exit timer plus full reload does not prove a coordinated transition. Avoid redundant downloads, long interaction locks, leaked timelines and content flashes; rapid navigation, errors, unsupported APIs and reduced motion must remain usable. Respect an existing multi-document architecture rather than migrating it solely for animation.
- Require separate evidence for startup/preloader, first-paint stability and route transitions. Slow or block relevant requests in a controlled test environment to verify readiness and recovery; a successful setup/build test or a settled screenshot establishes none of these. Record an unavailable browser check as unverified, not passed.
- Report what was measured and what was only inferred from code. Confirming local cold-load behavior does not establish real-user field performance or a guarantee across all networks.
- Profile the production `dist/` build for new SPA products, not only development output. Verify minification, actual transferred asset sizes and route behavior. JavaScript/CSS minification and HTTP gzip/Brotli compression are distinct; configure transfer compression only when the host supports it, without treating an archive of sources as a deployable build.

## Authorization
Never run disruptive tests on production without explicit scope, safe load ceiling and approval. Never assume access to prod implies authorization for stress tests.

References: https://web.dev/articles/vitals, https://web.dev/articles/optimize-inp and https://web.dev/learn/performance/optimize-web-fonts
