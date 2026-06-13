from django.db import models

# Essa tabela precisa de 2 chaves estrangeira desses bancos:
from hospedes.models import Hospede
from quartos.models import Quarto

# Create your models here.

class Reserva (models.Model):
    
    STATUS_CHOICES = [
        ('Reservada', 'Reservada'),
        ('Hospedada', 'Hospedada'),
        ('Finalizada', 'Finalizada'),
        ('Cancelada', 'Cancelada'),
    ]

    id=models.BigAutoField(primary_key=True) #chave primária

    #chaves estrangeiras:

    #on_delete=models.CASCADE : significa que se um hóspede for apagado a reserva dele também será
    hospede = models.ForeignKey(Hospede,on_delete=models.CASCADE)

    quarto=models.ForeignKey(Quarto,on_delete=models.CASCADE)

    data_entrada=models.DateField()
    data_saida=models.DateField()
    status=models.CharField(max_length=20,choices=STATUS_CHOICES)

    def __str__(self):
        return f'Reserva de {self.hospede.nome} - Quarto: {self.quarto.numero}'