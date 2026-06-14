from django.shortcuts import render, redirect
from .models import Quarto
from .forms import QuartoForm


def index(request):

    quartos = Quarto.objects.all()

    return render(
        request,
        'telaQuartos.html',
        {'quartos': quartos}
    )


def novoQuarto(request):

    if request.method == 'POST':

        form = QuartoForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('quartos')

    else:

        form = QuartoForm()

    return render(
        request,
        'novo_quarto.html',
        {'formulario': form}
    )