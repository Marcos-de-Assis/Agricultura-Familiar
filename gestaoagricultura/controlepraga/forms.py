from django import forms
from .models import Praga

class PragaForm(forms.ModelForm):
    class Meta:
        model = Praga
        fields = ['classif_praga', 'incidencia_na_planta', 'tipo_danos', 'acao_controle', 'eficacia_acao', 'custo_control_praga']
        