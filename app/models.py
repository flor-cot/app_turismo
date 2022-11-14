from django.db import models

# Create your models here.
class Provincia(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    def __str__(self):
        return self.nombre
    
class Destino(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    descripcion = models.CharField(max_length=1000, verbose_name='Descripcion')
    url=models.URLField(null=True, max_length=255)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
        return self.descripcion
        
    
class Ciudad(models.Model):
    nombre=models.CharField(max_length=100, verbose_name='Nombre')
    provincia=models.ForeignKey(Provincia, on_delete=models.CASCADE)
    # Portada=models.ImageField(upload_to='imagenes/', null=True, verbose_name="Portada")
    puntuacion=models.FloatField(null=True, verbose_name='Puntuación')

    def __str__(self):
        return self.nombre


class Hotel(models.Model):
    nombre=models.CharField(max_length=100, verbose_name='Nombre')
    descripcion=models.TextField(null=True, verbose_name='Descripción')
    url=models.URLField(null=True, max_length=255)
    # Portada=models.ImageField(upload_to='imagenes/', null=True, verbose_name="Portada")
    puntuacion=models.FloatField(null=True, verbose_name='Puntuación')
    vistas=models.IntegerField(default=0,verbose_name='Vistas')
    ciudad=models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre