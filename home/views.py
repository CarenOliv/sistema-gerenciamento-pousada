from django.shortcuts import render, redirect
#vamos usar o render para chamar o Template
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout

from hospedes.models import Hospede
from reservas.models import Reserva
from quartos.models import Quarto


def login_view(request):
    if request.method=="POST":
        username = request.POST.get("usuario")
        password = request.POST.get("senha")

        #TESTE
        #print("Usuário digitado:", username)
        #print("Senha digitada:", password)

        user = authenticate(
            request, username=username, password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            return render(
                request,
                'login.html', {'erro':'Usuário não encontrado'}
            )
    return render (request, 'login.html')


#logout próprio do Django
def logout_view(request):
    logout(request)
    return redirect('login')

def principal(request):
    
    total_hospedes = Hospede.objects.count()
    total_reservas = Reserva.objects.count()
    total_quartos = Quarto.objects.count()

    #o request tem que ser chamado no ínicio da rota aí depois: o conteúdo, nesse caso a pág HTML
    return render(request,'index.html',{
        'total_hospede': total_hospedes,
        'total_reservas':total_reservas,
        'total_quartos':total_quartos
    }) 

