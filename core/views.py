from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Produto

from .models import Veiculo

from .models import Cliente

def index (request):
    produtos = Produto.objects.all()
    veiculos = Veiculo.objects.all()
    clientes = Cliente.objects.all()
    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Teste de inserção de outra legenda',
        'produtos' : produtos,
        'veiculos' : veiculos,
        'clientes' : clientes
    }
    return render(request,'index.html', context)

def contato (request):
    clientes = Cliente.objects.all()
    context ={
        'clientes' : clientes
    }
    return render (request,'contato.html', context)

def produto(request, pk):
    #prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto,id=pk)
    context = {
        'produto' : prod
    }
    return render (request, 'produto.html', context)

def error404 (request, ex):
        template = loader.get_template('404.html')
        return HttpResponse(content=template.render(), content_type='text.html: charset=utf8', status=404)

def error500 (request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text.html: charset=utf8', status=500)

