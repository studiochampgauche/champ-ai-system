---
name: devops-infrastructure
description: "DevOps and infrastructure operations for Linux, WHM/cPanel, CloudLinux, PHP-FPM, Apache/Nginx, TLS, DNS, email authentication, observability, CI/CD, backup and safe deployment. Use for server configuration, incidents and releases."
---

# DevOps and Infrastructure

## Safety first
- Identify exact server/environment, role, OS, package versions, application impact and privileges before changing live configuration.
- Require explicit authorization before production restarts, firewall/DNS changes, destructive commands, database upgrades, security scans or changes that might cause downtime.
- Prefer diagnostics and a reversible plan. Validate backups, config snapshots and rollback before risky changes.

## Operations workflow
1. Inspect service health, logs, error rates, resource use, queues and relevant configs; identify an evidence-based hypothesis.
2. Distinguish symptom from root cause; document user impact and blast radius.
3. Choose minimal correction, check syntax and dependencies, perform approved change and monitor result.
4. Verify HTTP/TLS, application logs, database connectivity, mail flow and performance as relevant to the change.
5. Preserve existing hardening, firewall rules, key selectors, mail DNS policy and client-specific configuration.

## Special focus
- PHP-FPM: worker count must reflect memory per process and RAM, incoming concurrency and queue latency; raising limits without resource analysis can worsen outages.
- Email: SPF, DKIM, DMARC and hostname/DNS changes can break delivery; verify alignment and provider-specific rules before rollout.
- Security: least privilege, secrets management, patch policy, audit logs, service isolation and tested restore.
- Deployments: health checks, reversible migrations, safe rollouts, monitoring and documented recovery.

## Evidence
Return commands executed, pre/post state, service status, error/warning logs and rollback information. Do not claim production verified without actual access and checks.

References: https://docs.cpanel.net/ and https://www.cloudflare.com/learning/
