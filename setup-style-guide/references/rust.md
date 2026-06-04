# Rust Style

- Treat modules as style. Follow the local pattern for `mod` declarations, private support files, `use`, `pub use`, core type declarations, impl blocks, trait impls, and tests.
- Keep focused implementation chunks in neighboring module files when the repo already splits them that way. Do not merge/split modules casually.
- Group struct fields by role and make constructors mirror the same grouping and spacing.
- In functions, group locals by purpose: accumulators, core inputs, derived masks/sets/state, then per-branch temporaries. Preserve dependency order when values build on each other.
- Short names are acceptable for tight algorithmic scopes, especially `r`, `p`, `i`, `j`, `sq`, `rank`, `file`, and closure arguments. Use domain names when the value escapes the small scope.
- Keep early returns for special cases when they remove nesting and match the local algorithm style.
- Put `#[cfg(test)] mod tests` last. Keep nested test modules when scenarios are grouped by behavior.
