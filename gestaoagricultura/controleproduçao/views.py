from django.shortcuts import render, redirect
from .models import Producao
from .forms import ProducaoForm

def controle_producao(request):
    if request.method == 'POST':
        form = ProducaoForm(request.POST)
        if form.is_valid():
            producao = form.save(commit=False)
            producao.user = request.user
            producao.save()
            return redirect('controle_producao')
    else:
        form = ProducaoForm()
    producoes = Producao.objects.filter(user=request.user)
    return render(request, 'controle_producao.html', {'form': form, 'producoes': producoes})
