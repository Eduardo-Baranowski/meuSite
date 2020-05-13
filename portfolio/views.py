from django.shortcuts import render

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
