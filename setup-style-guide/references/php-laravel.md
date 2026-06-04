# PHP / Laravel Style

- Keep framework idioms direct. Do not replace clear controller/model code with service classes, DTOs, or repositories unless the repo already uses that layer or reuse is real.
- Controller flow usually reads as: validate request, perform transaction or query, apply side effects, return model/array/resource. Keep validation arrays and payload arrays in domain/input order.
- Prefer Laravel fluent chains and collection methods when that is the local style. Keep chained query clauses grouped by concern, with relationship filters and terminal operations easy to find.
- In models, preserve local ordering such as attributes/casts/eager loads first, boot methods/scopes next, query builders next, accessors next, relationships last.
- Keep relationship methods compact and consistently ordered. Do not add temporary variables around simple Eloquent calls unless they prevent repetition or clarify a nontrivial step.
- Use short closure parameters like `$query`, `$q`, `$dto`, or local domain names when the callback scope is small and obvious.
- Keep named arguments and snake_case field names when they match the Laravel/request/database surface.
