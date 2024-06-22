import requests
import json

# PUT = para actualizar encabezados
# DELETE = Borrar encabezados

if __name__ == '__main__':
    url = 'https://httpbin.org/delete'
    payload = {'nombre': 'Evelin', 'curso': 'python', 'nivel': 'Intermedio'}

    # Para encabezados
    headers = {'Conten-Type': 'application/json', 'acces-token': '12345'}

    response = requests.delete(url, data=json.dumps(payload), headers=headers) # Colocar diccionario, se van a mandar dentro del atributo data

    print(response.url)

    # response = requests.get(url)

    if response.status_code == 200:
        # print(response.content)
        headers_response = response.headers #Diccionarios
        print(headers_response)
        server = headers_response['Server']
        print(server)