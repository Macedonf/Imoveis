from django.shortcuts import render

from imoveis.models import Inquilino, Imovel


#pagina principal(inicial)
def index(request):
    return render(request, 'imoveis/index.html')


#listagem de imoveis
def list_imoveis(request):
    imoveis = Imovel.objects.all()
    return render(request, 'imoveis/list_imoveis.html', context={'imoveis': imoveis} )

def list_inquilinos(request):
    inquilinos = Inquilino.objects.all()
    return render(request, 'imoveis/list_inquilinos.html', context={'inquilinos': inquilinos})