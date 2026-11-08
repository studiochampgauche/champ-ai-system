---
name: typescript
description: "TypeScript design and refactoring for React, Node.js, API contracts, discriminated unions, runtime validation, strict type checking and safe migrations from JavaScript. Use for .ts and .tsx work and type-level architecture."
---

# TypeScript Engineering

## Method
- Inspect installed TypeScript version, tsconfig, lint rules, compilation targets and existing type conventions. Prefer established style.
- Keep `strict` type checking where already enabled. Never disable checks or add `@ts-ignore` to silence a design problem without justification.
- Model domain states with discriminated unions and narrow types; prefer readonly data for immutable flow.
- Distinguish types (compile-time) from runtime validation (untrusted input). Use the project's existing runtime schema library or appropriate explicit checks at trust boundaries.
- Avoid `any`, unsound assertions and non-null assertions when a safe model is possible; use `unknown` with narrowing for uncertain data.
- Represent API errors, optional values and async results explicitly. Avoid exposing secret or server-only types to clients.
- Keep generics intentional and local; do not create overabstracted types that require more time to understand than the behavior they model.
- When changing shared types, review dependent call sites and serializable data shapes before modifying.

## Verification
Run project typecheck/build, exercise runtime edge cases and inspect emitted client/server boundaries. Report any checks not run.

Reference: https://www.typescriptlang.org/docs/
