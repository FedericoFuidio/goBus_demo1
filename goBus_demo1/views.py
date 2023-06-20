from django.http import HttpResponse
from django.shortcuts import render, redirect



def homepage(request):
    # return HttpResponse('Bienvenido a GoBus!')
    # return render(request, 'homepage.html')
    return redirect('/api/')