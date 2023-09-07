import requests
import time
import random
from requests.exceptions import ConnectionError

# generating an access token
def generate_token():
    url = 'http://DESKTOP-LJL56QO:9443/token'

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate'
    }

    data = {'grant_type': 'password',
            # 'username': 'Admin',
            # 'password': 'a',
            'scope': 'apiKey=bc4acf10-16eb-4f8b-8bba-160d5a30908b'

            }
    # this will take an random time beween 3 and 8 seconds before retrying
    time_inactive_before_retry = random.randint(3,8)
    # this is the number of retires to be made
    MAX_RETRIES = 5
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.post(url=url, headers=headers, data=data)
            response.raise_for_status()
            break
        except ConnectionError as ce:
            print(f"Connection error (attempt {attempt + 1}/{MAX_RETRIES}): {ce}")
            if attempt <  MAX_RETRIES -1:
                time.sleep(time_inactive_before_retry)
                print("Retrying...")
            else:
                print("Max retries reached,unable to connect:\n",ce)
        except requests.RequestException as re:
            print(f"Request error (attempt {attempt + 1}/{MAX_RETRIES}): {re}")

            if attempt < MAX_RETRIES -1:
                time.sleep(time_inactive_before_retry)
                print("Retrying....")
            else:
                print( print("Max retries reached,unable to connect:\n",re))
        except Exception as e:
                print(e)
                break


token = generate_token()

print("token generated", token)
