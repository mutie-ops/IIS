import requests
from Authorization import cookies
import http.cookies


def create_headers(header):
    url = f"http://localhost:9000/api/apibase/Header/{header}"
    payload = {}

    # Extracting the cookie
    cookie = http.cookies.SimpleCookie(cookies)
    people_ess = cookie.get('PeopleEssUser').value
    xsrf = cookie.get('XSRF-TOKEN').value

    headers = {
                'Cookie': f'PeopleEssUser={people_ess}; XSRF-TOKEN={xsrf}'
              }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


create_headers(header='EMPLOYEE')
