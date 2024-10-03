from django.contrib import admin

# Register your models here.
from .models import *

models = [Animal, Protectora, Colaborador]

# Registro de modelos en el admin
for model in models:    
    admin.site.register(model)