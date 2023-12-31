from django.db import models
from recette.models import Recette
from recette.models import Recette
class Etape(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    ordre = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return f"Etape {self.ordre} de la recette {self.recette}"