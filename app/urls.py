from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.index, name ='index'),
    path('login',views.login, name='login'),
    path('registro',views.registro, name='registro'),
    path('destinos/<int:id_provincia>', views.destinos, name="destinos"),
    path('detalle/<int:id_destino>', views.undestino, name="undestino"),
    path('hotel/<int:id_hotel>', views.hotel_detalle, name="hotel_detalle"),
    path('about', views.about, name="about")
]