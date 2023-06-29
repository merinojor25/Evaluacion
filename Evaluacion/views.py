from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
    return render (request,"index.html")
def calendario(request):
    return render (request,"calendario.html")
def form(request):
    return render (request,"form.html")
def historia(request):
    return render (request,"historia.html")
def jugadores(request):
    return render (request,"jugadores.html")
def davis(request):
    return render (request,"davis.html")
def kobe(request):
    return render (request,"kobe.html")
def lebron(request):
    return render (request,"lebron.html")
def magic(request):
    return render (request,"magic.html")