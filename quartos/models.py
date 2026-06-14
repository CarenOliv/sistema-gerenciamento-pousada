from django.db import models

class Quarto(models.Model):

    TIPO_CHOICES = [
        ('Solteiro', 'Solteiro'),
        ('Casal', 'Casal'),
        ('Luxo', 'Luxo'),
        ('Família', 'Família'),
    ]

    numero = models.IntegerField()

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES
    )

    capacidade = models.IntegerField()

    valor_diaria = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    disponivel = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f'Quarto número: {self.numero} - Tipo: {self.tipo}'
        
        
        
        
        

