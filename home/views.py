from django.shortcuts import render
#vamos usar o render para chamar o Template
from django.http import HttpResponse

# Create your views here.

def principal(request):
    #return HttpResponse("Chegamos na View")
    return render(request,'index.html') #o request tem que ser chamado no ínicio da rota aí depois: o conteúdo, nesse caso a pág HTML

