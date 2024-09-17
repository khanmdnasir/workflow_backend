import json

from core.services import BaseService
from app.models import DocumentModel


class DocumentService(BaseService[DocumentModel]):
    def __init__(self):
        super().__init__('documents')

    def pre_modification(self, request):
        """Override this method to modify request data before validation"""
        # Example: Add a new field or modify existing ones
        data = {
            "nodes": json.dumps(request.data.get('nodes', [])),
            "edges": json.dumps(request.data.get('edges', [])),
            "name": request.data.get('name'),
            "user_id": request.user.id
        }
        return data

    def post_modification(self, data: dict) -> dict:
        """Override this method to modify request data before validation"""
        # Example: Add a new field or modify existing ones
        data['nodes'] = json.loads(data.get('nodes', ''))
        data['edges'] = json.loads(data.get('edges', ''))
        return data
