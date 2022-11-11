from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from django.shortcuts import render, redirect
from django.urls import reverse
from app.models import Provincia, Hotel, Comentario

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

     return render(request,'app/login.html',
                {'login_form':login_form})

def registro(request):
     if(request.method == 'POST'):
        registro_form = RegistroForm(request.POST)
        if(registro_form.is_valid()):
            messages.success(request,'Muchas gracias por registrarte.')
        else:
            messages.warning(request,'Por favor revisa los errores')
     else:
        registro_form = RegistroForm()

     return render(request,'app/registro.html',
                {'registro_form':registro_form})

def index(request):
    provincias = Provincia.objects.all()
    hoteles = Hotel.objects.order_by('-puntuacion').all()
    
    contexto = {'provincias': provincias, 'hoteles': hoteles}
    return render(request, 'app/index.html', contexto)


def destinos(request,provincia=""):
    return render(request,'app/destinos.html',{'provincia': provincia})

def about(request):
    data = {'hoteles':('hola','chau')}
    return render(request, 'app/about.html', data)

def hotel_detalle(request, id_hotel):
    hotel = Hotel.objects.get(id=id_hotel)
    comentarios = Comentario.objects.filter(hotel=id_hotel)

    return render(request, 'app/hotel_detalle.html', {'hotel': hotel, 'comentarios': comentarios})
