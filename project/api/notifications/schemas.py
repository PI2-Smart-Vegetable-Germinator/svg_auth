from project import ma

from marshmallow import fields


class DeviceIdSchema(ma.Schema):
    user_id = fields.Integer(required=True, data_key="userId")
    device_id = fields.Str(required=True, data_key="deviceId")
