import requests


def generate_token():
    url = "http://localhost:9000/token"

    payload = 'grant_type=password&username=Admin&password=a&scope=apiKey%3D0c4a0f04-6a8f-4c07-8767-2c8cf6eafa87'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.headers['set-Cookie']


cookies = generate_token()
