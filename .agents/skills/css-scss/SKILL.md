---
name: css-scss
description: "Professional CSS/SCSS architecture, responsive layouts, design tokens, cascade/scoping, modern layout, typography, CSS performance and maintainable styling. Use when building or auditing styles, animations and frontend design systems."
---

# CSS and SCSS Engineering

## Workflow
- Inspect stylesheet organization, supported browsers, delivery method, naming conventions and design tokens. Prefer plain CSS for new projects unless another styling tool is explicitly required; this skill does not authorize installing a preprocessor or bundler.
- Prefer existing tokens and patterns. Use modern Grid/Flexbox and fluid responsive sizing appropriately; avoid brittle absolute positioning.
- Organize SCSS modules with clear ownership; prevent overly deep nesting, selector specificity wars and global leaks.
- Separate structural/layout, component and state styles. Use logical properties where helpful for internationalization.
- Avoid expensive layout-thrashing effects, unbounded `will-change`, forced synchronous measurement and unexpected scroll locking.
- Define hover, focus-visible, active, disabled, error and reduced-motion states.
- Audit long content, narrow screens, zoom/reflow, high contrast and actual rendered results.
- Use GSAP for advanced animation choreography rather than replicating complex timelines in fragile CSS; keep simple transitions in CSS.

## Typography and composition
- Define type tokens by content role: display, heading, lead, body, supporting copy, label and control. Differentiate roles through size, weight, line-height and measure as needed; do not rely on one small paragraph size beneath oversized headings.
- Use readable relative sizing and responsive ranges. Preserve meaningful copy at narrow widths and 200% zoom rather than reducing it to tiny labels. Choose and load the actual weights or variable axes used; avoid synthetic weights and arbitrary font changes between components.
- Keep layout rules driven by content, with deliberate grouping, alignment and spacing. Do not bake decorative eyebrow rules or trailing arrow icons into every heading/button component. Follow the project's chosen art direction instead of imposing one universal visual theme.

## Stable first paint
- Deliver the initial background, layout and essential styles before revealing the experience. Avoid client-effect-only styling and late stylesheet discovery; establish animation start states before their first visible frame.
- Load only the fonts and critical weights needed. Prefer early font discovery over a late CSS `@import` chain; select `font-display` and fallback metrics deliberately, and verify wrapping and layout during font swaps. Preload only fonts proven critical to the first viewport.
- Reserve image/media space with dimensions or aspect ratios. A preloader does not replace stable typography, asset sizing or correct stylesheet delivery.
- Do not hide the entire document until a fragile animation callback runs. Any initially hidden animated region needs an error/timeout escape and a usable script-failure fallback. Reduced-motion styles must expose the usable final state and release modal/scroll-lock state correctly.

## Validation
Check configured style tooling, responsive layout, overflow, text zoom, keyboard focus and contrast. Inspect cold/warm first paint, font swaps, menu transitions and route changes, including reduced motion and interrupted animation. Provide browser evidence when available and identify checks not performed.

References: https://developer.mozilla.org/en-US/docs/Web/CSS, https://web.dev/learn/performance/optimize-web-fonts and https://sass-lang.com/documentation/
