import requests
import json

# Encabezados = cliente y servidor, obligados a enviar encabezados

if __name__ == '__main__':
    url = 'https://httpbin.org/post'
    payload = {'nombre': 'Evelin', 'curso': 'python', 'nivel': 'Intermedio'}

    # Para encabezados
    headers = {'Conten-Type': 'application/json', 'acces-token': '12345'}

    response = requests.post(url, data=json.dumps(payload), headers=headers) # Colocar diccionario, se van a mandar dentro del atributo data

    # json post se encarga de serializarlos
    # En caso contrario, data entonces los serializa

    print(response)

    # response = requests.get(url)

    if response.status_code == 200:
        # print(response.content)
        headers_response = response.headers #Diccionarios
        print(headers_response)
        server = headers_response['Server']
        print(server)



