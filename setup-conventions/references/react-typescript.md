# React / TypeScript Style

- Group imports in the local order: external libraries, local components, UI primitives, constants/history/hooks, libs, types, generated routes/helpers.
- Use `type` imports where the repo does, and match its React type style (`React.ReactNode` vs imported `ReactNode`).
- Use small inline prop types for one-off components and named types for reused/shared surfaces, matching nearby files.
- Order props by how the component reads: core data, external data collections, open/state controls, callbacks/actions, then optional trigger/render/config.
- Common component flow: history/navigation helpers, fetch/query hooks, local state, form/error helpers, effects, derived values, form/table setup, handlers, selected JSX fragments, return.
- Reach for `useMemo`, `useCallback`, and extra helper components only when the codebase already does or identity/performance constraints are real.
- A variable holding a JSX fragment earns its place when it makes a large return readable.
- Short callback names suit tight scopes: `s`, `r`, `p`, `row`, `field`, `value`, `prev`, `event`.
