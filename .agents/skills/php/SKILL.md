---
name: php
description: "Professional PHP development for PHP 8+, web apps, WordPress integration, backend endpoints, Composer, database access, validation, maintainable services, and secure deployment. Use when writing, modernizing or reviewing PHP code."
---

# PHP Engineering

## Approach
- Inspect PHP runtime/minimum supported version, Composer packages, framework and cPanel/CloudLinux setup before using version-specific language features.
- Preserve WordPress conventions where relevant; use established hooks/APIs instead of bypassing the platform unless the project explicitly requires a standalone architecture.
- Use strict typing where compatible, clear interfaces, explicit exceptions and separation of request handling from domain logic.
- Apply input validation, output escaping and safe SQL APIs. Never concatenate untrusted input into queries.
- Use framework or project-approved CSRF protection, sessions and server-side permission checks.
- Keep secrets in safe environment/config stores and out of public webroot and VCS.
- Use Composer with locked dependencies where adopted; verify extension availability and target PHP-FPM configuration.
- Diagnose PHP-FPM bottlenecks using utilization, memory, pool queue and log evidence before changing `pm.max_children`.

## Verification
Run syntax checks, configured static analysis/tests and representative HTTP checks; audit logs and error handling. For deployment changes, verify rollback and backup options before applying.

References: https://www.php.net/manual/en/ and https://developer.wordpress.org/
