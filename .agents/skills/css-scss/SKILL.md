---
name: css-scss
description: "Professional CSS/SCSS architecture, responsive layouts, design tokens, cascade/scoping, modern layout, typography, CSS performance and maintainable styling. Use when building or auditing styles, animations and frontend design systems."
---

# CSS and SCSS Engineering

## Workflow
- Inspect stylesheet organization, supported browsers, bundler, naming conventions and design tokens.
- Prefer existing tokens and patterns. Use modern Grid/Flexbox and fluid responsive sizing appropriately; avoid brittle absolute positioning.
- Organize SCSS modules with clear ownership; prevent overly deep nesting, selector specificity wars and global leaks.
- Separate structural/layout, component and state styles. Use logical properties where helpful for internationalization.
- Avoid expensive layout-thrashing effects, unbounded `will-change`, forced synchronous measurement and unexpected scroll locking.
- Define hover, focus-visible, active, disabled, error and reduced-motion states.
- Audit long content, narrow screens, zoom/reflow, high contrast and actual rendered results.
- Use GSAP for advanced animation choreography rather than replicating complex timelines in fragile CSS; keep simple transitions in CSS.

## Validation
Check style build/lint (if configured), responsive layout, overflow, keyboard focus and WCAG contrast. Provide browser evidence when available.

References: https://developer.mozilla.org/en-US/docs/Web/CSS and https://sass-lang.com/documentation/
