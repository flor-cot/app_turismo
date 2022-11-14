from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.index, name ='index'),
    path('login',views.iniciar_sesion, name='login'),
    path('logout',views.cerrar_sesion, name='logout'),
    path('registro',views.registro, name='registro'),
    path('destinos/<str:provincia>',views.destinos,name="destinos"),
    path('hotel/<int:id_hotel>', views.hotel_detalle, name="hotel_detalle"),
    path('about', views.about, name="about")
]