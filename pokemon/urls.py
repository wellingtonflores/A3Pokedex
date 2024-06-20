from django.urls import path
from .views import pokemon_detail

urlpatterns = [
    path('pokemon/<str:pokemon_id>/', pokemon_detail, name='pokemon_detail'),
    path('pokemon/<str:pokemon_name>/', pokemon_detail, name='pokemon_detail')
]
