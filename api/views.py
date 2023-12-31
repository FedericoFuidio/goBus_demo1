from django.shortcuts import render, redirect
from .models import Linea, LineaCompleta, Mensaje
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from . import forms
import requests
from django.http import JsonResponse
from django.core import serializers
# Create your views here.

def api(request):
    lineas = LineaCompleta.objects.all().order_by('date')
    return render(request, 'api/api.html', {'lineas': lineas})

def signup_view(request):
    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            login(request, user)
            # Log the user in
            # Por ahora redireccionamos a /api
            return redirect('/api/')
    else:
        form = UserCreationForm()

    return render(request, 'api/signup.html', {'form':form})

def login_view(request):
    if (request.method == 'POST'):
        form = AuthenticationForm(data=request.POST)
        if(form.is_valid()):
            # Los the user in
            user = form.get_user()
            login(request, user)
            # Por ahora lo direccionamos a /api
            if('next' in request.POST):
                return redirect(request.POST.get('next'))
            else:
                return redirect('/api/')

    else:
        form = AuthenticationForm()

    return render(request, 'api/login.html', {'form':form})

def logout_view(request):
    if(request.method == 'POST'):
        logout(request)
        return redirect('/api/')
    
@login_required(login_url="/api/login")
def add_line(request):
    if(request.method == 'POST'):
        form = forms.CreateLine(request.POST)
        if(form.is_valid()):
            #save line to db and send to Aplication
            form.save()
            return redirect('/api/')
    else:
        form = forms.CreateLine
    return render(request, 'api/add_line.html', {'form': form})

@login_required(login_url="/api/login")
def add_linea_completa(request):
    if(request.method == 'POST'):
        form = forms.CreateLineaCompleta(request.POST)
        if(form.is_valid()):
            #save line to db and send to Aplication
            form.save()
            return redirect('/api/')
    else:
        form = forms.CreateLineaCompleta
    return render(request, 'api/add_linea_completa.html', {'form': form})

@login_required(login_url="/api/login")
def add_mensaje(request):
    if(request.method == 'POST'):
        form = forms.CreateMensaje(request.POST)
        if(form.is_valid()):
            #save line to db and send to Aplication
            form.save()
            return redirect('/api/')
    else:
        form = forms.CreateMensaje
    return render(request, 'api/add_mensaje.html', {'form': form})

def get_lineas(request):
    print("RESPONDO REQUEST")
    lineas = LineaCompleta.objects.all().order_by('date')
    data = serializers.serialize("json", lineas)
    print(data)
    print("TERMINO RESPUESTA")
    return JsonResponse(data, safe=False)

def get_lineas_completas(request):
    print("RESPONDO REQUEST")
    lineasCompletas = LineaCompleta.objects.all().order_by('date')
    data = serializers.serialize("json", lineasCompletas)
    print(data)
    print("TERMINO RESPUESTA")
    return JsonResponse(data, safe=False)

def get_mensajes(request):
    print("RESPONDO REQUEST")
    mensajes = Mensaje.objects.all().order_by('date')
    data = serializers.serialize("json", mensajes)
    print(data)
    print("TERMINO RESPUESTA")
    return JsonResponse(data, safe=False)