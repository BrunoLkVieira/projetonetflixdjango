from django.urls import path, include
from .views import homepage, filmepage, detalhesfilme, pesquisafilme, editarperfil, criarconta
from django.contrib.auth import views as auth_view
app_name = "filme"

urlpatterns = [
    path('', homepage.as_view(), name="homepage"),
    path("filmes/", filmepage.as_view(),name="filmepage"),
    path("filmes/<int:pk>", detalhesfilme.as_view(),name="detalhesfilme"),
    path("pesquisafilme/", pesquisafilme.as_view(), name= "pesquisafilme"),
    path("login/", auth_view.LoginView.as_view(template_name="login.html") , name= "login"),
    path("logout/", auth_view.LogoutView.as_view(template_name="logout.html") , name= "logout"),
    path("editarperfil/", editarperfil.as_view(), name="editarperfil"),
    path("criarconta/", criarconta.as_view(), name="criarconta"),
]


