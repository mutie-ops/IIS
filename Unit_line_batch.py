# we are going to create unit line batches
import pandas as pd
from Authorization import cookies
import requests
import json
import random
import string


def get_unit_batch_template_details():
    global s_desc, l_des, temp_id, temp_code
    url = 'http://localhost:9000/api/apibase/ULBATCH/UnitLineBatchTemplateDetails'
    headers = {'Cookie': cookies}
    payload = {}

    response = requests.request('GET', url=url, headers=headers, data=payload)
    # print(response.text)

    for template in response.json()['data']:
        temp_id = template["unitLineBatchHeaderTemplateID"]
        temp_code = template["code"]
        s_desc = template["shortDescription"]
        l_des = template["longDescription"]

    return temp_id, temp_code, s_desc, l_des


def batch_normal_line_type():
    excel_data = pd.read_excel('C:\\Users\\HP\\PycharmProjects\\IIS\output_excel_file4.xlsx')
    employee_list = []
    payroll_def_codes = ['BASIC_SALARY', 'OVERTIME_1_5', 'OVERTIME_2_0']
    for payroll_def_code in payroll_def_codes:
        if 'OVERTIME_1_5' == payroll_def_code:
            units_payroll = 'Overtime 1.5'
        elif 'OVERTIME_2_0' == payroll_def_code:
            units_payroll = 'Overtime 2.0'
        else:
            units_payroll = 'Days Worked'
        for index, row in excel_data.iterrows():
            employee_code = row['Employee ID']
            date_worked = row['Date Worked']
            units = row[units_payroll]
            # employeerate = row['employeerate']

            field_list = [
                {
                    "companyruleCode": "SKANEM_PAY",
                    "payRunDefCode": "MAIN",
                    "LineType": "EA",
                    "payrollDefCode": payroll_def_code,
                    "dateWorked": date_worked.strftime('%Y-%m-%d %H:%M:%S'),
                    "Units": units,
                    "chargeoutrate": 0,

                }
            ]

            employee_entry = {
                "employeeCode": employee_code,
                "fieldList": field_list
            }

            employee_list.append(employee_entry)

    _data = get_unit_batch_template_details()
    random_codes = ''.join(random.choices(string.ascii_uppercase, k=4))
    url = 'http://localhost:9000/api/apibase/ULBATCH/create'
    header = {
        'Content-Type': 'application/json',
        'Cookie': cookies}

    payload = json.dumps({
        "unitLineBatchHeaderTemplateID": _data[0],
        "code": '{}'.format(random_codes),
        "shortDescription": _data[2],
        "longDescription": _data[3],
        "employeeList": employee_list
    })

    response = requests.request('POST', url=url, headers=header, data=payload)
    # print(response.text)
    success = response.json()['success']
    return success

def send_email():
    from Email_Services import create_message
    success_response = batch_normal_line_type()
    message = ('UNIT LINE BATCH UPDATE IS SUCCESSFUL,'
               'Awaiting verification and processing')
    to = 'mutie.mutisya@gravitysolutions.net'
    subject = 'SUCCESSFUL BATCH UPDATE'
    if success_response:
        create_message(message=message, to=to, subject=subject)
    else:
        create_message(message='UNIT LINE BATCH UPDATE FAILED', to=to, subject='FAILED BATCH UPDATE')


send_email()
