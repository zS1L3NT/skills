# PHP / Laravel Style

- Keep framework idioms direct. Controller and model code stays in place; service classes, DTOs, and repositories appear only where the repo already has that layer or reuse is real.
- Controller flow: validate request, run the transaction or query, apply side effects, return model/array/resource. Validation and payload arrays follow domain/input order.
- Use fluent chains and collection methods where that is the local style. Group chained query clauses by concern so relationship filters and terminal operations are easy to find.
- Model order: attributes/casts/eager loads, boot methods/scopes, query builders, accessors, then relationships.
- Keep relationship methods compact and consistently ordered, and simple Eloquent calls free of temporary variables.
- Short closure parameters (`$query`, `$q`, `$dto`, local domain names) suit small, obvious callbacks.
- Keep named arguments and snake_case field names where they match the Laravel/request/database surface.
