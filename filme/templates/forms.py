from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class CriarContaForm(UserCreationForm):
    email= forms.EmailField()

    class Meta:
        model = Usuario
        field = ('username', 'email', 'password1', 'password2')