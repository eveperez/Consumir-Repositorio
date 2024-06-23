import requests

if __name__ == '__main__':
    url = 'https://api.github.com/user'

    session = requests.session()
    session.auth = ('@gmail.com', '')

    response = session.get(url)
    if response.ok:
        print(response.content)
    else:
        print(response.content)

        response = session.get('https://github.com/')
        if response.ok:
            print(response.cookies)

"""
    # Obtener cookies que mando el servidor
    url = 'http://httpbin.org/cookies'
    cookies = {'my-cookie': 'true'}

    response = requests.get(url, cookies=cookies)

    if response.ok:
        cookies = response.cookies
        print(cookies)

        print("El contenido es: ")
        print(response.content)

"""