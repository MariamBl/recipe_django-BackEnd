from django.db import models
from django.contrib.auth.models import User
from recette.models import Recette

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    valeur = models.IntegerField()
