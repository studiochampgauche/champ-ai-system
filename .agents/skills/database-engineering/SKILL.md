---
name: database-engineering
description: "Database design and optimization for PostgreSQL and MariaDB, migrations, indexing, transactions, query plans, constraints, tenant isolation, backups and recovery. Use for schemas, SQL queries, data integrity or database performance."
---

# Database Engineering

## Principles
- Inspect DB engine/version, schema migrations, transaction semantics, query patterns, tenant boundaries and current indexes.
- Define invariant constraints in the DB when feasible: foreign keys, uniqueness, check constraints, non-null constraints and appropriate isolation.
- Prefer normalized domain schemas; denormalize only when justified by measured read/write trade-offs.
- Parameterize all queries. Keep SQL dialect-specific behavior explicit (PostgreSQL vs MariaDB); do not assume syntax parity.
- Treat migrations as production changes: estimate locks/time on real table sizes, design backwards-compatible rollout and reversibility when feasible.
- Measure queries with `EXPLAIN`/`EXPLAIN ANALYZE` using safe environment and realistic data volumes. Consider index selectivity and write costs.
- Use transactions for atomic business operations; prevent duplicate payment/event/ledger mutations with explicit uniqueness/idempotency constraints.
- Avoid leaking tenant data via joins, search, caching or aggregates.
- For sensitive data changes, confirm backup integrity, restore procedure and maintenance window before touching production.

## Validation
- Verify schema and migration on a staging copy if feasible; test nulls, duplicates, concurrent updates, rollback, tenant boundaries and realistic query load.
- Report query plans/latency before and after when optimizing performance. Never claim improvement based only on adding an index.

References: https://www.postgresql.org/docs/ and https://mariadb.com/kb/en/
