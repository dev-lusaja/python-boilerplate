from marshmallow import Schema, fields


class HealthSchemaException(Exception):
    pass


class HealthSchema(Schema):
    status = fields.Str(required=True)
