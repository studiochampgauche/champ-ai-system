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

## Authorization
Never run disruptive tests on production without explicit scope, safe load ceiling and approval. Never assume access to prod implies authorization for stress tests.

References: https://web.dev/articles/vitals and https://web.dev/articles/optimize-inp
