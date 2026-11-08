---
name: nodejs
description: "Node.js backend engineering for async processing, HTTP services, event loop, streams, queues, workers, error handling, logging and reliability. Use when developing or optimizing server-side JavaScript or TypeScript."
---

# Node.js Backend Engineering

## Before implementation
Inspect runtime version, framework, package manager, module format, deployment strategy and existing service boundaries. Do not introduce a new Node major or framework incidentally.

## Rules
- Keep the event loop responsive; avoid sync I/O and expensive CPU work in request paths. Use worker threads/queues where justified by measurement.
- Validate request data and permission checks at the server boundary, not only in React.
- Use parameterized queries and transactions for related database mutations.
- Bound payload sizes, timeouts, retries, concurrency and resource usage. Apply cancellation/AbortSignal where supported.
- Design asynchronous workflows for duplicate delivery and partial failure: idempotency keys, durable state changes, retryable jobs and poison-message handling.
- Use structured logging and correlation/request IDs; redact tokens, secrets and private data.
- Separate configuration from code; handle graceful shutdown, health checks and connection draining.
- Avoid synchronous errors being swallowed; distinguish expected validation, operational failures and programmer bugs.
- Audit dependencies for advisories and update deliberately; preserve lockfiles.

## Verification
Run target tests, build/typecheck, request integration and error-path tests, plus targeted profiling or load tests when performance is a requirement. Measure before/after, not assumptions.

References: https://nodejs.org/learn and https://nodejs.org/en/learn/getting-started/security-best-practices
