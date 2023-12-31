from rest_framework import serializers
from .models import Recette
from commentaires.models import Commentaire

class RecetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recette
        fields = ['id', 'nom', 'description', 'temps_preparation', 'temps_cuisson', 'personnes', 'image']

class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = ['id', 'user', 'recette', 'contenu', 'date', 'likes', 'dislikes']




