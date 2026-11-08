---
name: api-design
description: "REST and GraphQL API architecture, endpoint contracts, validation, authentication, pagination, caching, error handling, versioning and external integrations. Use when designing or implementing HTTP APIs and service-to-service contracts."
---

# API Design and Integration

## Workflow
1. Understand consumers, resource ownership, auth boundaries, expected volume and failure modes.
2. Agree on contract before parallel frontend/backend work: method/operation, path, payload, response, errors, permissions and versioning.
3. Validate data server-side; avoid exposing internal DB shapes as public API contracts.
4. Use clear status codes and predictable error objects without leaking implementation details or secrets.
5. Design bounded pagination/filtering, request-size limits, timeouts, rate limits and caching semantics.
6. Make mutating workflows retry-safe and idempotent where duplicate requests can cause damage.
7. For GraphQL, enforce operation cost/depth limits and authorization in resolvers/services; do not assume schema hiding is security.
8. For webhooks, validate authenticity and replay handling; acknowledge only after safe durable processing or appropriate queueing.
9. Document with a maintained OpenAPI/GraphQL schema and representative examples, including errors.

## Verification
Contract tests, role/tenant negative tests, retries, invalid inputs, 429/5xx and concurrent requests. Compare actual and documented payloads.

Reference: https://spec.openapis.org/oas/latest.html and https://owasp.org/www-project-api-security/
