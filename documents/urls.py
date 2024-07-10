from django.urls import path

from. views import documents
from .views import view_documents, delete_documents


urlpatterns = [
    path('documents/',documents, name='documents'),
    path("view_documents/",view_documents, name='view_documents'),
    path("delete_documents/<int:documents_id>/",delete_documents,name='delete_documents')

]
