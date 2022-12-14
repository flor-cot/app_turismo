from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.index, name ='index'),
    path('login/',views.iniciar_sesion, name='login'),
    path('logout/',views.cerrar_sesion, name='logout'),
    path('miperfil/',views.mi_perfil, name='miperfil'),
    path('registro/',views.registro, name='registro'),
    
    path('destinos/<int:id_provincia>', views.destinos, name="destinos"),
    path('detalle/<int:id_destino>', views.undestino, name="undestino"),
    path('atraccion/<int:id_atraccion>', views.atraccion, name="atraccion"),
    path('hotel/<int:id_hotel>', views.hotel_detalle, name="hotel_detalle"),
    path('about/', views.about, name="about"),
    path('password/', views.cambiar_password, name="cambiar_password"),
    path('busqueda/',views.busqueda, name='busqueda'),
    
    path('comentario/<int:id_hotel>', views.agregar_comentario, name="agregar_comentario"),
    path('eliminar_comentario/<int:id_comentario>/<int:id_hotel>', views.eliminar_comentario, name="eliminar_comentario"),
    path('gustar_comentario/<int:id_comentario>/<int:id_hotel>', views.gustar_comentario, name="gustar_comentario"),
    
    path('comentario_atraccion/<int:id_atraccion>', views.agregar_comentario_atraccion, name="agregar_comentario_atraccion"),
    path('eliminar_comentario_atraccion/<int:id_comentario>/<int:id_atraccion>', views.eliminar_comentario_atraccion, name="eliminar_comentario_atraccion"),
    path('gustar_comentario_atraccion/<int:id_comentario>/<int:id_atraccion>', views.gustar_comentario_atraccion, name="gustar_comentario_atraccion"),
    path('about/', views.about, name="about")
]