from flask import request
from flask_restplus import Namespace
from flask_restplus import Resource
from app.main.models import ClientModel
from app.main.schemas import ClientModelSchema
from app.main.exceptions import ResourceNotFoundException
from app.main.exceptions import ResourceAlreadyExistsException
from flask_restplus import fields
from flask_restplus import Namespace
from app.main import db
from app.main import ResponseService
from app.main.services.client_service import ClientService
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

        clients = ClientService.get_all()
        clients = ClientModelSchema().dump(clients, many=True)
        
        return ResponseService.response(clients), 200

    @api.doc('post_client')
    @api.expect(client)
    def post(self):
        """Create a new client"""

        client_schema = ClientModelSchema()
        client = None

        try:
            client = client_schema.load(api.payload)
            db.session.add(client)
            db.session.commit()
            client = client_schema.dump(client)

        except ValidationError as error:
            return error.messages, 400

        return ResponseService.response(client),201

@api.route('/clients/<int:client_id>')
class ClientResource(Resource):
    @api.doc('get_all_tests')
    def get(self, client_id):
        """Get an specific client"""

        client = None

        try:

            client = ClientService.get(client_id)

        except ResourceNotFoundException as error:
            ResponseService.add_messages(error.messages)
            return ResponseService.response(), 404

        client = ClientModelSchema().dump(client)

        return ResponseService.response(client), 200


    @api.doc('put_client')
    @api.expect(client)
    def put(self, client_id):
        """Modify an specific client"""

        client = None

        client_schema = ClientModelSchema()

        try:
            client = ClientModel.query.filter(ClientModel.id == client_id, ClientModel.is_deleted.is_(False)).first()

            if client is None:
                raise ResourceNotFoundException(client_id)
            
            client = client_schema.load(api.payload, instance=client)
            
            db.session.commit()

        except ResourceNotFoundException as error:
            ResponseService.add_messages(error.messages)
            return ResponseService.response(), 404

        client = ClientModelSchema().dump(client)

        return ResponseService.response(client), 200


    @api.doc('delete_client')
    def delete(self, client_id):
        """Delete an specific client"""

        client = None

        try:
            client = ClientModel.query.filter(ClientModel.id == client_id, ClientModel.is_deleted.is_(False)).first()

            if client is None:
                raise ResourceNotFoundException(client_id)
            
            client.is_deleted = True

            db.session.commit()

        except ResourceNotFoundException as error:
            ResponseService.add_messages(error.messages)
            return ResponseService.response(), 404

        return ResponseService.response(), 200