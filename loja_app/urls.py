from django.urls import path

from . import views

app_name = "loja_app"
urlpatterns = [
    path("",                         views.index,            name = 'index'),
    path("index.html",               views.index,            name = 'index'),
    path("login.html",               views.login,            name = 'login'),
    path("cadastro.html",            views.cadastro,         name = 'cadastro'),
    path("informatica.html",         views.informatica,      name = 'informatica'),
    path("consoles.html",            views.consoles,         name = 'consoles'),
    path("games.html",               views.games,            name = 'games'),
    path("sobre-a-empresa.html",     views.sobre_a_empresa,  name = 'sobre a empresa'),
    path("fale-conosco.html",        views.fale_conosco,     name = 'fale conosco'),
    path("desc-tlou.html",           views.desc_tlou,        name = 'the last of us'),
    path("desc-tlou2.html",          views.desc_tlou2,       name = 'the last of us 2'),
    path("clientela",                views.lista_de_clientes,name = 'clientes'),
    #path("<str:nome>", views.nome_da_loja)
]