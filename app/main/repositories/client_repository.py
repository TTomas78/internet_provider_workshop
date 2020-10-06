from app.main.models import ClientModel
from app.main.exceptions import ResourceNotFoundException

class ClientRepository:

    @staticmethod
    def get_all():
        return ClientModel.query.filter(ClientModel.is_deleted.is_(False)).all()

    @staticmethod
    def get(client_id):

        client = ClientModel.query.filter(ClientModel.id == client_id, ClientModel.is_deleted.is_(False)).first()
        
        if client is None:
            raise ResourceNotFoundException(client_id)

        return client