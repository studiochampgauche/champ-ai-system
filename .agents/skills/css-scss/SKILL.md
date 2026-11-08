---
name: css-scss
description: "Professional CSS/SCSS architecture, responsive layouts, design tokens, cascade/scoping, modern layout, typography, CSS performance and maintainable styling. Use when building or auditing styles, animations and frontend design systems."
---

# CSS and SCSS Engineering

## Workflow
- Inspect stylesheet organization, supported browsers, delivery method, naming conventions and design tokens. Prefer plain CSS for new projects. Follow the workspace's minimal esbuild build from `src/` to `dist/`; do not add a preprocessor or larger starter stack merely for styling. Edit source styles, never generated/minified output.
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
- Keep layout rules driven by content, with deliberate grouping, alignment and spacing. Follow the project's chosen art direction instead of imposing one universal visual theme.
- Shared eyebrow components start as plain text, without automatic lines, dots, icons or badges. Make any justified accent an explicit project-specific choice, not a global pseudo-element or a replacement symbol for the same ornament habit.
- Do not inject decorative arrows into or beside buttons, links, cards or scroll prompts, including hover/focus states, pseudo-elements, masks, backgrounds and icon components. Apply the `ui-ux` distinction between forbidden adornment, actual directional/disclosure controls and an explicit user request.

## Homepage viewport sizing
- Unless the user specifies otherwise, let the homepage hero span the available width with intentional gutters and target the available viewport height through `min-block-size`, with automatic block size and border-box sizing. Avoid fixed pixel heights or maximum-height caps. Prefer `inline-size: 100%` within the full-width page shell over `100vw` that can introduce scrollbar overflow; constrain inner copy independently.
- Account for the actual header and outer vertical spacing once: subtract an in-flow header and outer gaps from the viewport target. For an overlay header, keep the viewport target and reserve internal clearance for readable content. Include safe-area padding within the size calculation. Do not add a full viewport below an in-flow header or subtract an overlay header twice.
- Choose mobile viewport units deliberately: `svh` gives a stable initial screen with browser controls visible; `dvh` tracks the visible height as those controls change and requires checking resize/scroll jumps. Use a compatible fallback for the supported browsers; do not rely only on legacy `100vh` for mobile fit. See [MDN viewport units](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#relative_length_units_based_on_viewport).
- Keep text and actions in flow so content can grow beyond the minimum on short screens, long translations or zoom. Do not impose a fixed-height ceiling, hide content overflow or shrink text to force a fit. Crop decorative media in its own layer; ensure padding, media aspect ratios and absolute positioning do not force unnecessary hero overflow. Verify tall/short screens, mobile portrait/landscape, 200% zoom and horizontal overflow.

## Stable first paint
- Deliver the initial background, layout and essential styles before revealing the experience. Avoid client-effect-only styling and late stylesheet discovery; establish animation start states before their first visible frame.
- For the required startup preloader on new websites/demos, style the initial HTML/loading shell before the application can paint. Critical shell styles and its background must not depend on a late module or animation library. Use a delivery method compatible with the site's CSP. A loader mounted after content has appeared cannot prevent its first flash.
- Load only the fonts and critical weights needed. Prefer early font discovery over a late CSS `@import` chain; select `font-display` and fallback metrics deliberately, and verify wrapping and layout during font swaps. Preload only fonts proven critical to the first viewport.
- Reserve image/media space with dimensions or aspect ratios. A preloader does not replace stable typography, asset sizing or correct stylesheet delivery.
- Do not hide the entire document until a fragile animation callback runs. Any initially hidden animated region needs an error/timeout escape and a usable script-failure fallback. Reduced-motion styles must expose the usable final state and release modal/scroll-lock state correctly.
- Keep a meaningful HTML/CSS recovery state accessible when all JavaScript is disabled or the bootstrap/watchdog is blocked. Activate any content-covering loading state only with recovery already armed; do not ship a static overlay that requires unavailable JavaScript to disappear.
- Coordinate CSS entry/exit states with destination readiness and the `ui-ux` transition sequence. Unless the user specifies otherwise, animate the outgoing page view fully to opacity 0, switch at actual exit completion, and immediately animate the prepared incoming view to opacity 1. Keep the outgoing view at full opacity during preparation; do not pause a partial fade or use mismatched CSS durations and navigation timers. A body opacity animation on each reload does not coordinate navigation. Cancel stale animations and restore usable styles on interruption/error. Respect reduced motion and provide an immediately usable fallback when the chosen transition API is unavailable.

## Validation
Check configured style tooling, responsive layout, overflow, text zoom, keyboard focus and contrast. Inspect cold/warm first paint, font swaps, menu transitions and route changes, including reduced motion and interrupted animation. Provide browser evidence when available and identify checks not performed.

References: https://developer.mozilla.org/en-US/docs/Web/CSS, https://web.dev/learn/performance/optimize-web-fonts and https://sass-lang.com/documentation/
