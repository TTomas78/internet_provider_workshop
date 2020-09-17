from flask_restplus import fields
from flask_restplus import Namespace

api = Namespace('Clients', description='clients related operations', path='/')

client = api.model('client',{
    'dni': fields.String(description='Client dni', example='36598654'),
    'first_name': fields.String(description='Client first name', example='Pedro'),
    'last_name': fields.String(description='Client last name', example='Asdf'),
    'phone': fields.Integer(description='Client phone', example='+542316548')
})