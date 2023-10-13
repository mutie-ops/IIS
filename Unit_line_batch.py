# we are going to create unit line batches
from Authorization import cookies
import requests
import json
import random
import string


def get_unit_batch_template_details():
    url = 'http://localhost:9000/api/apibase/ULBATCH/UnitLineBatchTemplateDetails'
    headers = {'Cookie': cookies}
    payload = {}

    response = requests.request('GET', url=url, headers=headers, data=payload)
    print(response.text)
    return response.text


# get_unit_batch_details()
def get_batch_header_instance_details():
    global HEADER_DETAILS, CODE, SHORT_DESC, LONG_DESC, EMPLOYEE_ID, EMPLOYEE_CODE, EMPLOYEE_NAME, LINE_TYPE, PAYROLL_DEF, DATE_WORKED
    url = 'http://localhost:9000/api/apibase/ULBATCH/UnitLineBatchHeaderDetails'
    headers = {'Cookie': cookies}
    payload = {}

    response = requests.request('GET', url=url, headers=headers, data=payload)

    print(response.text)
    response_data = response.json()['data']

    SELECTED_HEADER = []

    for header_details in response_data:
        HEADER_DETAILS = header_details.get("unitLineBatchHeaderID")
        if HEADER_DETAILS == 2:
            SELECTED_HEADER.append(header_details)

    print(SELECTED_HEADER)
    for details in SELECTED_HEADER:
        CODE = details.get('code')
        SHORT_DESC = details.get('shortDescription')
        LONG_DESC = details.get('longDescription')
        employee_list = details.get('employeeList')
        for employee_details in employee_list:
            EMPLOYEE_ID = employee_details.get('employeeID')
            EMPLOYEE_CODE = employee_details.get('employeeCode')
            EMPLOYEE_NAME = employee_details.get('employeeDisplayName')
            field_list = employee_details.get('fieldList')
            # print("field_list",field_list)

            for fields in field_list:
                # print(fields.get('companyruleCode'))
                # print(fields.get("payRunDefID"))
                LINE_TYPE = fields.get("lineType")
                PAYROLL_DEF = fields.get("payrollDefCode")
                DATE_WORKED = fields.get("dateWorked")
                # print(fields.get("Units"))
                # print(fields.get("inputAmount"))
                # print(fields.get("chargeoutrate"))
                # print(fields.get("jobcostcode"))
                # print(fields.get("note"))
                # print(fields.get("employeerate"))

    return (HEADER_DETAILS, CODE, SHORT_DESC, LONG_DESC, EMPLOYEE_ID,
            EMPLOYEE_CODE, EMPLOYEE_NAME, LINE_TYPE, PAYROLL_DEF, DATE_WORKED)


def post_normal_unit_batch():
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(5))

    url = "http://localhost:9000/api/apibase/ULBATCH/create"
    headers = {
        'Content-Type': 'application/json',
        'Cookie': cookies}
    payload = json.dumps({
        "unitLineBatchHeaderTemplateID": 2,
        "code": random_string.upper(),
        "shortDescription": "Overtime batch",
        "longDescription": "Overtime batch",
        "employeeList": [
            {
                "employeeCode": "E006",
                "fieldList": [
                    {
                        "companyruleCode": "ECO_PAY",
                        "payRunDefCode": "MAIN",
                        "LineType": "EA",
                        "payrollDefCode": "OVERTIME_1_5",
                        "dateWorked": "2023-07-01T00:00:00",
                        "Units": 10,
                        "inputAmount": "",
                        "chargeoutrate": 0,
                        "jobcostcode": "",
                        "note": "",
                        "employeerate": ""
                    }
                ]
            }
        ]
    })
    response = requests.request('POST', url=url, headers=headers, data=payload)
    print(response.text)
    return response.json()['data']


DATA = post_normal_unit_batch()


# verifying
def verify_unit_batch():
    url = "http://localhost:9000/api/apibase/ULBATCH/verify"
    headers = {
        'Content-Type': 'application/json',
        'Cookie': cookies}
    payload = json.dumps({
        "unitLineBatchHeaderID": DATA['unitLineBatchHeaderID'],
        "Code": DATA['code']
    })

    response = requests.request('POST', url=url, headers=headers, data=payload)
    print(response.text)


verify_unit_batch()


# PROCESS BATCH
def process_unit_batch():
    url = "http://localhost:9000/api/apibase/ULBATCH/process"

    headers = {
        'Content-Type': 'application/json',
        'Cookie': cookies}
    payload = json.dumps({
        "unitLineBatchHeaderID": DATA['unitLineBatchHeaderID'],
        "Code": DATA['code']
    })

    response = requests.request('POST', url=url, headers=headers, data=payload)
    print(response.text)


process_unit_batch()
