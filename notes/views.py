from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .forms import NoteForm
from .models import Note
from recette.models import Recette
from .serializer import NoteSerializer  # Ajouter cette ligne si besoin

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ajouter_note_api(request, pk):
    recette = get_object_or_404(Recette, pk=pk)

    if request.method == 'POST':
        form = NoteForm(request.data)

        if form.is_valid():
            note = form.save(commit=False)
            note.recette = recette
            note.user = request.user
            note.save()

            serializer = NoteSerializer(note)  # Utiliser le serializer pour renvoyer les données de la note ajoutée
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
