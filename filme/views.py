from django.shortcuts import render, redirect
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
# def homepage(request):
#     return render(request, "homepage.html")

class homepage(TemplateView):
    template_name = "homepage.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("filme:filmepage")
        else:
            return super().get(self, request, *args, **kwargs)



# def filmepage(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context["lista_filmes"] = lista_filmes
#     return render(request, "filmepage.html", context)

class filmepage(LoginRequiredMixin, ListView):
    template_name = "filmepage.html"
    model = Filme
    #object_list



class detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    #object -> 1 item do nosso modelo


    def get(self, request, *args, **kwargs):
        #contabilizar uma visualização
        filme = self.get_object()
        filme.visualizacao += 1
        filme.save()
        usuario= request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(detalhesfilme, self).get_context_data(**kwargs)

        filmes_relacionados = Filme.objects.filter(categoria = self.get_object().categoria)[0:8]
        context["filmes_relacionados"] = filmes_relacionados
        return context



class pesquisafilme(LoginRequiredMixin, ListView):
    template_name = "pesquisafilme.html"
    model = Filme

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get("query")

        if termo_pesquisa:
            object_list = Filme.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None
    # object_list


class editarperfil(LoginRequiredMixin, TemplateView):
    template_name = "editarperfil.html"


class criarconta(TemplateView):
    template_name = "criarconta.html"