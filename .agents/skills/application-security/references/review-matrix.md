# Security Review Matrix

| Boundary | Verify | Negative test |
|---|---|---|
| Authentication | Session identity, expiration, renewal and logout | Request using expired/revoked credentials is denied |
| Authorization | User may perform action on exact object | Change object ID to another user/tenant and verify denial |
| Admin operations | Elevated permission is checked server-side | Regular member calls admin route directly and fails |
| Data access | Tenant predicate in every scoped query | Cross-tenant read/write returns no sensitive data |
| Writes | Valid schema, size and allowed transitions | Send forged/extra fields, invalid roles and state transitions |
| SQL / command | Parameterization and shell avoidance | Untrusted delimiters remain data, not executable instructions |
| Web rendering | Contextual escaping and safe DOM | Untrusted markup cannot execute script |
| CSRF | Stateful browser write requests protected | Cross-site request fails or is denied by robust anti-CSRF design |
| Uploads | MIME/content, size, storage and serving | Script payload cannot execute when served back |
| External URL fetch | SSRF defenses and redirect checks | Block localhost, metadata IPs and private targets |
| Webhooks | Signature verification, replay/duplication handling | Invalid/replayed event cannot mutate state |
| Dependencies | Known vulnerabilities and integrity | Lockfile/audit reports and upgrades reviewed |
| Errors/logging | No private data leakage | 500s show generic message, logs redact secrets |

Never use live customer data for adversarial testing without permission. Test environments and fixtures are preferred.
