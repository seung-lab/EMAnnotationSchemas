import os

import marshmallow as mm

from emannotationschemas.schemas.base import BoundSpatialPoint


def get_app_base_path():
    return os.path.dirname(os.path.realpath(__file__))


def get_instance_folder_path():
    return os.path.join(get_app_base_path(), "instance")


def get_flattened_bsp_keys_from_schema(schema):
    """Returns the flattened keys of BoundSpatialPoints in a schema

    :param schema: schema
    :return: list
    """
    keys = []

    for key in schema.declared_fields.keys():
        field = schema.declared_fields[key]

        if isinstance(field, mm.fields.Nested) and isinstance(
            field.schema, BoundSpatialPoint
        ):
            keys.append("{}.{}".format(key, "position"))

    return keys


def get_bsp_columns(Schema):
    columns = []
    for k, v in Schema._declared_fields.items():
        if isinstance(v, mm.fields.Nested):
            if isinstance(v.schema, BoundSpatialPoint):
                columns.append(k)
    return columns


def create_segmentation_table_name(table_name: str, segmentation_source: str):
    return f"{table_name}__{segmentation_source}"
