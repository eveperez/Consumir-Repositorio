import requests
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    client_id = os.getenv('client_id')
    client_secret = os.getenv('client_secret')

    print(f"Client ID: {client_id}")
    print(f"Client Secret: {client_secret}")

    # https://github.com/login/oauth/authorize?client_id=''&scope=repo

    code = ''
    # Permite obtener casi toda la informacion del usuario
    access_token = ''

    url = 'https://api.github.com/user/repos'
    payload = {'name': 'git_api_cf_comunidad'}
    headers = {'Accept': 'application/json', 'Authorization': 'token ' + access_token}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print(response.json())
    else:
        print(response.content)
