# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .models import Projeto # Importe o modelo do projeto, se aplicável
from .utils import analise_custo_beneficio # Importe a função de análise de custo benefício

def analise_custo_beneficio_view(request):
    if request.method == 'POST':
        # Obtenha os dados do formulário
        nome_projeto = request.POST.get('nome_projeto')
        data_inicio_projeto = request.POST.get('data_inicio_projeto')
        # Obtenha os outros dados necessários do formulário

        # Chame a função de análise de custo benefício
        diferenca_custo, rec_liquida = analise_custo_beneficio(nome_projeto, data_inicio_projeto, ...)

        # Retorne os resultados em formato JSON
        return JsonResponse({'diferenca_custo': diferenca_custo, 'rec_liquida': rec_liquida})

    # Se o método da solicitação não for POST, retorne uma resposta vazia
    return JsonResponse({}, status=400)
