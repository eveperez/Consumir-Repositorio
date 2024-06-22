
import requests
import json


#Get como cliente, obtenemos un json

if __name__== '__main__':
    # url = 'https://www.google.com.mx/'
    url = 'https://httpbin.org/get?nombre=evelin&curso=python'
    args = {'nombre': 'Evelin', 'curso': 'python', 'nivel': '1'}
    response = requests.get(url, params=args)
    print(response)

    # response = requests.get(url)

    if response.status_code == 200:

        # content = response.content #Obtener el contenido de la pagina

        # file = open('google.html', 'wb') #abrir archivo
        # file.write(content) #escribir archivo
        # file.close()  #cerrar archivo

        # OTRA FORMA
        # response_json = response.json() #Diccionario que se convierte a json
        # origin = response_json['origin']
        # print(origin)

        # OTRA FORMA
        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(origin)

