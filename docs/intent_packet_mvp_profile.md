# Intent Packet: MVP Profile (Lightweight)

Status: draft (MVP)  
Last updated: 2026-02-03

## Purpose
Define the minimal intent packet shape used in MVP capture.
This is a profile of the existing v1 intent_packet schema, not a replacement.

## MVP-required fields
- kind: "intent"
- natural_language: string

## MVP-recommended fields
- schema_version: "v1"
- source: "chatgpt" | "action_relay" | "curl"
- timestamp: ISO-8601 UTC
- conversation_id: string (optional)
- message_id: string (optional)
- fields: object (optional)

## Explicitly out of scope for the intent packet (MVP)
- execution plans
- tool calls
- Notion API parameters (except as generic hints inside fields)

## Notes
- The v1 JSON schema allows additionalProperties, so schema_version is additive.
- If a strict v2 schema is introduced later, it should be added as schemas/v2/* and kept backward compatible.
