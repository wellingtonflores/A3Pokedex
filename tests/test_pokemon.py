import pytest
from django.test import Client
from django.urls import reverse
from faker import Faker

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

#teste com ids aleatorios
fake = Faker()

def test_pokemon_detail_random_ids():
    client = Client()
    generated_ids = []
    
    for _ in range(5):
        random_id = fake.random_int(min=1, max=1025)
        generated_ids.append(random_id)
        url = reverse('pokemon_detail', kwargs={'pokemon_id': random_id})
        response = client.get(url)
        
        assert response.status_code == 200 or response.status_code == 404
        if response.status_code == 200:
            assert 'Pokemon não encontrado.' not in response.content.decode('utf-8')
        else:
            assert '<p class="pokemon__image">Pokemon não encontrado.</p>' in response.content.decode('utf-8')
    
    print("Generated IDs:", generated_ids)

#teste botao prev_pokemon
@pytest.mark.django_db
def test_prev_pokemon_button(client):
    
    response = client.post('/pokemon/1/', {'prev_pokemon': True, 'pokemon_id': 2})
    
    assert response.status_code == 302 
    assert response.url == '/pokemon/1/'  

#teste botao next_pokemon
@pytest.mark.django_db
def test_next_pokemon_button(client):
    
    response = client.post('/pokemon/1/', {'next_pokemon': True, 'pokemon_id': 2})
   
    assert response.status_code == 302  
    assert response.url == '/pokemon/3/'  

#teste botao search_pokemon
@pytest.mark.django_db
def test_search_pokemon_button(client):
    response = client.post('/pokemon/1/', {'search_pokemon': 'bulbasaur'})
    assert response.status_code == 302
    assert response.url == '/pokemon/1/'