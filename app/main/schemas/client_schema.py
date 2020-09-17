from marshmallow import fields, pre_dump, ValidationError
from app.main.models import ClientModel
from app.main.schemas import BaseSchema



class ClientModelSchema(BaseSchema):

    dni = fields.Integer()

    class Meta(BaseSchema):
        model = ClientModel
        fields = (
                    'id',
                    'dni',
                    'first_name',
                    'last_name',
                    'phone',
        )
