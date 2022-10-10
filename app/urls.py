from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.index),
    path('destinos/<str:provincia>',views.destinos,name="destinos"),
]