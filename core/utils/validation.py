import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

# 🇮🇹 Funzione per validare una risposta API contro uno schema JSON
# 🇬🇧 Function to validate an API response against a JSON schema

def validate_json_schema(response_json, schema_path):
    with open(schema_path) as f:
        schema = json.load(f)

    try:
        validate(instance=response_json, schema=schema)
        return True, None
    except ValidationError as e:
        return False, e.message
