from django.db import models

# Create your models here.
class Linea(models.Model):
    linea = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.linea
    
    '''
    # Funcion para mostrar solo unos pocos caracteres en la vista de Django
    def snippet(self):
        return self.ubicacion[:50] + '...' # Usado si la ubicacion es muy larga
    '''

class Mensaje(models.Model):
    linea = models.CharField(max_length=100)
    proxima_parada = models.CharField(max_length=100)
    tiempo_proxima_parada = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.linea
    

class LineaCompleta(models.Model):
    linea = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    recorrido = models.JSONField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.linea
    
