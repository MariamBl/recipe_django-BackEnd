from django import forms
from .models import Recette


class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ('nom', 'description', 'image', 'temps_preparation', 'temps_cuisson', 'personnes',  )
        widgets = {
            'ingredients': forms.Textarea(attrs={'rows': 5}),
            'etapes': forms.Textarea(attrs={'rows': 10}),
        }
