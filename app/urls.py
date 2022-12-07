from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.index, name ='index'),
    path('login/',views.iniciar_sesion, name='login'),
    path('logout/',views.cerrar_sesion, name='logout'),
    path('registro/',views.registro, name='registro'),
    path('destinos/<int:id_provincia>', views.destinos, name="destinos"),
    path('detalle/<int:id_destino>', views.undestino, name="undestino"),
    path('hotel/<int:id_hotel>', views.hotel_detalle, name="hotel_detalle"),
    path('comentario/<int:id_hotel>', views.agregar_comentario, name="agregar_comentario"),
    path('eliminar_comentario/<int:id_comentario>/<int:id_hotel>', views.eliminar_comentario, name="eliminar_comentario"),
    path('gustar_comentario/<int:id_comentario>/<int:id_hotel>', views.gustar_comentario, name="gustar_comentario"),
    path('about/', views.about, name="about")
]