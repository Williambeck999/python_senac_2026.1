from django.contrib import admin

# Register your models here.

from .models import Categoria, Receita

admin.site.register(Categoria)
admin.site.register(Receita)