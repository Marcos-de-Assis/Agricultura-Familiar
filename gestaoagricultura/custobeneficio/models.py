from django.db import models

# Create your models here.
class Projeto(models.Model):
class CustoBeneficio(models.Model):
    produtividade = models.FloatField(verbose_name="Produtividade (kg/ha)")
    area = models.FloatField(verbose_name="Área (ha)")
    preco_venda = models.FloatField(verbose_name="Preço de Venda (R$/kg)")
    custo_producao = models.FloatField(verbose_name="Custo de Produção (R$/ha)")
    custo_fixo = models.FloatField(verbose_name="Custo Fixo (R$/ha)")
    custo_variavel = models.FloatField(verbose_name="Custo Variável (R$/ha)")
    custo_oportunidade = models.FloatField(verbose_name="Custo de Oportunidade (R$/ha)")

    def __str__(self):
        return f"Custo Benefício - {self.id}"

    @property
    def receita(self):
        return self.produtividade * self.area * self.preco_venda

    @property
    def custo_total(self):
        return self.custo_producao + self.custo_fixo + self.custo_variavel + self.custo_oportunidade

    @property
    def beneficio(self):
        return self.receita - self.custo_total
    