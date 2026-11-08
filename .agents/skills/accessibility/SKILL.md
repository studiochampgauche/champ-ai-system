---
name: accessibility
description: "Accessible web design and React UI implementation following WCAG 2.2 AA, semantic HTML, keyboard, focus, forms, contrast, motion and assistive-technology behavior. Use during design, coding, review and QA."
---

# Accessibility (WCAG 2.2 AA)

## Practice
- Use semantic HTML first: links navigate, buttons act, fieldset/legend group related controls, headings form a meaningful outline.
- Ensure all interactive controls are keyboard reachable, operable and visibly focused. Manage focus for dialogs, navigation and dynamic content.
- Provide associated labels, helpful instructions, inline errors and programmatic error/status messages.
- Verify color contrast, text resizing, spacing, touch target size, layout reflow and zoom; do not rely on color alone.
- Provide meaningful alt text for informative images and empty alt for decorative ones; avoid images for textual information when possible.
- Use ARIA only where semantic HTML cannot express necessary behavior; test states and roles, don't add decorative ARIA.
- Respect `prefers-reduced-motion`; do not use movement or scroll hijacking that prevents task completion.
- Test with keyboard and automated tooling; manually verify critical flows with an actual screen reader where available.

## Definition of done
Relevant WCAG 2.2 AA criteria checked; no critical keyboard/focus blockers; deficiencies repaired and retested. Automated checks alone never prove full conformance.

Official reference: https://www.w3.org/TR/WCAG22/ and https://www.w3.org/WAI/ARIA/apg/
