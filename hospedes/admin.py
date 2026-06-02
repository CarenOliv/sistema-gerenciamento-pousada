from django.contrib import admin

from .models import *
#Enviar a model para o painel do administrador:

admin.site.register(Hospede)