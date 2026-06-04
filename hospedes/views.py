from django.shortcuts import render, redirect
from .models import *
from .forms import HospForm

# Create your views here.

def index(request):
    hospede = Hospede.objects.all() #vai pegar todos os hóspedes cadastrados no banco

    if request.method == "POST":
        form = HospForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('hospedes')
    else:
        form = HospForm()

    return render(request, 
                  'telaGeralHosp.html',
                  {'hosp':hospede,
                   'formulario':form} #isso são objetos
                  )

