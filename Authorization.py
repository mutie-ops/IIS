import requests
import time
import random
from requests.exceptions import ConnectionError


# generating an access token
def generate_token():
    url = 'http://localhost:9000/token'

    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Accept': 'application/json',

    }

    data = {'grant_type': 'password',
            # 'username': 'admin',
            # 'password': 'a',
            'scope': 'apikey=04284baa-8323-4775-913f-beaffa7664d8'
            }

    # response = requests.post(url=url, headers=headers,data=data)
    # response_status = response.raise_for_status()
    # print('response status:', response.json())
    #
    # print('response status:', response_status)

    # this will take an random time between 3 and 8 seconds before retrying
    time_inactive_before_retry = random.randint(3, 5)
    # this is the number of retires to be made
    MAX_RETRIES = 3
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.post(url=url, headers=headers ,data=data)
            print('response status:', response.json())
            return response.json()

        except ConnectionError as ce:
            print(f"Connection error (attempt {attempt + 1}/{MAX_RETRIES}): {ce}")
            if attempt < MAX_RETRIES - 1:
                print("Retrying...")
                time.sleep(time_inactive_before_retry)

            else:
                print("Max retries reached,unable to connect:\n", ce)

        except requests.RequestException as re:
            print(f"Request error (attempt {attempt + 1}/{MAX_RETRIES}): {re}")

            if attempt < MAX_RETRIES - 1:
                print("Retrying....")
                time.sleep(time_inactive_before_retry)
            else:
                print("Max retries reached,unable to connect:\n", re)
        except Exception as e:
            print(e)
            break



token = generate_token()

print("token generated", token)
