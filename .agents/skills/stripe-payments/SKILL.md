---
name: stripe-payments
description: "Stripe and Stripe Connect integration design for SaaS/marketplaces: payments, billing, connected accounts, webhooks, idempotency, refunds, disputes, reconciliation and multi-tenant money movement. Use for payment or subscription work."
---

# Stripe Payments and Connect

## High-risk domain rules
- Read current Stripe documentation for the exact API version and selected payment flow before coding. Avoid assuming older platform charge or Connect patterns still apply.
- Choose charge/payment ownership, settlement/payout model, application fees, refunds, dispute liability, onboarding and platform permissions explicitly.
- Never handle raw card data unless integration requirements and PCI scope demand it; prefer Stripe-hosted/Stripe.js flows when appropriate.
- Treat Stripe events as asynchronous and potentially repeated or out of order. Verify signatures using the raw request body, record processed event IDs and implement idempotent handlers.
- Store a clear mapping among platform account, connected account, customer, payment, invoice, refund and internal ledger records.
- Handle retries, partial failure, negative balances, cancellations, disputes and reconciliation; never treat frontend success navigation as proof of payment.
- Validate payment amount/currency on a trusted server. Define fee and tax calculations with authoritative product/legal inputs rather than guessing rates.
- Restrict secrets and publishable keys to their intended environments; use test/live separation and safe logs.

## Verification
Test positive and negative webhook paths, replay/duplicate events, refunds, partial failures, API idempotency, permissions and reconciliation in test mode before release.

Documentation: https://docs.stripe.com/ , https://docs.stripe.com/connect , https://docs.stripe.com/events
