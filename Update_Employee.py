from Authorization import cookies
import requests
import json

file_path = 'C:\\Users\\Benjamin Mutie\\Desktop\\IIS\\employee_data.json'


def get_employees():
    url = "http://localhost:9000/api/apibase/employee/Get/1"
    headers = {'Content-Type': 'application/json',
               'Cookie': cookies
               }
    payload = {}

    response = requests.request('POST', url=url, headers=headers, data=payload)
    print(response.text)
    # data = response.json()
    # with open(file_path, 'w') as json_file:
    #     json.dump(data, json_file)
    #
    # print(data)

get_employees()
def update_employee():
    url = "http://localhost:9000/api/apibase/employee/put"
    headers = {'Content-Type': 'application/json',
               'Cookie': cookies
               }
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    payload = json.dumps(data)

    response = requests.request('POST', url=url, headers=headers, data=payload)
    print(response.text)

update_employee()