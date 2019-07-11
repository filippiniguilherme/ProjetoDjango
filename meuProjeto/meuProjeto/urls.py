"""meuProjeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from .views import  home
from clientes.views import clientes, cliente_detalhe, cliente_por_nome

urlpatterns = [
    re_path(r'^$', home),
    re_path(r'^clientes$', clientes),
    re_path(r'^cliente/(?P<id>\d+)$', cliente_detalhe),
    re_path(r'^cliente/(?P<nome>\w+)$', cliente_por_nome),
    re_path(r'^admin/', admin.site.urls),
]
