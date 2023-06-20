from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.api),
    path('signup/', views.signup_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('new_line/', views.add_line),
]