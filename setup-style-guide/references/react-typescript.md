# React / TypeScript Style

- Keep imports grouped in the local order: external libraries, local components, UI primitives, constants/history/hooks, libs, types, generated route/helpers.
- Use `type` imports where the repo does. Keep React type style consistent, such as `React.ReactNode` vs imported `ReactNode`.
- Prefer small inline prop types for one-off components and named types for reused/shared surfaces, matching nearby files.
- Order props by how the component reads: core data first, external data collections next, open/state controls next, callbacks/actions next, optional trigger/render/config last.
- Common component declaration flow: history/navigation helpers, fetch/query hooks, local state, form/error helpers, effects, derived values, form/table setup, handlers, selected JSX fragments, return.
- Respect hook order and JavaScript temporal dead zones. If a derived value must be declared before another hook or callback can safely use it, keep it there and use spacing to show feature groups.
- Do not introduce `useMemo`, `useCallback`, or extra helper components for style alone. Use them when the local codebase already does or when identity/performance constraints are real.
- Inline weak variables, but keep variables that name a real domain concept, narrow a type, avoid expensive work, stabilize a reference, or make a large JSX block readable.
- Short callback names are fine in tight scopes: `s`, `r`, `p`, `row`, `field`, `value`, `prev`, and `event` are acceptable when the closure makes them obvious.
- Keep JSX props on one line until it becomes hard to scan; then split one prop per line with no blank lines inside the prop list.
- At call sites, order props to mirror the component's own prop type and user-facing importance.
