from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.urls import reverse

def index(request):
    return HttpResponse('Este es el index.')
