# views/user_view.py

from core.views import BaseView
from app.models import DocumentModel
from app.services import DocumentService


class DocumentView(BaseView[DocumentModel]):
    model_class = DocumentModel
    service = DocumentService()
