from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    nif = models.CharField(max_length=8)
    sala = models.CharField(max_length=20)
    email = models.EmailField(max_length=80)
    senha = models.CharField(max_length=20)
    