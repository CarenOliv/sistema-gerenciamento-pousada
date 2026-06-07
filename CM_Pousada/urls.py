"""
URL configuration for CM_Pousada project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#rotas de apps

from home import views as views_principais
from hospedes import views as views_telaGeralHosp
from quartos import views as views_quartos
from reservas import views as views_reservas




urlpatterns = [

    path('',views_principais.login_view, name='login'),
    path('home/',views_principais.principal, name='home'),
    path('logout/',views_principais.logout_view, name='logout'),

    path('admin/',admin.site.urls),
    path('hospedes/', views_telaGeralHosp.index, name='hospedes'),
    path('quartos/', views_quartos.index, name='quartos'),
    path('reservas/', views_reservas.index, name='reservas')
]
