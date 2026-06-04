from django import forms
from .models import Hospede #esse . antes d emodels é para indicar que é no mesmo app

class HospForm (forms.ModelForm):

    class Meta: #o que vai compor o formulário

        model=Hospede #primeiro parâmetro

        #campos:
        fields=['nome','cpf','telefone','email']