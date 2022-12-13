from django.contrib import admin
from .models import Provincia, Ciudad, Hotel, Comentario, Atraccion, ComentarioGustado

# Register your models here.
"""Modelo del hotel"""
class HotelAdmin(admin.ModelAdmin):
    fields = ['nombre','ciudad']
    list_display = ['nombre','ciudad']

class HotelInline(admin.StackedInline):
    model = Hotel

class AtraccionInline(admin.StackedInline):
    model = Atraccion


"""Modelo de la ciudad"""
class CiudadAdmin(admin.ModelAdmin):
    fields = ['nombre', 'url']
    inlines = [HotelInline, AtraccionInline]
    list_display = ('nombre', 'provincia',)

class CiudadInline(admin.StackedInline):
    model = Ciudad


"""Modelo de la provincia"""
class ProvinciaAdmin(admin.ModelAdmin):
    fields = ['nombre']
    inlines = [CiudadInline]


"""Modelo del comentario"""

class ComentarioGustadoInline(admin.StackedInline):
    model = ComentarioGustado

class ComentarioAdmin(admin.ModelAdmin):
    inlines = [ComentarioGustadoInline]

admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Comentario,ComentarioAdmin)
admin.site.register(Atraccion)