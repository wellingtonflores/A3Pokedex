import pytest
from django.test import Client
from django.urls import reverse

# teste id-1
@pytest.mark.django_db
def test_pokemon_detail_id_1():
    client = Client()
    url = reverse('pokemon_detail', kwargs={'pokemon_id': 1})
    response = client.get(url)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert b'pokemon' in response.content, "Response does not contain 'pokemon'"
    assert b'name' in response.content, "Response does not contain 'name'"

# teste id-2
@pytest.mark.django_db
def test_pokemon_detail_id_2():
    client = Client()
    url = reverse('pokemon_detail', kwargs={'pokemon_id': 2})
    response = client.get(url)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert b'pokemon' in response.content, "Response does not contain 'pokemon'"
    assert b'name' in response.content, "Response does not contain 'name'"

# teste id-0
@pytest.mark.django_db
def test_pokemon_detail_id_0():
    client = Client()
    url = reverse('pokemon_detail', kwargs={'pokemon_id': 0})
    
    response = client.get(url)
    
    assert response.status_code == 200
    assert '<p class="pokemon__image">Pokemon não encontrado.</p>' in response.content.decode('utf-8')

# teste id-1025
@pytest.mark.django_db
def test_pokemon_detail_id_1025():
    client = Client()
    url = reverse('pokemon_detail', kwargs={'pokemon_id': 1025})
    response = client.get(url)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert b'pokemon' in response.content, "Response does not contain 'pokemon'"
    assert b'name' in response.content, "Response does not contain 'name'"

# teste id-1024
@pytest.mark.django_db
def test_pokemon_detail_id_1024():
    client = Client()
    url = reverse('pokemon_detail', kwargs={'pokemon_id': 1024})
    response = client.get(url)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert b'pokemon' in response.content, "Response does not contain 'pokemon'"
    assert b'name' in response.content, "Response does not contain 'name'"

# teste id-1026
@pytest.mark.django_db
def test_pokemon_detail_id_1026():
    client = Client()
    url = reverse('pokemon_detail', kwargs={'pokemon_id': 1026})
    
    response = client.get(url)
    
    assert response.status_code == 200
    assert '<p class="pokemon__image">Pokemon não encontrado.</p>' in response.content.decode('utf-8')