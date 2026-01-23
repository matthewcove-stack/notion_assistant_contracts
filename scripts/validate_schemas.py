"""Validate JSON schemas and examples.

Requires: pip install jsonschema
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError as exc:
    print("jsonschema is required: pip install jsonschema", file=sys.stderr)
    raise SystemExit(2) from exc


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    schemas_dir = root / "schemas" / "v1"
    examples_dir = root / "examples"

    schemas = {}
    errors = []

    for schema_path in sorted(schemas_dir.glob("*.schema.json")):
        schema = load_json(schema_path)
        try:
            Draft202012Validator.check_schema(schema)
        except Exception as exc:
            errors.append(f"Schema invalid: {schema_path.name}: {exc}")
        schema_name = schema_path.name[: -len(".schema.json")]
        schemas[schema_name] = schema

    for example_path in sorted(examples_dir.glob("*.json")):
        prefix = example_path.name.split(".", 1)[0]
        schema = schemas.get(prefix)
        if not schema:
            errors.append(
                f"Example has no matching schema: {example_path.name} (expected {prefix}.schema.json)"
            )
            continue
        instance = load_json(example_path)
        validator = Draft202012Validator(schema)
        for err in validator.iter_errors(instance):
            errors.append(f"Example invalid: {example_path.name}: {err.message}")

    if errors:
        for err in errors:
            print(err, file=sys.stderr)
        return 1

    print("Schemas and examples are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
