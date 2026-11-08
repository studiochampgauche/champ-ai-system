---
name: application-security
description: "Secure application design and security review for web apps, APIs, authentication, authorization, sessions, injection, XSS, CSRF, SSRF, uploads, secrets, dependencies, threat modeling and OWASP ASVS. Use when building, auditing or repairing security-sensitive functionality."
---

# Application Security — Defense in Depth

## Objective
Apply risk-based security engineering to implementation and review. The primary baseline is OWASP ASVS 5.0 and OWASP Cheat Sheet Series; OWASP Top 10 2025 is an awareness guide, not a substitute for verification requirements.

## Workflow
1. Identify assets, user roles, trust boundaries, sensitive data, exposed endpoints, third-party dependencies, and attacker-controlled input.
2. Map applicable ASVS controls to the current feature; record threat scenarios and abuse cases rather than reviewing generic checkboxes alone.
3. Trace each sensitive operation end-to-end: authentication, authorization, validation, data access, logging, error handling, and side effects.
4. Fix vulnerabilities at the actual trust boundary; add negative tests that prove the bypass no longer works.
5. Reassess the attack surface introduced by changes and report residual risks with severity, prerequisites, and evidence.

## Always inspect
- **Authorization**: server-side object and action checks on every protected request; default deny; least privilege; tenant isolation at query and write boundaries; negative IDOR/BOLA tests.
- **Authentication/session**: phishing-resistant MFA where warranted; server-controlled session lifecycle; secure/HttpOnly/SameSite cookies and appropriate CSRF defense; no session identifiers in logs or URLs.
- **Input/output**: validated types, sizes and allowed formats; parameterized SQL; contextual output encoding and safe DOM APIs; never use raw HTML for untrusted input without proven sanitization.
- **APIs**: strict access control, content-size/time limits, throttling, predictable error codes without data leakage, safe pagination and resource bounds.
- **Uploads & SSRF**: safe filenames, isolated storage, content validation, file limits; egress allowlists/blocked internal addresses and redirect handling for server-side fetches.
- **Secrets & cryptography**: managed secrets, transport encryption, correct algorithms and rotation; no credentials in source, logs or tests.
- **Dependencies**: audit and update supported packages; review advisories and lockfile changes; no unverified supply-chain scripts.
- **Logging**: security-relevant events without passwords/tokens/PII; alerting and retention proportional to risk.

## Evidence-based completion
- Provide a finding, affected route/file, proof or reproducible negative test, risk, remediation, and test result.
- Never claim an application is secure merely because static checks pass. Distinguish review depth and what was not inspected.
- Production scans, penetration testing and disruptive tests require explicit authorization and scoped targets.

Read [Security review matrix](references/review-matrix.md) and [Multi-tenant abuse tests](references/tenant-tests.md) where relevant.

## Official references
- https://asvs.owasp.org/
- https://owasp.org/projects/top-ten
- https://cheatsheetseries.owasp.org/
- https://developer.mozilla.org/en-US/docs/Web/Security
