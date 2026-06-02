from django.db import models

# Create your models here.

class Hospede (models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nome} - {self.cpf}'