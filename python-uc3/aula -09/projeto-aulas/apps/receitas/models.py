from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Categoria(models.Model):
    """Representa uma categoria de receita, como Sobremesa ou Jantar."""

    nome = models.CharField(max_length=100)

    class Meta:
            verbose_name = "Categoria"
            verbose_name_plural = "Categorias"
            ordering = ["nome"]

    def __str__(self):
        return self.nome

class Receita(models.Model):
    """Representa uma receita publicada no sistema."""

    titulo = models.CharField(max_length=200)

    ingredientes = models.TextField(
        help_text="Informe um ingrediente por linha."
    )

    modo_preparo = models.TextField(
        help_text="Descreva o passo a passo do preparo."
    )

    tempo_preparo = models.PositiveIntegerField(
        help_text="Tempo total de preparo, em minutos."
    )

    data_publicacao = models.DateTimeField(auto_now_add=True)

    publicada = models.BooleanField(default=False)