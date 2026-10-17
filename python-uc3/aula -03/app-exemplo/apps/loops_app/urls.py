from django.urls import path
from . import views

app_name = 'loops' #Aula 03
urlpatterns = [
    path('',views.index, name= 'index'),# Aula 03
    path('for/', views.pagina_for, name='pagina_for'),
    path('jogo/', views.jogo_adivinhacao, name='jogo_adivinhacao'),
]