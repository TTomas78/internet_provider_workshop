from flask import request
from flask_restplus import Namespace
from flask_restplus import Resource
from app.main.models import ClientModel
from app.main.schemas import ClientModelSchema
from app.main.exceptions import ResourceNotFoundException
from flask_restplus import fields
from flask_restplus import Namespace
from app.main import db
from marshmallow.exceptions import ValidationError

api = Namespace('Clients', description='clients related operations', path='/')

client = api.model('client',{
    'dni': fields.String(description='Client dni', example='36598654'),
    'first_name': fields.String(description='Client first name', example='Pedro'),
    'last_name': fields.String(description='Client last name', example='Asdf'),
    'phone': fields.Integer(description='Client phone', example='+542316548')
})

@api.route('/clients')
class ClientResourceList(Resource):
    @api.doc('get_all_tests')
    def get(self):
        """List all clients"""
        clients = ClientModel.query.all()
        clients = ClientModelSchema().dump(clients, many=True)
        
        return clients, 200

    @api.doc('post_client')
    @api.expect(client)
    def post(self):

        client_schema = ClientModelSchema()
        client = None

        try:
            client = client_schema.load(api.payload)
            db.session.add(client)
            db.session.commit()
            client = client_schema.dump(client)

        except ValidationError as error:
            return error.messages, 400

        return client,201

@api.route('/clients/<int:client_id>')
class ClientResource(Resource):
    @api.doc('get_all_tests')
    def get(self, client_id):
        """Get a specific client"""
        client = None

        try:
            client = ClientModel.query.get(client_id)
        
            if client is None:
                raise ResourceNotFoundException(client_id)

        except ResourceNotFoundException as error:
            return error.messages, 404

        client = ClientModelSchema().dump(client)

        return client, 200
