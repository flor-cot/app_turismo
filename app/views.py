from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from django.shortcuts import render, redirect
from django.urls import reverse
from app.models import Provincia, Hotel, Comentario, Destino

from django.template import loader

from app.forms import RegistroForm, LoginForm

from django.contrib import messages

def login(request):
    
     if(request.method == 'POST'):

        login_form = LoginForm(request.POST)
        if(login_form.is_valid()):
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.warning(request,'Por favor revisa los errores')
    else:
        login_form = LoginForm()
    provincias = Provincia.objects.all()
    contexto = { 'provincias': provincias, 'login_form':login_form}
    return render(request,'app/login.html', contexto)

def registro(request):
    provincias = Provincia.objects.all()
    if(request.method == 'POST'):
        registro_form = RegistroForm(request.POST)
        if(registro_form.is_valid()):
            messages.success(request,'Muchas gracias por registrarte.')
        else:
            messages.warning(request,'Por favor revisa los errores')
    else:
        registro_form = RegistroForm()
    contexto = { 'provincias': provincias, 'registro_form':registro_form}
    return render(request,'app/registro.html', contexto)

def index(request):
    provincias = Provincia.objects.all()
    hoteles = Hotel.objects.order_by('-puntuacion').all()
    
    contexto = {'provincias': provincias, 'hoteles': hoteles}
    return render(request, 'app/index.html', contexto)


def destinos(request,provincia=""):
    provincias = Provincia.objects.all()
    id = Provincia.objects.filter(nombre = provincia).values('id')[0]['id']
    destinos = Destino.objects.filter(provincia_id = id)
    contexto = {'provincia': provincia, 'provincias': provincias, 'destinos': destinos}
    return render(request,'app/destinos.html', contexto)

def about(request):
    data = {'hoteles':('hola','chau')}
    return render(request, 'app/about.html', data)

def undestino(request,iddestino=""):
    provincias = Provincia.objects.all()
    destino = Destino.objects.get(pk=iddestino)
    contexto = { 'provincias': provincias, 'destino': destino}
    return render(request, 'app/undestino.html', contexto)

def hotel_detalle(request, id_hotel):
    hotel = Hotel.objects.get(id=id_hotel)
    comentarios = Comentario.objects.filter(hotel=id_hotel)

    return render(request, 'app/hotel_detalle.html', {'hotel': hotel, 'comentarios': comentarios})
