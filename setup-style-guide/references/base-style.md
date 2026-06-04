# Code Style

## Core Rules

Make code justify its existence. Prefer the style already proven in the local area, and preserve behavior unless a behavior change is explicit.

Inspect nearby code before deciding what "clean" means:

- Equivalent files: sibling components/controllers/hooks/helpers/classes/modules, similar pages/screens, existing shared utilities, and current imports/types.
- Current usage: call sites, parameters/props passed by callers, helpers consumed downstream, tests or build checks that cover the area.
- Declaration order: how the local code orders injected dependencies, property wrappers/decorators/attributes, constants, stored fields, state, computed values, constructors, lifecycle methods, actions, render/body methods, helpers, nested types, and tests.

## Reason For Being There

Every line needs a reason:

- Delete code, props, branches, imports, wrappers, and helpers that do not carry real behavior, clarity, reuse, or constraint.
- Do not add abstractions for one-off logic.
- Keep code scoped to the file/component unless there is meaningful reuse or the repo already has a matching shared pattern.
- Do not pad simple logic with defensive abstractions or line-heavy rewrites.

Comments count as code with intent. Preserve comments by default when they record rationale, workflow notes, constraints, temporary options, domain caveats, or non-obvious positioning. Remove comments only when they are clearly stale, misleading, or pure boilerplate with no useful signal.

## Physical Grouping

Keep related code physically nearby:

- Group variables, callbacks, derived values, effects, handlers, JSX/render blocks, and helper functions by feature or responsibility.
- Use spacing to make those groups obvious.
- Order declarations by dependency and reading flow where the language allows it: inputs first, derived values next, actions next, rendering data last.
- Avoid long mixed lists where unrelated feature state, formatting values, handlers, and config sit together.

Treat declaration order as a first-class convention:

- Learn the order from nearby files before changing it.
- Keep equivalent declarations in the same relative order across the file, folder, and project.
- Preserve strong layer patterns, such as identity/core inputs before dependencies, dependencies before state, state before derived values, derived values before operations, primary entry points before extracted helpers, and private/nested support types after the public surface when that is how the local code reads.
- Respect hard ordering constraints: declarations may need to move earlier because of JavaScript temporal dead zones, hook/lifecycle rules, type inference, initialization order, dependency injection, visibility, or language-specific compile rules. When exact ordering is impossible, use the closest valid order and spacing/grouping to show the intended distinctions.
- Keep framework-specific groups together: annotations/decorators/property wrappers, dependency injection, request validation, query/mutation state, lifecycle hooks, render/body output, route handlers, tests, and helper methods should not be interleaved casually.

## Variables And Names

Remove weak variables:

- Inline variables that only rename a short expression, are used once, or add more scope clutter than clarity.
- It is acceptable to repeat a harmless expression two or three times when that keeps the code tighter and clearer.
- Keep a variable when it prevents duplicated expensive work, preserves referential stability, captures a side effect safely, enables type narrowing, names a genuinely important concept, or removes meaningful noise.

Make names compact but complete:

- Prefer one-word names when the meaning stays clear in context.
- Use longer names only when the missing detail would make the code ambiguous.
- Accept short local names such as `data`, `item`, `value`, `result`, `props`, `p`, `r`, or `x` when the small scope makes the meaning obvious, especially in closures, maps, filters, reducers, and tiny helpers.
- Rename vague names only when the surrounding context does not already identify the concept.
- Do not rename into cleverness. The next reader should not need to decode style.

## APIs, Arguments, And Props

Treat interfaces, parameters, and props as part of the style surface:

- Define only fields, constructor parameters, function parameters, props, request values, and options that are actually needed.
- Keep names, types, and ordering consistent with equivalent local APIs.
- Order definitions by importance and usage, usually identity/core data first, dependencies next, behavior callbacks/actions next, presentation/config/options last.
- Order call-site arguments, named parameters, object fields, JSX props, request payloads, and test data to match the callee's conceptual order.
- Keep argument/prop/field lists on one line when readable; split one item per line only when necessary for length, formatter rules, or clarity.
- Do not insert blank lines inside a single argument/prop/field list.

## Consistency

Maintain repo-wide consistency for recurring choices:

- Import style, type style, class/struct/function layout, hook/lifecycle placement, component/controller/service export shape, route/helper usage, and UI/API composition should match the dominant nearby pattern.
- File/module boundaries are style too: keep focused support code in the same file or neighboring module pattern the repo already uses, and do not merge/split files casually.
- If a repo is inconsistent, follow the local folder/file pattern unless a broader convention pass is explicit.
- Do not change a shared convention across many files without calling out the scope first.
