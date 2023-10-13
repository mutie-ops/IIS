from Authorization import cookies
import json
import requests

file_path = 'C:\\Users\\Benjamin Mutie\\Desktop\\IIS\\employee_Line.json'


def get_employee_line_header():
    url = "http://localhost:9000/api/apibase/Header/EMPLOYEE/C"
    header = {
        'Cookie': cookies
    }
    payload = {}
    response = requests.request('POST', url=url, headers=header, data=payload)

    print(response.text)
    DATA = response.json()
    return DATA['data']['apiObjectID']


header_id = get_employee_line_header()


def create_employee():
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    url = f'http://localhost:9000/api/apibase/line/{header_id}/E'

    header = {
        'Cookie': cookies
    }
    payload = data
    response = requests.request('POST', url=url, headers=header, data=payload)
    print('respose2',response.text)


create_employee()

# validating_header