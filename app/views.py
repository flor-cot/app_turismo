from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

def index(request):
    return HttpResponse('Este es el index.')

def destinos(request,provincia=""):
    return render(request,'app/destinos.html',{'provincia': provincia})
