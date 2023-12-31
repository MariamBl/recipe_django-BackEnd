from django.db import models
from django.contrib.auth.models import User

class Recette(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    temps_preparation = models.IntegerField()
    temps_cuisson = models.IntegerField()
    personnes = models.IntegerField()
    image = models.CharField(max_length=100)
