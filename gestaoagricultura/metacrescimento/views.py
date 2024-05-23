from django.shortcuts import render
from .forms import MetaProducaoForm
from .utils.calculations import calcular_meta_producao

def meta_producao(request):
    if request.method == 'POST':
        form = MetaProducaoForm(request.POST)
        if form.is_valid():
            produtividade = form.cleaned_data['produtividade']
            area = form.cleaned_data['area']
            preco_venda = form.cleaned_data['preco_venda']
            resultado = calcular_meta_producao(produtividade, area, preco_venda)
            return render(request, 'meta_producao_result.html', {'resultado': resultado})
    else:
        form = MetaProducaoForm()
    return render(request, 'meta_producao.html', {'form': form})