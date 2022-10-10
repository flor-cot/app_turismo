from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.index, name ='index'),
    path('login',views.login, name='login'),
    path('destinos/<str:provincia>',views.destinos,name="destinos"),
    path('about', views.about, name="about")
]