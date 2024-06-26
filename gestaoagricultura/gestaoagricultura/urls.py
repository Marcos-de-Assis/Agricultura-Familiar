"""
URL configuration for gestaoagricultura project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import analise_custo_beneficio, meta_producao, custo_oportunidade

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analise_investimento/', include('analise_investimento.urls')),
    path('analise-custo-beneficio/', analise_custo_beneficio, name='analise_custo_beneficio'),
    path('meta-producao/', meta_producao, name='meta_producao'),
    path('custo-oportunidade/', custo_oportunidade, name='custo_oportunidade'),
]

