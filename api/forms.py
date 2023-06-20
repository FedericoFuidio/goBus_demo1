from django import forms 
from . import models

class CreateLine(forms.ModelForm):
    class Meta:
        model = models.Linea
        fields = ['linea', 'empresa', 'ubicacion']


class CreateLineaCompleta(forms.ModelForm):
    class Meta:
        model = models.LineaCompleta
        fields = ['linea', 'empresa', 'recorrido']

class CreateMensaje(forms.ModelForm):
    class Meta:
        model = models.Mensaje
        fields = ['linea', 'proxima_parada', 'tiempo_proxima_parada']