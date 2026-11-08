---
name: multi-tenant-authorization
description: "Multi-company SaaS tenant isolation, RBAC and ABAC policy design, object-level authorization, permission matrices, data access and cross-tenant negative tests. Use for marketplaces, multi-sided platforms, admin panels and APIs with multiple organizations."
---

# Multi-Tenant Authorization

## Design
1. Define tenant/organization membership, role hierarchy, entity ownership, permitted actions and lifecycle changes.
2. Specify a permission matrix and encode checks in trusted application service/policy boundaries; default deny.
3. Require authenticated tenant context from a verified membership, never solely from a client-submitted tenant ID.
4. Scope reads and writes at the database/query layer. For joins, exports, queues, events, caches, search and object storage, propagate tenant context safely.
5. Use least privilege for support/admin impersonation, background workers and service credentials. Log privileged access.
6. Separate platform operator privileges from tenant administrator privileges.
7. For PostgreSQL Row Level Security, treat it as defense-in-depth, configure roles/settings correctly and test for bypass; do not assume it is active simply because policies exist.

## Verification
- Create at least two tenants, multiple roles and known fixtures; test both permitted and forbidden actions.
- For each ID-bearing endpoint, replace a resource ID with one from another tenant and assert no data or mutation occurs.
- Include nested resources, filtered list endpoints, file downloads, external integrations and WebSocket channels.
- Validate revoked roles, stale sessions, races, bulk operations and queued tasks.

## Handoff
Return permission matrix changes, evidence of denial tests, data migration impacts, and unresolved cross-boundary risks.

Official reference: https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html
