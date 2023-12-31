from django.urls import path
from . import views

urlpatterns = [
    # Autres chemins d'URL...
    path('ajouter_note_api/<int:pk>/', views.ajouter_note_api, name='ajouter_note_api'),
    # Autres chemins d'URL...
]
