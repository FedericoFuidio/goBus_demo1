from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.api),
    path('signup/', views.signup_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('new_line/', views.add_line),
    path('get_lineas/', views.get_lineas),
    path('new_linea_completa/', views.add_linea_completa),
    path('new_mensaje/', views.add_mensaje),
    path('get_lineas_completas/', views.get_lineas_completas),
    path('get_mensajes/', views.get_mensajes)
]