from django import forms
from .models import AnaliseInvestimento

class AnaliseInvestimentoForm(forms.ModelForm):
    class Meta:
        model = AnaliseInvestimento
        fields = [
            'projeto', 'data_implantacao', 'recurso_inicial', 
            'custo_mensal', 'receita_estimada', 'valor_residual', 'tma'
]
        