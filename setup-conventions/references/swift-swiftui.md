# Swift / SwiftUI Style

- Typical view order: immutable identity inputs, environment/storage dependencies, repositories/services, query/mutation wrappers, local state, computed accessors, operations, `body`, extracted subviews, preview.
- Separate property-wrapper groups with spacing when they serve different features: `@Environment`, repository wrappers, fetcher wrappers, `@State`, `@Binding`.
- Service/domain type order: stored dependencies, initializer, static/computed helpers, public behavior, private helpers, then private support types.
- Let SwiftFormat shape multiline calls: one argument per line for longer calls, in declaration order.
- Use `$0` and short names in tiny closures. Name values once a closure spans multiple statements, crosses feature boundaries, or hides its type.
- Order extracted view properties/functions as they appear in `body`, so the declarations read like the render path.
- Keep `#Preview` last and shaped like nearby previews.
