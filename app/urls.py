from django.urls import path
from app.views import DocumentView

urlpatterns = [
    path('documents/', DocumentView.as_view(), name='document_create_getall'),
    path('document/<str:pk>/', DocumentView.as_view(), name='document_retrieve_update'),
]
