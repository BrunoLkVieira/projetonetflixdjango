from .models import Filme


def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by("-data_criacao")[0:8]
    return {'lista_filmes_recentes':lista_filmes}

def lista_filme_emalta(request):
    lista_filme = Filme.objects.all().order_by("-visualizacao")[0:8]
    return {"lista_filme_emalta":lista_filme}

