from django.shortcuts import render, redirect
from .models import Praga
from .forms import PragaForm

def controle_pragas(request):
    if request.method == 'POST':
        form = PragaForm(request.POST)
        if form.is_valid():
            praga = form.save(commit=False)
            praga.user = request.user
            praga.save()
            return redirect('controle_pragas')
    else:
        form = PragaForm()
    pragas = Praga.objects.filter(user=request.user)
return render(request, 'controle_pragas.html', {'form': form, 'pragas': pragas})