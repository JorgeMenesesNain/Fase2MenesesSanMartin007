from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('juegos/',views.juegos,name='juegos'),
    path('tarjetas/',views.tarjetas,name='tarJetas'),
    path('ju/',views.JuegoListView.as_view(),name='ju'),
    path('j/<int:pk>',views.JuegoDetailView.as_view(),name='juego-detail'),
]