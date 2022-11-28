from django.contrib import admin
from .models import Provincia, Ciudad, Hotel, Comentario, Atraccion

# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    fields = ['nombre','ciudad']
    list_display = ['nombre','ciudad']

class HotelInline(admin.StackedInline):
    model = Hotel

class AtraccionInline(admin.StackedInline):
    model = Atraccion

class CiudadAdmin(admin.ModelAdmin):
    fields = ['nombre', 'url']
    inlines = [HotelInline, AtraccionInline]
    list_display = ('nombre', 'provincia',)

class CiudadInline(admin.StackedInline):
    model = Ciudad

class ProvinciaAdmin(admin.ModelAdmin):
    fields = ['nombre']
    inlines = [CiudadInline]

admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Comentario)
admin.site.register(Atraccion)