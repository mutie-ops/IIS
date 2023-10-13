import requests


def generate_token():
    url = "http://localhost:9000/token"
    payload = 'grant_type=password&username=Admin&password=a&scope=apiKey%3D9785869f-8d94-465d-97fa-62c7e330643e'
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
