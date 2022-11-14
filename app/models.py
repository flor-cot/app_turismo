from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Provincia(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    def __str__(self):
        return self.nombre
    
    
class Ciudad(models.Model):
    nombre=models.CharField(max_length=100, verbose_name='Nombre')
    provincia=models.ForeignKey(Provincia, on_delete=models.CASCADE)
    url=models.URLField(null=True, max_length=255)
    # Portada=models.ImageField(upload_to='imagenes/', null=True, verbose_name="Portada")
    puntuacion=models.FloatField(null=True, verbose_name='Puntuación')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Ciudades"

class Atraccion(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion=models.TextField(null=True, verbose_name='Descripción')
    url=models.URLField(null=True, max_length=255)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    puntuacion=models.FloatField(default=0, null=True, verbose_name='Puntuación')
    vistas=models.IntegerField(default=0,verbose_name='Vistas')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Atracciones"

class Hotel(models.Model):
    nombre=models.CharField(max_length=100, verbose_name='Nombre')
    descripcion=models.TextField(null=True, verbose_name='Descripción')
    url=models.URLField(null=True, max_length=255)
    # Portada=models.ImageField(upload_to='imagenes/', null=True, verbose_name="Portada")
    ciudad=models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    puntuacion=models.FloatField(default=0, null=True, verbose_name='Puntuación')
    vistas=models.IntegerField(default=0,verbose_name='Vistas')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Hoteles"

# Para los usuarios utilizaremos el modelo User que viene incorporado en el módulo auth
# Sus campos son: username, first_name, last_name, password, email

class Comentario(models.Model):
    mensaje = models.TextField(null=True, verbose_name='mensaje')
    likes = models.IntegerField(default=0,verbose_name='Comentario Likes')
    fecha = models.DateField(auto_now_add=True, verbose_name='Fecha')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)