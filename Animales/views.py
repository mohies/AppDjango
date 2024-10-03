from django.shortcuts import render
from .models import *



# Registro de modelos en el admin



def animales_list(request):
   
    animales= Animal.objects.all()
    return render(request,'Animales/animales_list.html',{"animales_mostrar":animales}) #template no hace falta porque esta sen settings

def colaboradores_list(request):
   
    colaborades= Colaborador.objects.all()
    return render(request,'Animales/colaboradores_list.html',{"colaboradores_mostrar":colaborades}) #template no hace falta porque esta sen settings

def protectora_list(request):
   
    protectoras= Protectora.objects.all()
    return render(request,'Animales/protectoras_list.html',{"protectoras_mostrar":protectoras}) #template no hace falta porque esta sen settings


    