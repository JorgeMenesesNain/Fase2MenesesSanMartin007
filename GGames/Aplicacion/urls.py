from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('juegos/',views.juegos,name='juegos'),
    path('tarjetas/',views.tarjetas,name='tarJetas'),
    path('formulario/',views.formulario,name='formulario'),
    path('ju/',views.JuegoListView.as_view(),name='ju'),
    path('j/<int:pk>',views.JuegoDetailView.as_view(),name='juego-detail'),
    path('compañia/<int:pk>',views.CompañiaDetailView.as_view(), name='compañia-detail'),
]

urlpatterns+= [
    path('compañia/create/',views.CompañiaCreate.as_view(), name='compañia_create'),
    path('compañia/<int:pk>/delete/',views.CompañiaDelete.as_view(), name='compañia_delete'),
    path('compañia/<int:pk>/update/',views.CompañiaUpdate.as_view(), name='compañia_update'),
]