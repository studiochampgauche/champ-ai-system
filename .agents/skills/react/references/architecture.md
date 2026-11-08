# React Architecture and Data Boundaries

## Choose architecture to fit the existing project
- Inspect the repository before choosing a folder structure. Feature-centric modules often work well for growing applications, but do not impose them on a stable repository without need.
- For a new small application, keep editable HTML, JavaScript/JSX, styles and assets in `project/src/`, with generated deployable output in `project/dist/`. Create components, routes, service or feature modules as real behavior needs them; do not pre-create empty `features/`, `shared/`, database or connector layers.
- Domain rules and permission checks belong on a trusted server. UI-level guards improve UX but never replace server authorization.
- Prefer explicit props and component composition before introducing context or a global store. If context is needed, keep its scope tight.
- Separate domain model and API DTOs. Validate externally received data at trust boundaries; static TypeScript types are not runtime validation.
- For complex forms, select the project's existing library and schema validation; verify server validation independently.

## Source-to-dist delivery
- New web products use a React SPA with a persistent shell and standalone client routing. Use ordinary JavaScript or JSX with native CSS, and add other runtime dependencies only for required behavior.
- Keep the editable shell at `project/src/index.html` with application code, styles and assets under `src/`. Group pass-through files in `project/src/public/` only when useful, then copy them into the release output; do not create a second source tree at `project/public/`. `dist/` is generated and must not become a second editable source tree.
- Add esbuild as a development dependency and call its build API from a small Node script. Bundle the React application and its imports, transform JSX when used, minify production JS/CSS, and produce browser-compatible files in `dist/`. Keep React and React DOM compatible and avoid duplicate React instances. Retain the package lock.
- Handle HTML and assets explicitly: esbuild does not bundle HTML by itself. Copy/process the source HTML to reference the emitted JS/CSS, including filenames from build metadata when hashing is used. Copy only required pass-through files and preserve asset attribution. Clean only the verified generated output directory before production builds so stale files do not leak into a release.
- Define `npm run dev`, `npm run build` and `npm run preview` in `project/package.json`. Development should rebuild the relevant sources and assets; production builds create minified output; preview serves that exact output without a development-only transform. Use Node built-ins for the small scripts/server where needed; do not construct a custom bundler or framework.
- Serve and deploy `dist/`, never the repository, `src/` or all of `node_modules/`. Keep server-only code and credentials outside the public output. Configure a fallback to `index.html` for real HTML navigation requests; missing assets and API requests must return their proper responses, not the SPA shell.
- Test direct route entry, reload, Back/Forward, subpath asset URLs if supported, and unknown routes against the release preview. Confirm that no runtime compiler, unbundled JSX/CommonJS or implicit external CDN is required.
- For an existing or explicitly requested no-build project, preserve that contract: browser modules need compatible distributions, and import maps resolve URLs without transforming JSX or CommonJS. Do not migrate it solely to match the new-project default.

## State ownership
1. Local UI state: controls, tabs, dialog visibility, input composition.
2. URL state: filters, paging, search state that should be shareable/bookmarkable; use router APIs.
3. Server state: remote entities, async loading, caching/invalidation; use an explicit fetch/data layer or the established framework/query APIs when already present.
4. Shared domain state: only when legitimately shared; avoid caches maintained in two places.

## Routing and existing server-rendered applications
- New products use client routing within the SPA shell. Standalone React Router does not imply adopting its framework mode or a Vite starter.
- For an existing project, check whether the app is SPA, SSR, SSG or RSC-enabled and preserve its architecture unless migration is authorized. Do not invent server components in a client-only application or introduce a framework to obtain them without authorization.
- Avoid browser-only globals during server render. Keep server and client behavior consistent to prevent hydration errors.
- If rendering HTML on the server, check page metadata, route semantics and canonical URLs.
- Preserve routing behavior, deep links, error boundaries and browser history.
- Avoid fetching the same data on server and client accidentally, unless it serves a real requirement.

## Layout and animations
- Prefer CSS for simple state transitions and reduced-motion support; use GSAP when timelines, scroll coordination or complex choreography justify it.
- For interactive animation in React, refer to the official `gsap-react` skill and `@gsap/react` best practices.

## References
- [esbuild setup](https://esbuild.github.io/getting-started/)
- [esbuild build API](https://esbuild.github.io/api/)
- [React Router declarative routing](https://reactrouter.com/start/declarative/routing)
- [React without JSX](https://react.dev/reference/react/createElement)
- [Browser import maps](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap)
