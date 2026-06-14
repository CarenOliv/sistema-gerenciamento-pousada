from django.shortcuts import render, redirect
from .models import Hospede
from .forms import HospForm


def index(request):
    hospede = Hospede.objects.all() #vai pegar todos os hóspedes cadastrados no banco

    return render(
        request,
        'telaGeralHosp.html',
        {'hosp': hospede}
    )


def novoHospede(request):

    if request.method == 'POST':
        form = HospForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('hospedes')

    else:
        form = HospForm()

    return render(
        request,
        'novo_hospede.html',
        {'formulario': form}
    )