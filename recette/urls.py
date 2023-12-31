from django.urls import path
from . import views

urlpatterns = [
    # Autres URLs de l'application
    path('api/recette/<int:pk>/', views.DetailRecetteAPIView.as_view(), name='detail-recette-api'),
    #path('api/recette/<int:pk>/ajouter_commentaire/', views.AjouterCommentaireAPIView.as_view(), name='ajouter-commentaire-api'),
    path('api/recette/<int:pk>/ajouter_note/', views.AjouterNoteAPIView.as_view(), name='ajouter-note-api'),
    path('api/commentaire/<int:pk>/ajouter_like/', views.AjouterLikeAPIView.as_view(), name='ajouter-like-api'),
    path('api/commentaire/<int:pk>/ajouter_dislike/', views.AjouterDislikeAPIView.as_view(), name='ajouter-dislike-api'),
    path('api/recettes/', views.RecetteListAPIView.as_view(), name='recette-list-api'),
    path('api/recette/creer/', views.CreerRecetteAPIView.as_view(), name='creer-recette-api'),
    path('api/recette/<int:pk>/supprimer/', views.SupprimerRecetteAPIView.as_view(), name='supprimer-recette-api'),
]
