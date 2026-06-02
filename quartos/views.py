from django.shortcuts import render

from .models import *

# Create your views here.

def index(request):
    quartos=Quarto.objects.all()

    return render(request,'telaQuartos.html',{'quartos':quartos})