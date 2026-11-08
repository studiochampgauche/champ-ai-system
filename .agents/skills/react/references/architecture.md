# React Architecture and Data Boundaries

## Choose architecture to fit the existing project
- Inspect the repository before choosing a folder structure. Feature-centric modules often work well for growing applications, but do not impose them on a stable repository without need.
- For a new small application, begin with its entry point, components, styles and assets. Create routing, service or feature modules as real behavior needs them; do not pre-create empty `features/`, `shared/`, database or connector layers.
- Domain rules and permission checks belong on a trusted server. UI-level guards improve UX but never replace server authorization.
- Prefer explicit props and component composition before introducing context or a global store. If context is needed, keep its scope tight.
- Separate domain model and API DTOs. Validate externally received data at trust boundaries; static TypeScript types are not runtime validation.
- For complex forms, select the project's existing library and schema validation; verify server validation independently.

## Browser module delivery without a bundler
- Native browser modules execute JavaScript, not JSX. Use `createElement` or an already authorized transform; do not add an in-browser compiler or invent a build system to preserve JSX syntax.
- Check the selected packages' exports and distribution formats before designing imports. A CommonJS npm entry cannot be served directly as an ES module. Import maps map specifiers to module URLs; they perform no transpilation or package conversion.
- Select verified browser-compatible modules and pin their versions. Check transitive imports and keep React/React DOM compatible with one shared React instance. Prefer locally served assets where compatible artifacts are available; preserve attribution and record their origin.
- A runtime CDN adds an external availability and security dependency. Do not choose one implicitly to make a no-bundler setup work. Verify any approved remote delivery against CSP, CORS, caching and the deployment's offline/privacy requirements.
- If a required package has no suitable distribution within the permitted stack, explain the concrete incompatibility and ask for an explicit exception or alternative. Do not claim that copying `node_modules/` or adding an import map solves it.
- Verify first load and direct navigation on the actual server: MIME types, module URLs, dependency resolution and route fallback must work without a development tool providing hidden behavior. Keep a static server's public root explicit; do not expose the repository or all of `node_modules/`.

## State ownership
1. Local UI state: controls, tabs, dialog visibility, input composition.
2. URL state: filters, paging, search state that should be shareable/bookmarkable; use router APIs.
3. Server state: remote entities, async loading, caching/invalidation; use an explicit fetch/data layer or the established framework/query APIs when already present.
4. Shared domain state: only when legitimately shared; avoid caches maintained in two places.

## SSR/RSC, routing and hydration
- Check whether the app is SPA, SSR, SSG or RSC-enabled. Do not invent server components in a client-only application or introduce a framework to obtain them without authorization.
- Avoid browser-only globals during server render. Keep server and client behavior consistent to prevent hydration errors.
- If rendering HTML on the server, check page metadata, route semantics and canonical URLs.
- Preserve routing behavior, deep links, error boundaries and browser history.
- Avoid fetching the same data on server and client accidentally, unless it serves a real requirement.

## Layout and animations
- Prefer CSS for simple state transitions and reduced-motion support; use GSAP when timelines, scroll coordination or complex choreography justify it.
- For interactive animation in React, refer to the official `gsap-react` skill and `@gsap/react` best practices.

## References
- [React without JSX](https://react.dev/reference/react/createElement)
- [Browser import maps](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap)
