---
name: architecture-design
description: "Software architecture, requirements analysis, trade-off decisions, system boundaries, ADRs, event flows, schema evolution, scalability and delivery planning. Use for major features, new platforms, migrations or complex technical decisions."
---

# Architecture and Technical Design

## Objective
Create the simplest architecture that satisfies current requirements with a credible path for future growth. Avoid both premature complexity and fragile shortcuts.

## Method
1. Inspect codebase, operational constraints, existing ADRs, contracts, dependencies and team capability.
2. Identify functional requirements, quality attributes, users/permissions, data sensitivity, expected volume, budgets and failure tolerance.
3. Draw component boundaries and data flows (as text/diagrams when relevant); define ownership and trust boundaries.
4. Compare alternatives and trade-offs; record assumptions, reversible vs irreversible decisions, migration cost and operational burden.
5. Produce a practical implementation sequence with testable acceptance criteria and safe dependency order.
6. Communicate clear interfaces for parallel ENGINEER/DEVOPS/DESIGNER tasks.
7. Revisit design when tests or real measurements contradict assumptions; do not defend an architecture for its own sake.

## Artifacts
- Short ADR: context, decision, alternatives, consequences and when to reconsider.
- Interfaces: endpoint contracts, events, schemas, error behavior and permissions.
- Delivery plan: dependencies, risks, verification and rollout/rollback.

## Caution
Do not change production systems or commit to financial/business arrangements just because a design recommends them. Present trade-offs and request authorization when appropriate.
