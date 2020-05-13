#from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home), 
    path('home/', home),    
    path('sobre/', sobre),
    path('servicos/', servicos),
    path('artigos/', artigos),    
    path('portfolio', portfolio),
    path('orcamentos/', orcamentos),
]
