# Multi-tenant Threat Scenarios

For business A and business B fixtures, and roles owner/admin/member/invited/anonymous:
1. Try reading, editing, deleting, exporting and listing B's resources with A's session.
2. Try changing `tenantId`, `ownerId`, `companyId`, resource identifiers or nested foreign keys in JSON bodies, query strings and headers.
3. Verify child entities inherit the parent tenant; checking only the top-level route is not enough.
4. Test direct upload/file URLs, job queues, notifications, WebSocket subscriptions, caches, audit logs and search indexes.
5. Test revoked membership, role downgrade, invitation expiry and concurrent updates.
6. Ensure operations are atomic where authorization and business state interact; test race and double-submit behavior.
7. Confirm errors and timing do not leak object existence across tenant boundaries.
8. Require proofs: test name, role fixture, ID scope, expected denial and actual response.
