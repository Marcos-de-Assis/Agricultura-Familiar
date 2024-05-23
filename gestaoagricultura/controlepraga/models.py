from django.db import models
from django.contrib.auth.models import User

class ControlePraga(models.Model):
    produtor = models.ForeignKey(User, on_delete=models.CASCADE)
    classif_praga = models.CharField(max_length=100)
    incidencia_na_planta = models.IntegerField()
    tipo_danos = models.CharField(max_length=100)
    acao_controle = models.CharField(max_length=200)
    eficacia_acao = models.CharField(max_length=100)
    custo_control_praga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
    return self.classif_praga