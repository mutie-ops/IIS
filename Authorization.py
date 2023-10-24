import requests


def generate_token():
    url = "http://localhost:9000/token"
    payload = 'grant_type=password&scope=apiKey%3Df0475c65-3a42-4d45-9ebd-4f3acbd37096'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        # print(response.text)
        # print(response.headers)
        return response.headers['set-Cookie']
    except Exception as e:
        print(e)


cookies = generate_token()
