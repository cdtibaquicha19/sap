from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from personas.models import Persona, Domicilio

def bienvenido(request):
    personas = {
        'numerototal':Persona.objects.count(),
        'personas' : Persona.objects.order_by('id')
    }
    return render(request, 'bienvenido.html', personas)

def domicilio(request):
    domicilios = {
        'numerototal': Domicilio.objects.count(),
        'domicilios': Domicilio.objects.order_by('id')
    }
    return render(request, 'domicilios.html', domicilios)