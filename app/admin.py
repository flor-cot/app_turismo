from django.contrib import admin
from .models import Provincia, Ciudad, Hotel, Comentario

# Register your models here.
class HotelInline(admin.StackedInline):
    model = Hotel

class CiudadAdmin(admin.ModelAdmin):
    fields = ['nombre']
    inlines = [HotelInline]
    list_display = ('nombre', 'provincia',)

class CiudadInline(admin.StackedInline):
    model = Ciudad

class ProvinciaAdmin(admin.ModelAdmin):
    fields = ['nombre']
    inlines = [CiudadInline]

admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Hotel)
admin.site.register(Comentario)