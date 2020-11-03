from django.shortcuts import render
from . models import Genero,Juego,Compañia
from django.views import generic

# Create your views here.
def index(request):
    return render(
        request,"index.html")

def juegos(request):
    return render(
        request,"juegos.html")

def tarjetas(request):
    return render(
        request,"tarjetas.html")

class JuegoListView(generic.ListView):
    model=Juego
    paginate=10

class JuegoDetailView(generic.DetailView):
    model=Juego