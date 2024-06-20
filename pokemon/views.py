# pokemon/views.py
from django.shortcuts import render, redirect
import requests

def pokemon_detail(request, pokemon_id):
    if request.method == 'POST':
        if 'prev_pokemon' in request.POST:
            pokemon_id = int(request.POST.get('pokemon_id')) - 1
        elif 'next_pokemon' in request.POST:
            pokemon_id = int(request.POST.get('pokemon_id')) + 1
        elif 'search_pokemon' in request.POST:
            pokemon_id_or_name = request.POST.get('search_pokemon')
            if pokemon_id_or_name.isdigit():
                pokemon_id = int(pokemon_id_or_name)
            else:
                try:
                    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id_or_name.lower()}/')
                    response.raise_for_status()
                    pokemon_data = response.json()
                    pokemon_id = pokemon_data['id']
                except requests.exceptions.RequestException as e:
                    print("Pokemon não encontrado")
                    return render(request, 'index.html', {'pokemon': None})
        return redirect('pokemon_detail', pokemon_id=pokemon_id)

    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/')
        response.raise_for_status()
        pokemon_data = response.json()
        animated_front_default = None
        if 'versions' in pokemon_data['sprites']:
            generation_v = pokemon_data['sprites']['versions'].get('generation-v')
            if generation_v and 'black-white' in generation_v:
                black_white = generation_v['black-white']
                if 'animated' in black_white:
                    animated_front_default = black_white['animated'].get('front_default')
        
        pokemon_data['animated_front_default'] = animated_front_default
        
        return render(request, 'index.html', {'pokemon': pokemon_data})
    except requests.exceptions.RequestException as e:
        print(e)
        return render(request, 'index.html', {'pokemon': None})
