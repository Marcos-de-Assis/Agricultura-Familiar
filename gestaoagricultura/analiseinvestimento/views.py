from django.shortcuts import render, redirect
from .forms import AnaliseInvestimentoForm
from .models import AnaliseInvestimento

def analise_investimento(request):
    if request.method == 'POST':
        form = AnaliseInvestimentoForm(request.POST)
        if form.is_valid():
            investimento = form.save(commit=False)
            # Lógica de cálculo para tempo de retorno e projeto viável
            investimento.tempo_retorno = (investimento.recurso_inicial + investimento.custo_mensal * investimento.tma) / investimento.receita_estimada
            investimento.projeto_viavel = True  # ou qualquer outra lógica para definir a viabilidade
            investimento.save()
        return redirect('analise_investimento_result', pk=investimento.pk)
    else:
        form = AnaliseInvestimentoForm()
    
    return render(request, 'analise_investimento/form.html', {'form': form})

def analise_investimento_result(request, pk):
    investimento = AnaliseInvestimento.objects.get(pk=pk)
    return render(request, 'analise_investimento/result.html', {'investimento': investimento})
