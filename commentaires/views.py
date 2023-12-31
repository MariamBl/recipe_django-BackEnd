from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .forms import CommentaireForm
from .models import Commentaire
from .serializer import CommentaireSerializer
from recette.models import Recette
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ajouter_commentaire_api(request, pk):
    recette = get_object_or_404(Recette, pk=pk)

    if request.method == 'POST':
        form = CommentaireForm(request.data)

        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.recette = recette
            commentaire.user = request.user
            commentaire.save()

            serializer = CommentaireSerializer(commentaire)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
