from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def clientes(request):
    return HttpResponse('Clientes: Maria, José e João')

def cliente_detalhe(request, id):
    return HttpResponse(id)

def cliente_por_nome(request, nome):
    return HttpResponse('Olá %s' % nome)