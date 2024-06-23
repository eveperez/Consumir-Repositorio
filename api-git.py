import requests
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

print(f"Client ID: {client_id}")
print(f"Client Secret: {client_secret}")

# https://github.com/login/oauth/authorize?client_id=Ov23liPI6WxSMWMDp0cv&scope=repo

code = '45ae90306c5a35da4eeb'
# Permite obtener casi toda la informacion del usuario
access_token = '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'

if __name__ == '__main__':
    url = 'https://github.com/login/oauth/access_token'
    payload = {'client_id': client_id, 'client_secret': client_secret, 'code': code}
    headers = {'Accept': 'application/json'}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_json = response.json()
        access_token = response_json['access_token']
        print(access_token)
    else:
        print(response.content)
        print(response.text)

