from django.urls import path
from . import views

urlpatterns = [
    path('', views.analise_investimento, name='analise_investimento'),
    path('result/<int:pk>/', views.analise_investimento_result, name='analise_investimento_result'),
]