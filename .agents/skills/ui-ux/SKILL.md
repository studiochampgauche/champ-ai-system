---
name: ui-ux
description: "Premium UI/UX design systems, visual hierarchy, responsive layouts, typography, color, components, interactions, product journeys and visual QA. Use for interface design, redesign, usability and detailed frontend polish."
---

# UI / UX Design — Premium Digital Quality

## Objective
Deliver distinctive, considered interfaces that make complex products understandable and pleasant to use. Beautiful must also mean legible, accessible, stable and effective.

## Process
1. Learn product goals, audience, key flows, actual content, brand constraints and any established design system.
2. For new designs or substantial redesigns, inspect two or three relevant live references, using Awwwards for discovery and direct sites outside award galleries. Study desktop and mobile composition, typography, navigation/menu behavior, entry/loading and page transitions where observable. Record exact URLs and concrete observations in the existing brief or handoff; do not claim visits, motion checks or model training that did not occur. For targeted adjustments, reuse the established direction and references unless a specific gap requires more research. If access is unavailable, state that limitation and work from the available evidence.
3. Choose an art direction for this brief: composition, type roles, imagery, color and motion. Extract useful principles from references without copying their branding or layout. For a demo collection, compare the preceding demos and give each new brand a distinct direction; do not change fonts or colors at random just to appear different.
4. Map information architecture and real navigation before composing screens. A single long page is a deliberate choice, not the default way to avoid designing routes and transitions.
5. Inventory the components actually needed and define their typography, spacing and relevant states, including first entry, loading, empty, validation, error, success, disabled and interrupted interaction. Do not add components just to satisfy a checklist.
6. Inspect the rendered result on mobile and desktop, with long content, keyboard operation and reduced motion. Refine alignment, reading rhythm, contrast, interaction and perceived loading, then fix visible defects within scope.

## Standards
- Compose around the content and the user's next action. Do not reuse the same centered hero, alternating splits, card grid and closing CTA for every brief, or replace that recipe with arbitrary asymmetry, giant type or empty space.
- Do not automatically append arrows to buttons, prefix eyebrows with long rules, or fill margins with tiny labels, status chips and slogans. Each element must help orientation, explain content or communicate an action. Directional icons are appropriate when they convey direction or a state that the label does not already communicate.
- Establish readable roles for lead copy, paragraphs, supporting text, captions, labels and controls, using size, weight, line-height and measure deliberately. Do not make all non-heading text look alike or shrink meaningful information into microtext. Choose heading and text families for the brand and language; neither an editorial serif nor TikTok Sans is a universal default.
- Motion must reinforce understanding. Use GSAP for complex orchestration where justified; integrate `gsap-react`, `gsap-performance` and reduced-motion considerations.
- Preserve accessibility; hover-only and mouse-only UI is incomplete.
- Reuse existing components and tokens unless there is a clear reason to redesign.
- Never generate a decorative showcase image just to announce task completion.

## Whole-experience design
- Carry the chosen direction through composition, typography, imagery, links/CTAs, cards/lists, forms, filters, menus, overlays and footer wherever they exist. A strong hero cannot compensate for an unfinished rest of the experience.
- Give each component a clear content role and behavior. Repeated components should share a coherent language; hierarchy and purpose, not a requirement for every button to look unique, determine variation.
- Design the applicable default, hover, focus, pressed/selected, disabled, pending, empty, error and success states. For forms and filters, cover validation, feedback and recovery; for overlays, cover dismissal, focus and return to context. Keep decorative treatments subordinate to comprehension and use.
- Review complete journeys and the full page, including secondary routes and the footer. Recheck component consistency, content density, imagery crops, reading order and interaction feedback at mobile and desktop sizes.

## Navigation and motion
- Design the navigation with the same care as the page. Choose visible links, a drawer or a composed overlay based on content and available space; a hamburger is not an automatic desktop design. Specify open/close choreography, item hierarchy, active destination, hover/focus and touch states.
- Menus must handle Escape, focus placement and restoration, and scroll-lock cleanup. Trap focus only for modal menus and keep the background inert while modal. Use meaningful link labels and `aria-current` for the active destination; closing or interrupted animation must not leave invisible links focusable.
- Plan first entry and route changes together. For presentation sites with multiple routes, provide a deliberate transition when motion is appropriate, preserving the shared shell and avoiding a flash between pages. Anchor scrolling and hover effects are not evidence of a working page transition.
- Preserve deep links, browser Back/Forward, expected scroll restoration and focus after navigation. Handle rapid repeated navigation and interrupted animations; reduced motion must allow immediate usable navigation without waiting for choreography.

## First paint and loading
- Specify the first visible frame before adding entry motion: correct background, critical styles, stable image dimensions and readable font fallbacks. Fix FOUC and font/layout jumps at their source with ENGINEER; a covering animation is not a repair.
- Make an explicit preloader decision. When the experience has necessary initialization, design a brief loader around those actual resources and reveal the page as soon as it is ready. Do not force an artificial minimum delay, invent percentage progress or wait for every below-the-fold asset.
- A loader must have success, error and bounded-timeout exits, plus a usable fallback if scripts or assets fail. Avoid permanent hidden content, trapped focus and retained scroll locks. Skip unnecessary replay on warm visits; respect reduced motion and avoid announcing every animation frame to assistive technology.

## Acceptance checks
- Inspect the full page at desktop and mobile sizes: purposeful section rhythm, readable supporting text, distinct typographic roles, and no repeated decorative device without a content reason.
- Observe cold and warm entry, slow or failed critical assets, and the reduced-motion experience. Check the first frames and final layout, not only a settled screenshot.
- Exercise the menu with mouse, touch and keyboard; verify opening, closing, active links, focus restoration and interrupted states.
- Exercise actual route links, direct entry to a route, refresh, rapid navigation and Back/Forward. Report untested states instead of assuming motion and loading behavior from the source code.

## Handoff
Provide the concise design rationale and reference observations, type roles, navigation/loading decisions, checked interactions and unresolved constraints. Keep this in the normal brief or handoff rather than adding a separate design-process file for every page.
