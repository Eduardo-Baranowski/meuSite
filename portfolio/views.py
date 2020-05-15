from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import *
from django import forms



# Create your views here.

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def servicos(request):
    return render(request, 'servicos.html')

def artigos(request):
    return render(request, 'artigos.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def orcamentos(request):
    return render(request, 'orcamentos.html')

def formulario(request):
    return render(request, 'formulario.html')

def insereFormulario(request):
    nome = request.POST.get('name')    
    telefone = request.POST.get('telefone')    
    descricao = request.POST.get('descricao')
    email = request.POST.get('email')
    if email:
        formulario = Formulario()
        formulario.nome=nome
        formulario.telefone=telefone
        formulario.descricao=descricao
        formulario.email=email
        formulario.save()
        return redirect('/home')

def servicos(request):
    return render(request, 'servicos.html')

def trabalheConosco(request):
    return render(request, 'trabalheConosco.html')


def insereCurriculo(request):
    nome = request.POST.get('name')    
    telefone = request.POST.get('telefone')    
    descricao = request.POST.get('descricao')
    email = request.POST.get('email')
    curriculo = request.POST.get('curriculo')

    if email:
        formulario = Curriculo()
        formulario.nome=nome
        formulario.telefone=telefone
        formulario.descricao=descricao
        formulario.email=email
        formulario.curriculo=curriculo
        formulario.save()        
        return redirect('/home')



