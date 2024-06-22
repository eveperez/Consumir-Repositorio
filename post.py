import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/post'
    payload = {'nombre': 'Evelin', 'curso': 'python', 'nivel': '1'}
    response = requests.post(url, data=json.dumps(payload)) # Colocar diccionario, se van a mandar dentro del atributo data

    # json post se encarga de serializarlos
    # En caso contrari, serializa diccionario en data

    print(response)

    # response = requests.get(url)

    if response.status_code == 200:
        print(response.content)
