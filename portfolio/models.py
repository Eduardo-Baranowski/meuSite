from django.db import models
from django import forms



# Create your models here.

class Formulario(models.Model):    
    nome = models.CharField('name', max_length=150)
    telefone = models.CharField('telefone', max_length=50)    
    descricao = models.TextField('descricao', max_length=550, default='string')
    email = models.EmailField('email', max_length=150)

    def __str__(self):
        return self.nome

class Curriculo(models.Model):    

    nome = models.CharField('name', max_length=150)
    telefone = models.CharField('telefone', max_length=50)    
    descricao = models.TextField('descricao', max_length=550, default='string')
    email = models.EmailField('email', max_length=150)
    curriculo = models.FileField('curriculo', upload_to='Downloads/')

    def __str__(self):
        return self.nome