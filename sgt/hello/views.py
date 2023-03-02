from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')
 

def saudacao(request, nome):
    return HttpResponse("<h1 style='color:blue'> Olá, u ari ispecious </h1> <h1 style='color:red' >%s</h1>  "%(nome))

def greet(request, nome):
    return render(request,'greet.html', {'name': nome})

def tia(request, nome):
    return render(request,'tia.html', {'name': nome, 'dia':True})
