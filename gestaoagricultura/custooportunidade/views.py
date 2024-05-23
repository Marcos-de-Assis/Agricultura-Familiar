from django.shortcuts import render
from .forms import CustoOportunidadeForm
from .utils.calculations import calcular_custo_oportunidade

def custo_oportunidade(request):
    if request.method == 'POST':
        form = CustoOportunidadeForm(request.POST)
        if form.is_valid():
            retorno_alternativo = form.cleaned_data['retorno_alternativo']
            retorno_atual = form.cleaned_data['retorno_atual']
            resultado = calcular_custo_oportunidade(retorno_alternativo, retorno_atual)
            return render(request, 'custo_oportunidade_result.html', {'resultado': resultado})
    else:
        form = CustoOportunidadeForm()
    return render(request, 'custo_oportunidade.html',
                  