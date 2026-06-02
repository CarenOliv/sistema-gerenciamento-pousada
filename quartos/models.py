from django.db import models

# Create your models here.
class Quarto (models.Model):
    id = models.BigAutoField(primary_key=True)
    numero=models.IntegerField()
    tipo=models.CharField(max_length=30)
    valor_diaria=models.DecimalField(max_digits=8,decimal_places=2) #no máximo 8 números com 2 após a vírgula
    disponivel=models.BooleanField(default=True)

    def __str__(self):
        return f'Quarto número: {self.numero} - Tipo: {self.tipo}'
