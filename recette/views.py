from django.shortcuts import render, get_object_or_404,redirect
from recette.models import Recette
from etapes.models import Etape
from notes.models import Note
from commentaires.models import Commentaire
from django.db import models
from notes.forms import NoteForm
from django.contrib.auth.decorators import login_required
from commentaires.forms import CommentaireForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import RecetteForm
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recette
from .serializer import RecetteSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg

class DetailRecetteAPIView(APIView):
    def get(self, request, pk):
        recette = get_object_or_404(Recette, pk=pk)
        serializer = RecetteSerializer(recette)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class AjouterCommentaireAPIView(APIView):
#     def post(self, request, pk):
#         recette = get_object_or_404(Recette, pk=pk)
#         contenu = request.data.get('contenu')  # Assurez-vous que le contenu est fourni dans les données POST
#         if contenu:
#             commentaire = Commentaire.objects.create(recette=recette, contenu=contenu)
#             return Response({'success': 'Commentaire ajouté avec succès'}, status=status.HTTP_201_CREATED)
#         return Response({'error': 'Le contenu du commentaire est requis'}, status=status.HTTP_400_BAD_REQUEST)

class AjouterNoteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        recette = get_object_or_404(Recette, pk=pk)
        form = NoteForm(request.data)
        
        if form.is_valid():
            note = form.save(commit=False)
            note.recette = recette
            note.user = request.user  # Assurez-vous que la note est associée à l'utilisateur authentifié
            note.save()
            return Response({'success': 'Note ajoutée avec succès'}, status=status.HTTP_201_CREATED)
        
        return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

# class DetailRecetteAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, pk):
#         recette = get_object_or_404(Recette, pk=pk)
#         etapes = Etape.objects.filter(recette=recette).order_by('ordre')
#         note_moyenne = Note.objects.filter(recette=recette).aggregate(Avg('valeur'))['valeur__avg']

#         context = {
#             'recette': recette,
#             'etapes': etapes,
#             'note_moyenne': note_moyenne,
#         }

#         return Response(context, status=status.HTTP_200_OK)
class AjouterLikeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        commentaire = get_object_or_404(Commentaire, pk=pk)
        commentaire.likes += 1
        commentaire.save()
        return Response({'success': 'Le commentaire a été liké avec succès'}, status=status.HTTP_200_OK)

class AjouterDislikeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        commentaire = get_object_or_404(Commentaire, pk=pk)
        commentaire.dislikes += 1
        commentaire.save()
        return Response({'success': 'Le commentaire a été disliké avec succès'}, status=status.HTTP_200_OK)

class RecetteListAPIView(APIView):
    def get(self, request):
        recettes = Recette.objects.all()
        serializer = RecetteSerializer(recettes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreerRecetteAPIView(APIView):
    def post(self, request):
        serializer = RecetteSerializer(data=request.data)
        if serializer.is_valid():
            recette = serializer.save(auteur=request.user)
            return Response({'success': 'Recette créée avec succès', 'id': recette.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SupprimerRecetteAPIView(APIView):
    def delete(self, request, pk):
        recette = get_object_or_404(Recette, pk=pk)
        if request.user == recette.auteur:
            recette.delete()
            return Response({'success': 'Recette supprimée avec succès'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Vous n\'êtes pas autorisé à supprimer cette recette'}, status=status.HTTP_403_FORBIDDEN)
