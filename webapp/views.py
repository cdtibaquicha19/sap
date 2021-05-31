from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return HttpResponse("hola mundo desde django ")

def despedirce(request):
    return HttpResponse("despedida desde django ")

def contacto(request):
    return HttpResponse("3175217930 - cdtibaquicha19@gmail.com")