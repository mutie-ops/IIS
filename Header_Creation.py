import requests
from Authorization import cookies

def create_headers(header):
    url = f"http://localhost:9000/api/apibase/Header/{header}"
    payload = {}
    headers = {
        'Cookie': cookies
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    data = response.json()

    api_object_id = data['data']['apiObjectID']
    print(api_object_id)
    return api_object_id


header_ = 'REPORTSTOEMP'
object_id = create_headers(header=header_)

