from django.shortcuts import render
from . models import Genero,Juego,Compañia
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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

def formulario(request):
    return render(
        request,"formulario.html")

class CompañiaCreate(CreateView):
    model = Compañia
    fields = '__all__'

class CompañiaUpdate(UpdateView):
    model = Compañia
    fields = ['compañia']

class CompañiaDelete(DeleteView):
    model = Compañia
    success_url = reverse_lazy('index')

class CompañiaDetailView(generic.DetailView):
    model = Compañia 

class JuegoListView(generic.ListView):
    model=Juego
    paginate=10

class JuegoDetailView(generic.DetailView):
    model=Juego