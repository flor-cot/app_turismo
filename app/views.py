from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from app.models import Provincia, Hotel, Comentario, Atraccion, Ciudad, ComentarioGustado , ComentarioAtraccion, ComentarioGustadoAtraccion
from django.template import loader

from app.forms import RegistroForm, EditProfileForm

from django.contrib.postgres.search import SearchQuery, SearchVector

from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.db.models import Q
from datetime import datetime

import random


def iniciar_sesion(request):
    
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

@login_required
def mi_perfil(request):
    if request.method == 'POST':
        edit_form = EditProfileForm(request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request,'Los datos fueron modificados con éxito.')
            return redirect('miperfil')
        else:
            messages.warning(request,'Los datos no pudieron ser modificados.')
            return redirect('miperfil')
    else:
        edit_form = EditProfileForm(instance=request.user)
        args = {'form': edit_form}
        return render(request,'app/miperfil.html', args)

@login_required
def cambiar_password(request):
    return render(request,'app/nueva_password.html')

def registro(request):
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
    hoteles_query = Hotel.objects.order_by('-puntuacion').all()
    hoteles = hoteles_query[:4]
    hotel_random = random.choice(range(1,len(hoteles_query)+1))
    contexto = {'hoteles': hoteles, 'hotel_random': Hotel.objects.get(pk=hotel_random)}
    return render(request, 'app/index.html', contexto)


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

@login_required
def undestino(request,id_destino=""):
    ciudad = Ciudad.objects.get(id=id_destino)
    atracciones = Atraccion.objects.filter(ciudad=id_destino)
    hoteles = Hotel.objects.filter(ciudad=id_destino)
    contexto = {'atracciones': atracciones, 'hoteles': hoteles, 'ciudad' : ciudad}
    return render(request, 'app/undestino.html', contexto)

##
##  Detalle de los hoteles y CRUD comentarios
##

def hotel_detalle(request, id_hotel):
    hotel = Hotel.objects.get(id=id_hotel)
    comentarios = Comentario.objects.filter(hotel=id_hotel)

    return render(request, 'app/hotel_detalle.html', {'hotel': hotel, 'comentarios': comentarios})

def atraccion(request, id_atraccion):
    atraccion = Atraccion.objects.get(id=id_atraccion)
    comentarios = ComentarioAtraccion.objects.filter(atraccion=id_atraccion)
    
    return render(request, 'app/atraccion.html', {'atraccion': atraccion, 'comentarios':comentarios})

def busqueda(request):
    q = request.GET.get('q')

    if q:
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

    
def agregar_comentario(request, id_hotel):
    if request.user.is_authenticated:
        if request.method == 'POST':
            comentario = Comentario(mensaje=request.POST.get('comentario_nuevo'),hotel_id=id_hotel,usuario_id=request.user.id, fecha=datetime.now())
            comentario.save()
            return redirect('hotel_detalle', id_hotel=id_hotel)
    else:
        messages.info(request, "Necesita loguearse para comentar")
        return redirect('hotel_detalle', id_hotel=id_hotel)

def eliminar_comentario(request, id_comentario, id_hotel):
    if request.user.is_authenticated:
        comentario_a_eliminar = Comentario.objects.get(id=id_comentario)
        comentario_a_eliminar.delete()
        return redirect('hotel_detalle', id_hotel=id_hotel)
    else:
        messages.info(request, "Necesita loguearse para eliminar comentario")
        return redirect('hotel_detalle', id_hotel=id_hotel)

def gustar_comentario(request, id_comentario, id_hotel):
    if request.user.is_authenticated:
        usuario_id = request.user.id

        # traemos el comentario a gustar
        comentario = Comentario.objects.get(id=id_comentario)

        try:
            # traemos el registro de la tabla intermedia ComentarioGustado para ese comentario y usuario si existe
            comentario_estado = ComentarioGustado.objects.get(comentario_id=id_comentario, usuario_id=usuario_id)
            # Si ya le gustaba le deja de gustar y viceversa
            if comentario_estado.estado == True:
                comentario.likes = comentario.likes - 1
                comentario_estado.estado = False
            else:
                comentario.likes = comentario.likes + 1
                comentario_estado.estado = True
            comentario.save()
            comentario_estado.save()
        except:
            # si no existe el registro de la tabla intermedia lo creamos y le ponemos el me gusta
            nuevo_me_gusta = ComentarioGustado(comentario_id=id_comentario, usuario_id=usuario_id, estado=True)
            comentario.likes = comentario.likes + 1
            comentario.save()
            nuevo_me_gusta.save()
        return redirect('hotel_detalle', id_hotel=id_hotel)
    else:
        messages.info(request, "Necesita loguearse para poner me gusta")
        return redirect('hotel_detalle', id_hotel=id_hotel)



def agregar_comentario_atraccion(request, id_atraccion):
    if request.user.is_authenticated:
        if request.method == 'POST':
            comentario = ComentarioAtraccion(mensaje=request.POST.get('comentario_nuevo'),atraccion_id=id_atraccion,usuario_id=request.user.id, fecha=datetime.now())
            comentario.save()
            return redirect('atraccion', id_atraccion=id_atraccion)
    else:
        messages.info(request, "Necesita loguearse para comentar")
        return redirect('atraccion', id_atraccion=id_atraccion)

def eliminar_comentario_atraccion(request, id_comentario, id_atraccion):
    if request.user.is_authenticated:
        comentario_a_eliminar = ComentarioAtraccion.objects.get(id=id_comentario)
        comentario_a_eliminar.delete()
        return redirect('atraccion', id_atraccion=id_atraccion)
    else:
        messages.info(request, "Necesita loguearse para eliminar comentario")
        return redirect('atraccion', id_atraccion=id_atraccion)

def gustar_comentario_atraccion(request, id_comentario, id_atraccion):
    if request.user.is_authenticated:
        usuario_id = request.user.id

        # traemos el comentario a gustar
        comentario = ComentarioAtraccion.objects.get(id=id_comentario)

        try:
            # traemos el registro de la tabla intermedia ComentarioGustado para ese comentario y usuario si existe
            comentario_estado = ComentarioGustadoAtraccion.objects.get(comentario_id=id_comentario, usuario_id=usuario_id)
            # Si ya le gustaba le deja de gustar y viceversa
            if comentario_estado.estado == True:
                comentario.likes = comentario.likes - 1
                comentario_estado.estado = False
            else:
                comentario.likes = comentario.likes + 1
                comentario_estado.estado = True
            comentario.save()
            comentario_estado.save()
        except:
            # si no existe el registro de la tabla intermedia lo creamos y le ponemos el me gusta
            nuevo_me_gusta = ComentarioGustadoAtraccion(comentario_id=id_comentario, usuario_id=usuario_id, estado=True)
            comentario.likes = comentario.likes + 1
            comentario.save()
            nuevo_me_gusta.save()
        return redirect('atraccion', id_atraccion=id_atraccion)
    else:
        messages.info(request, "Necesita loguearse para poner me gusta")
        return redirect('atraccion', id_atraccion=id_atraccion)
