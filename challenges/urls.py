from os import name

from django.urls import path
from . import views

# Se creo este archivo urls.py en la app challenges
urlpatterns = [
    # path("january", views.january),
    # path("february", views.february)
    # str y int: es un convertidor, ejm: /123 -> "123"
    path("", views.index, name="index"),  # Se activara automaticamente
    path("<int:month>", views.monthly_challenge_by_number),
    # Creando una 'dynamic route'
    path("<str:month>", views.monthly_challenge, name="dynamic_path"),
]
