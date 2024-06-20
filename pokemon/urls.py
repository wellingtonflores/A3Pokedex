from django.shortcuts import redirect
from django.urls import path
from .views import pokemon_detail

urlpatterns = [
    path('', lambda request: redirect('pokemon_detail', pokemon_id=1)),
    path('pokemon/<str:pokemon_id>/', pokemon_detail, name='pokemon_detail'),
]
