import humps
from copy import deepcopy

def load_schemas(schema_list):
    schema_list = deepcopy(schema_list)
    new_schemas = {
        "title": "Module",
        "id": "Module",
        "type": "object",
        "definitions": {}
    }
    # A key of schema title to metadata about that class
    # - schema_id
    # - module_type
    schema_class_meta_info = {}

    # High level approach here is to

    dependency_definitions = {}

    for schema_entity in schema_list:
        schema = schema_entity["schema"]
        schema_key = schema["title"]

        if schema.get("definitions") is not None:
            dependency_definitions.update(schema["definitions"])
            del schema["definitions"]



        # For each schema we encounter, keep track of it's
        # key in the definitions and use that to map to the type of
        # module it is, and it's schema id (if applicable)
        schema_class_meta_info[schema_key] = {
            "module_type": schema_entity["module_type"],
            "schema_id": schema_entity["id"]
        }
        new_schemas["definitions"][schema_key] = schema

    for subschema_key, subschema in dependency_definitions.items():
        definition_key = humps.pascalize(subschema_key)
        future_class_name = subschema["title"]

        if new_schemas["definitions"].get(definition_key) is None:
            module_type = humps.pascalize(subschema_key.split("_")[-1])
            schema_class_meta_info[future_class_name] = {
                "module_type": module_type
            }
            if subschema.get("definitions") is not None:
                del subschema["definitions"]
            new_schemas["definitions"][definition_key] = subschema

    return (new_schemas, schema_class_meta_info)