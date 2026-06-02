from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    hospede = Hospede.objects.all() #vai pegar todos os hóspedes cadastrados no banco

    return render(request, 'telaGeralHosp.html',{'hosp':hospede})