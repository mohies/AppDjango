from django.urls import path
from . import views
urlpatterns = [
    path('',views.animales_list,name='animales_list'),
    path('animal',views.animales_list,name='animales_list'),
    path('colaborador',views.colaboradores_list,name='colaboradores_list'),
    path('protector',views.protectora_list,name='protectores_list'),
]