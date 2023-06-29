"""
URL configuration for Evaluacion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Evaluacion.views import index,calendario,davis,form,historia,jugadores,kobe,lebron,magic


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index,name='index'),
    path('calendario/',calendario,name='calendario'),
    path('davis/',davis,name='davis'),
    path('form',form,name='form'),
    path('historia/',historia,name='historia'),
    path('jugadores/',jugadores,name='jugadores'),
    path('kobe/',kobe,name='kobe'),
    path('lebron/',lebron,name='lebron'),
    path('magic/',magic,name='magic'),

]
