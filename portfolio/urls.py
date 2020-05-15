#from django.contrib import admin
from django.urls import path
from .views import *
from portfolio import views

urlpatterns = [
    path('', views.home), 
    path('home/', views.home),    
    path('sobre/', views.sobre),
    path('servicos/', views.servicos),
    path('artigos/', views.artigos),     
    path('portfolio/', views.portfolio),
    path('orcamentos/', views.orcamentos),
    path('orcamentos/formulario/', views.formulario),   
    path('sobre/trabalheConosco/', views.trabalheConosco),       
    path('orcamentos/formulario/orcamentos/formulario/insert', views.insereFormulario), 
    path('sobre/trabalheConosco/sobre/formulario/insert', views.insereCurriculo), 
]
