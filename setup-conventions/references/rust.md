# Rust Style

- Modules are style. Follow the local pattern for `mod` declarations, private support files, `use`, `pub use`, core types, impl blocks, trait impls, and tests, including how implementation chunks split across neighboring files.
- Group struct fields by role and make constructors mirror the same grouping and spacing.
- Group function locals by purpose: accumulators, core inputs, derived masks/sets/state, then per-branch temporaries, in dependency order.
- Short names suit tight algorithmic scopes (`r`, `p`, `i`, `j`, `sq`, `rank`, `file`, closure arguments). Use domain names once a value escapes the small scope.
- Use early returns for special cases when they remove nesting and match the local algorithm style.
- Put `#[cfg(test)] mod tests` last, keeping nested test modules where scenarios group by behavior.
