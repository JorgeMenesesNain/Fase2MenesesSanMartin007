from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('juegos/',views.juegos,name='juegos'),
    path('trajetas/',views.tarjetas,name='tarJetas')
    
]