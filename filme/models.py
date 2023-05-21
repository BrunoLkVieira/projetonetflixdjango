from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

# criar filmes

LISTA_CATEGORIAS= (
    ("SERIE_TERROR", "Séries de Terror"),
    ("SERIES", "Séries"),

)

class Filme(models.Model):
    thumb= models.ImageField(upload_to="thumb_filmes")
    titulo= models.CharField(max_length=100)
    descricao= models.TextField(max_length=1000)
    categoria= models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    data_criacao= models.DateTimeField(default=timezone.now)
    visualizacao = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo


# criar episodios
class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.filme.titulo + " - " + self.titulo


class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")