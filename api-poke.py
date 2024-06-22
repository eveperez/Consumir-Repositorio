import requests

def get_pokemonts(url='https://pokeapi.co/api/v2/pokemon-form/', offset=0):
    # Definir una variable en caso contrario
    args = {'offset': offset} if offset else {}
    response = requests.get(url)

    # Enlistarlos
    if response.status_code == 200:
        # Obtener json de Api
        payload = response.json()
        # Obtener el result, en caso contrario lista vacia
        results = payload.get('results', [])

        # Result lleno
        if results:
            for pokemon in results:
                name = pokemon['name']
                print(name)

        next = input("Continuar listado? [Y/N] ").lower() #Lower = pone las letraes en minusculas
        if next == 'y':
            get_pokemonts(offset=offset+20)

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon-form/'
    get_pokemonts()

"""
if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon-form/' # Lista de pokemons

    # Poner la cantidad de pokemones que queremos obtenener
    args = {'offset': 0, 'limit': 100}
    response = requests.get(url,params=args)

    # Enlistarlos
    if response.status_code == 200:
        # Obtener json de Api
        payload = response.json()
        # Obtener el result, en caso contrario lista vacia
        results = payload.get('results', [])

        # Result lleno
        if results:
            for pokemon in results:
                name = pokemon['name']
                print(name)
                            
"""