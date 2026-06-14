from django.shortcuts import render, redirect
from .forms import ReservaForm
from .models import Reserva


def index(request):

    reservas = Reserva.objects.all()

    return render(
        request,
        'telareservas.html',
        {'reservas': reservas}
    )


def novaReserva(request):

    if request.method == 'POST':

        form = ReservaForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('reservas')

    else:

        form = ReservaForm()

    return render(
        request,
        'nova_reserva.html',
        {'form': form}
    )