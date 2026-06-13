from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva

        fields = [
            'hospede',
            'quarto',
            'data_entrada',
            'data_saida',
            'status'
        ]

        widgets = {
            'data_entrada': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'data_saida': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }