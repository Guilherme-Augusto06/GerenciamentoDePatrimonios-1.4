from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    nif = models.CharField(max_length=8)
    sala = models.CharField(max_length=20)
    email = models.EmailField(max_length=80)
    senha = models.CharField(max_length=20)
    
class Senai(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=1500)
    logo = models.ImageField(upload_to='logo/')