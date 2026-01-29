# notion_assistant_contracts — Intent

This repository defines versioned JSON Schemas shared across Brain OS services.
It exists to prevent contract drift between:
- intent_normaliser
- context_api
- notion_gateway
- action_relay examples/client payloads

The `VERSION` file is the contract version expected by services.
