from project import ma
from project.api.auth.models import Users
from marshmallow import fields


class UsersSchema(ma.ModelSchema):
    device_id = fields.Str(data_key='deviceId')
    machine_id = fields.Integer(data_key='machineId')

    class Meta:
        model = Users
        fields = ('id', 'device_id', 'machine_id')

