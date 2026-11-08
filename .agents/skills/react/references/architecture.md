# React Architecture and Data Boundaries

## Choose architecture to fit the existing project
- Inspect the repository before choosing a folder structure. Feature-centric modules often work well for growing applications, but do not impose them on a stable repository without need.
- Suggested conceptual boundaries: `app/` for composition/routing, `features/` for domain flows, `shared/ui/` for reusable visual primitives, `shared/lib/` for isolated utilities, `services/` or query modules for API access. Adapt names to the existing architecture.
- Domain rules and permission checks belong on a trusted server. UI-level guards improve UX but never replace server authorization.
- Prefer explicit props and component composition before introducing context or a global store. If context is needed, keep its scope tight.
- Separate domain model and API DTOs. Validate externally received data at trust boundaries; static TypeScript types are not runtime validation.
- For complex forms, select the project's existing library and schema validation; verify server validation independently.

## State ownership
1. Local UI state: controls, tabs, dialog visibility, input composition.
2. URL state: filters, paging, search state that should be shareable/bookmarkable; use router APIs.
3. Server state: remote entities, async loading, caching/invalidation; use framework loaders/actions or existing query layer.
4. Shared domain state: only when legitimately shared; avoid caches maintained in two places.

## SSR/RSC, routing and hydration
- Check whether app is SPA, SSR, SSG or RSC-enabled. Do not invent server components in a client-only Vite app.
- Avoid browser-only globals during server render. Keep server and client behavior consistent to prevent hydration errors.
- If rendering HTML on the server, check page metadata, route semantics and canonical URLs.
- Preserve routing behavior, deep links, error boundaries and browser history.
- Avoid fetching the same data on server and client accidentally, unless it serves a real requirement.

## Layout and animations
- Prefer CSS for simple state transitions and reduced-motion support; use GSAP when timelines, scroll coordination or complex choreography justify it.
- For interactive animation in React, refer to the official `gsap-react` skill and `@gsap/react` best practices.
