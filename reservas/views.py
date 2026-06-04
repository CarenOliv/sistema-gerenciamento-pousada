from django.shortcuts import render

# Create your views here.

from .models import Reserva

def index(request):
    reservas = Reserva.objects.all()
    return render (request, 'telareservas.html',{'reservas':reservas})