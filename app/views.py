from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render, redirect
from django.urls import reverse
from app.models import Provincia
from app.models import Destino

from django.template import loader

from app.forms import RegistroForm, LoginForm

from django.contrib import messages

def login(request):
    if(request.method == 'POST'):
        contexto = {
        'hoteles' : (
            {'nombre': 'Dormís Acá',
            'localidad': 'Esquel',
            'url': 'https://cf.bstatic.com/xdata/images/hotel/square200/326764577.webp?k=7bf33baa41be7679d441daae4f50729f207006a81c368049d4a98842e84dacce&o=',
            'nota': 9.5},
            {'nombre': 'Hotel Libertador',
            'localidad': 'Trelew',
            'url': 'https://cf.bstatic.com/xdata/images/hotel/square200/158940060.webp?k=8eb5f2d0f9c1985a578700b6e20c2319945dd5596f1d1ea2caadcf0ff0670428&o=',
            'nota': 8.6},
            {'nombre': 'Hotel El Pedral',
            'localidad': 'Punta Ninfas',
            'url': 'https://cf.bstatic.com/xdata/images/hotel/square200/63971796.webp?k=1617ee39d4790de593c72e8863c5eabe705284a96ce316a83292a70a705282f7&o=',
            'nota': 9.9},
            {'nombre': 'Hotel Tolosa',
            'localidad': 'Puerto Madryn',
            'url': 'https://cf.bstatic.com/xdata/images/hotel/square200/396558790.webp?k=dfe14d2cc8eabcc0704ec3a9ce557c7dcb7bd98033758210db5bd54ec6beec9b&o=',
            'nota': 8.8},
            {'nombre': 'Lucania Palazzo Hotel',
            'localidad': 'Comodoro Rivadavia',
            'url': 'https://cf.bstatic.com/xdata/images/hotel/square200/236289877.webp?k=27178ed7bc190e32c56960c0a4683f64166eb2806609e5dabc8b648c5b7057a4&o=',
            'nota': 8.8}
        )
        }
        login_form = LoginForm(request.POST)
        if(login_form.is_valid()):
            return render(request,'app/index.html', contexto)
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
    hoteles = {
        'hoteles' : (
            {'nombre': 'Dormís Acá',
            'localidad': 'Esquel',
            'url': 'https://cf.bstatic.com/xdata/images/hotel/square200/326764577.webp?k=7bf33baa41be7679d441daae4f50729f207006a81c368049d4a98842e84dacce&o=',
            'nota': 9.5},
            {'nombre': 'Hotel Libertador',
            'localidad': 'Trelew',
            'url': 'https://cf.bstatic.com/xdata/images/hotel/square200/158940060.webp?k=8eb5f2d0f9c1985a578700b6e20c2319945dd5596f1d1ea2caadcf0ff0670428&o=',
            'nota': 8.6},
            {'nombre': 'Hotel El Pedral',
            'localidad': 'Punta Ninfas',
            'url': 'https://cf.bstatic.com/xdata/images/hotel/square200/63971796.webp?k=1617ee39d4790de593c72e8863c5eabe705284a96ce316a83292a70a705282f7&o=',
            'nota': 9.9},
            {'nombre': 'Hotel Tolosa',
            'localidad': 'Puerto Madryn',
            'url': 'https://cf.bstatic.com/xdata/images/hotel/square200/396558790.webp?k=dfe14d2cc8eabcc0704ec3a9ce557c7dcb7bd98033758210db5bd54ec6beec9b&o=',
            'nota': 8.8},
            {'nombre': 'Lucania Palazzo Hotel',
            'localidad': 'Comodoro Rivadavia',
            'url': 'https://cf.bstatic.com/xdata/images/hotel/square200/236289877.webp?k=27178ed7bc190e32c56960c0a4683f64166eb2806609e5dabc8b648c5b7057a4&o=',
            'nota': 8.8}
        )
    }
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

