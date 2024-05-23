from django import forms
from .models import CustoBeneficio

class CustoBeneficioForm(forms.ModelForm):
    class Meta:
        model = CustoBeneficio
        fields = '__all__'
