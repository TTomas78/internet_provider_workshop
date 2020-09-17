class ResourceNotFoundException(Exception):
    """Expects an entity id to complete the message"""
    def __init__(self, entity_id):
        self.messages = 'Entity {} not found'.format(entity_id)