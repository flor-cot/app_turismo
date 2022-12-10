from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from app.models import Provincia, Hotel, Comentario, Atraccion, Ciudad
from django.template import loader
from django.contrib.postgres.search import SearchQuery, SearchVector

from app.forms import RegistroForm

from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.db.models import Q



def iniciar_sesion(request):
    
    #  if(request.method == 'POST'):
        
    #     login_form = LoginForm(request.POST)
    #     if(login_form.is_valid()):
    #         return HttpResponseRedirect(reverse('index'))
    #     else:
    #         messages.warning(request,'Por favor revisa los errores')
    #  else:
    #     login_form = LoginForm()

    #  return render(request,'app/login.html',
    #             {'login_form':login_form})
    if request.user.is_authenticated:
        return redirect('index')    
    else:
        if(request.method == 'POST'):
            usuario = request.POST.get('usuario')
            password =request.POST.get('password')  

            #busca al usuario en la BDD
            user = authenticate(request, username=usuario, password=password)   

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Usuario O contraseña incorrecto')   

        return render(request,'app/login.html')

@login_required
def cerrar_sesion(request):
	logout(request)
	return redirect('login')


def registro(request):
    #  if(request.method == 'POST'):
    #     registro_form = RegistroForm(request.POST)
    #     if(registro_form.is_valid()):
    #         messages.success(request,'Muchas gracias por registrarte.')
    #     else:
    #         messages.warning(request,'Por favor revisa los errores')
    #  else:
    #     registro_form = RegistroForm()
        if request.user.is_authenticated:
            return redirect('index')
        else:  
            registro_form = RegistroForm()

            if request.method == 'POST':
                registro_form = RegistroForm(request.POST)
                if registro_form.is_valid():
                    registro_form.save()
                    usuario = registro_form.cleaned_data.get('username')
                    messages.success(request,'La cuenta de' + ' ' + usuario + ' ' + 'fue creada con éxito.')
                    return redirect('login')

            return render(request,'app/registro.html',
                        {'registro_form':registro_form})

def index(request):
    hoteles = Hotel.objects.order_by('-puntuacion').all()
    provincias = Provincia.objects.all()
    
    contexto = {'hoteles': hoteles , 'provincias': provincias}
    return render(request, 'app/index.html', contexto)

@login_required
def destinos(request,id_provincia=""):
    ciudades = Ciudad.objects.filter(provincia=id_provincia)
    # destinos = Destino.objects.filter(provincia=id_provincia)
    # id = Provincia.objects.filter(nombre = provincia).values('id')[0]['id']
    # destinos = Destino.objects.filter(provincia_id = id) 'destinos': destinos,
    contexto = {'ciudades': ciudades, 'provincia': Provincia.objects.get(pk=id_provincia)}
    return render(request,'app/destinos.html', contexto)

def about(request):
    data = {'hoteles':('hola','chau')}
    return render(request, 'app/about.html', data)

def undestino(request,id_destino=""):
    atracciones = Atraccion.objects.filter(ciudad=id_destino)
    hoteles = Hotel.objects.filter(ciudad=id_destino)
    contexto = {'atraccion': atracciones, 'hoteles': hoteles} #, 'ciudad': Ciudad.objects.get(pk=id_destino)}
    return render(request, 'app/undestino.html', contexto)

def hotel_detalle(request, id_hotel):
    hotel = Hotel.objects.get(id=id_hotel)
    comentarios = Comentario.objects.filter(hotel=id_hotel)

    return render(request, 'app/hotel_detalle.html', {'hotel': hotel, 'comentarios': comentarios})


def busqueda(request):
    q = request.GET.get('q')

    if q:
       # ciudades = Ciudad.objects.filter(nombre__search=q)
        ciudades = Ciudad.objects.filter(
            Q(nombre__icontains=q) | 
            Q(provincia__nombre__icontains=q) )

        atracciones = Atraccion.objects.filter(
            Q(nombre__icontains=q) | 
            Q(ciudad__nombre__icontains=q) )  
        hoteles = Hotel.objects.filter(
            Q(nombre__icontains=q) | 
            Q(ciudad__nombre__icontains=q) )   

    else:
        None
    # 
    contexto = {'ciudades':ciudades, 'atracciones':atracciones, 'hoteles':hoteles, 'q':q}
    return render(request, 'app/busqueda.html', contexto)