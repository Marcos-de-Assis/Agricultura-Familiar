from django.db import models

# Create your models here.
class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField()
    