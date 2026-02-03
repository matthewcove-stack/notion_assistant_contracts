# notion_assistant_contracts — Current State (Authoritative for this repo)

## What works today
- Schemas under `schemas/v1/`
- Examples under `examples/`
- Schema validation script: `python scripts/validate_schemas.py`
- `VERSION` file exists as version tag

## Phase 1 contract requirements
For Phase 1, the following must be stable and used everywhere:
- Intent packet shape(s) for task creation/update
- Action plan representation (if used)
- Gateway request/response payload shapes for tasks create/update
- Intent response status values, including `executed` and `failed` when actions run

If Phase 1 requires changes:
- Introduce a new schema revision under `schemas/v1/` (or bump to v2 if breaking)
- Update examples
- Bump `VERSION`
- Update dependent services accordingly

## Phase 1 scope (exact)

Goal: a single end-to-end vertical slice that reliably turns a natural-language intent into a Notion Task create/update, with an audit trail.

In scope:
- Submit intent (via action_relay client or curl) to intent_normaliser `POST /v1/intents`.
- intent_normaliser normalises into a deterministic plan (`notion.tasks.create` or `notion.tasks.update`).
- If `EXECUTE_ACTIONS=true` and confidence >= threshold, intent_normaliser executes the plan by calling notion_gateway:
  - `POST /v1/notion/tasks/create` or `POST /v1/notion/tasks/update`
- Write artifacts for: received → normalised → executed (or failed) with stable IDs.
- Idempotency: duplicate submissions with the same `request_id` (or generated deterministic key) must not create duplicate Notion tasks.
- Error handling: gateway errors are surfaced in the response and recorded as artifacts.
- Minimal context lookups:
  - Optional: query context_api for project/task hints when provided, but Phase 1 must still work without context_api being “perfect”.

Out of scope (Phase 2+):
- UI for clarifications (API-only is fine).
- Calendar events / reminders.
- Full automated background sync from Notion.
- Multi-user, permissions, or “agents” beyond single operator.


## Verification commands
- `python scripts/validate_schemas.py`
