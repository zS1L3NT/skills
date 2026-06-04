# Swift / SwiftUI Style

- Preserve the strong declaration order found in nearby files. Typical SwiftUI view order: immutable identity inputs, environment/storage dependencies, repositories/services, query/mutation wrappers, local state, computed accessors, operations, `body`, extracted subviews, preview.
- Keep property-wrapper/dependency groups visually separated when they serve different features: `@Environment`, repository wrappers, fetcher wrappers, `@State`, `@Binding`, etc.
- In service/domain types, prefer stored dependencies first, initializer immediately after stored state, static/computed helpers before behavior, public behavior before private helpers, private support types after the main public surface.
- Let SwiftFormat shape multiline calls. Prefer one argument per line for longer calls and keep argument order aligned with initializer/function declaration order.
- Use `$0` and short local names in tiny closures. Name values when the closure spans multiple statements, crosses feature boundaries, or the type is not obvious.
- Keep extracted view properties/functions in the same order they appear in `body` so scanning the render path and the declarations feels linear.
- Keep `#Preview` last and structured like nearby previews.
