from django import forms
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from loja_app.models import cliente

clientes_nomes = []
clientes_senhas= []

class FormNovoCliente(forms.Form):
    nome    = forms.CharField(label='Nome')
    senha   = forms.CharField(label='Senha', widget=forms.PasswordInput)

# Create your views here.
def index(request):
    return render(request, "loja_app/index.html")
def informatica(request):
    return render(request, "loja_app/informatica.html")
def consoles(request):
    return render(request, "loja_app/consoles.html") 
def games(request):
    return render(request, "loja_app/games.html")
def desc_tlou(request):
    return render(request, "loja_app/desc-tlou.html")
def desc_tlou2(request):
    return render(request, "loja_app/desc-tlou2.html")
def sobre_a_empresa(request):
    return render(request, "loja_app/sobre-a-empresa.html")
def fale_conosco(request):
    return render(request, "loja_app/fale-conosco.html")   
def login(request):
    return render(request, 'loja_app/login.html')
def cadastro(request):
    if request.method == "POST":
        form = FormNovoCliente(request.POST)

        if form.is_valid():
            cliente_nome = form.cleaned_data["nome"]
            cliente_senha = form.cleaned_data["senha"]

            abc = cliente.objects.create(nome = cliente_nome, senha = cliente_senha).save()
            
            return HttpResponseRedirect(reverse("loja_app:index"))
        else: 
            return render(request, 'loja_app/cadastro.html',  {
                "form": form
            })

    return render(request, "loja_app/cadastro.html" , {
        "form": FormNovoCliente()
    })
def lista_de_clientes(request):
    return render(request, "loja_app/lista_de_clientes.html", {
        "clientes": cliente.objects.all()
    })

    '''
    return render(request, "loja_app/lista_de_clientes.html", {
        "nomes": clientes_nomes,
        "senhas": clientes_senhas
    })
    '''
