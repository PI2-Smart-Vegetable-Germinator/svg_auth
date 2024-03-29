from project import ma
from .models import Users
from marshmallow import fields
from marshmallow import validate


class SignupSchema(ma.ModelSchema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=[validate.Length(min=6, max=255)])
    device_id = fields.Str(data_key='deviceId')

    class Meta:
        model = Users
