from django.db import models

class AnaliseInvestimento(models.Model):
    projeto = models.CharField(max_length=100)
    data_implantacao = models.DateField()
    recurso_inicial = models.FloatField()
    custo_mensal = models.FloatField()
    receita_estimada = models.FloatField()
    valor_residual = models.FloatField()
    tma = models.FloatField()
    tempo_retorno = models.FloatField(null=True, blank=True)
    projeto_viavel = models.BooleanField(default=False)

    def __str__(self):
  return self.projeto