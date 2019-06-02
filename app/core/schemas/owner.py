import uuid
import datetime

from marshmallow import Schema, fields, post_load, pre_load, post_dump


class OwnerSchemaException(Exception):
    pass


class OwnerSchema(Schema):
    id = fields.UUID(required=True)
    name = fields.Str(required=True)
    status = fields.Int(required=True)
    regDate = fields.DateTime(required=True)

    @pre_load
    def defaults(self, data):
        data['id'] = uuid.uuid1()
        data['status'] = 1
        data['regDate'] = datetime.datetime.today().isoformat()  # format ISO 8601

    @post_load
    def data_format(self, data):
        data['id'] = str(data['id'])
        data['regDate'] = str(data['regDate'])
        return data

    @post_dump
    def dump_format(self, data):
        data['regDate'] = str(datetime.datetime.strptime(data['regDate'], '%Y-%m-%dT%H:%M:%S+00:00'))
        return data
