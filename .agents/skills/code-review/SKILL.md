---
name: code-review
description: "Independent code review and change validation covering correctness, risks, architecture fit, security, performance, tests, maintainability and regression evidence. Use for pull requests, release reviews and audit handoffs."
---

# Code Review — Evidence-First

## Purpose
Provide an independent judgment of whether a change satisfies the request and preserves existing behavior. Do not approve by intuition or because code looks tidy.

## Review workflow
1. Read original requirement, diff, affected callers, tests and project rules.
2. Prioritize behavior and risk: incorrect logic, missing validation/authorization, tenant leaks, data corruption, races, dangerous deployments, user-visible regressions.
3. Review interface design, failure paths, maintainability, data migrations, performance and accessibility relevant to the change.
4. Run focused checks when permitted; write a minimal repro or targeted test for suspected high-impact issues.
5. Classify findings by severity and identify exact file/line or condition and reproduction; distinguish confirmed defects from speculation.
6. Feed actionable findings back for remediation; after fixes, rerun checks and independently verify the resolution.

## Report format
- Scope and reviewed artifacts.
- Confirmed findings, severity, reproduction and recommended action.
- Tests run and actual results.
- Unverified areas and remaining risk.
- Approval status linked to explicit acceptance criteria.

Never assert that code is secure, production-ready or tested if corresponding evidence is absent.
