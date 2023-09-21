import requests


def generate_token():
    url = "http://localhost:9000/token"

    payload = 'grant_type=password&username=Admin&password=a&scope=apiKey%3D0c4a0f04-6a8f-4c07-8767-2c8cf6eafa87'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        # print(response.text)
        return response.headers['set-Cookie']
    except Exception as e:
        print(e)


cookies = generate_token()
