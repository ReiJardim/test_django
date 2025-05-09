from django.shortcuts import render

from django.http import HttpResponse

from datetime import datetime


# Create your views here.

def mensagem(request):
    hora_atual = datetime.now().hour
    if hora_atual < 12:
        saudacao = "Bom dia!"
    elif hora_atual < 18:
        saudacao = "Boa tarde!"
    else:
        saudacao = "Boa noite!"

    return render(request, 'mensagem.html', {'mensagem': saudacao})


def home(request):
    nome = 'King'

    return render(request, 'home.html', {'nome': nome})


def saudacao(request, nome):

    mesnage = f'Olá {nome}, tudo bem?'
    return HttpResponse(mesnage)


def produto(request, id_produto):
    produtos = {
        1: 'Notebook',
        2: 'Televisão',
        3: 'Sapato'
    }
    produto = produtos.get(id_produto, 'Produto não encontrado')
    return HttpResponse(f'Produto: {produto}')


def index(request):

    ola = "ôpa !"
    return render(request, 'index.html', {'ola': ola})
