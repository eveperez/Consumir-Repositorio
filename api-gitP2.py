import requests
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

print(f"Client ID: {client_id}")
print(f"Client Secret: {client_secret}")

# https://github.com/login/oauth/authorize?client_id=Ov23liPI6WxSMWMDp0cv&scope=respo

code = '656cb2b0a01848a386fe'
# Permite obtener casi toda la informacion del usuario
access_token = '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'

if __name__ == '__main__':
    # Peticion para obtener los repositorios
    url = 'https://api.github.com/user/repos'

    headers = {'Authorization': 'token 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'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        payload = response.json()

        for project in payload:
            name = project['name']
            print(name)
    else:
        print(response.content)