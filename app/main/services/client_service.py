from app.main.repositories.client_repository import ClientRepository

class ClientService:

    @staticmethod
    def get_all():
        return ClientRepository.get_all()

    @staticmethod
    def get(client_id):
        return ClientRepository.get(client_id)
