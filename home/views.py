from django.shortcuts import render
from recette.models import Recette
from notes.models import Note
from django.db.models import Avg


def home(request):
    recettes = Recette.objects.annotate(note_moyenne=Avg('note__valeur')).order_by('-note_moyenne')[:3]
    context = {
        'recettes': recettes
    }
    return render(request, 'home_page.html', context)
