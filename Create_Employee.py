from Authorization import cookies
import requests
import json

print(cookies)


def create_employee():
    url = f'http://localhost:9000/api/apibase/employee'

    header = {
        'Content-Type': 'application/json',
        'Cookie': cookies
    }

    payload = json.dumps({
        "EmployeeCode": "EOO13",
        "CompanyCode": "FINTECH",
        "DateEngaged": "2/1/2023 12:00:00 AM",
        "JobTitleTypeCode": "",
        "JobGradeCode": "",
        "DateJoinedGroup": "2/1/2023 12:00:00 AM",
        "LeaveStartDate": "2/1/2023 12:00:00 AM",
        "EntityCode": "1563",
        "TaxNo": "g45645643b56",
        "TitleTypeCode": "MR",
        "Initials": "Z",
        "FirstName": "Zachery",
        "KnownAsName": "Zachery",
        "LastName": "Muindo",
        "IDNumber": "45gfg543245",
        "BirthDate": "10/12/1995 12:00:00 AM",
        "Gender": "M",
        "LanguageTypeCode": "ENG",
        "NationalityCountryCode": "KEN",
        "Disabled": "False",
        "CompanyRuleCode": "FINTECH_PAY",
        "HoursPerPeriod": "",
        "HoursPerDay": "",
        "AnnualSalary": "",
        "PeriodSalary": "60000.0000",
        "OverrideAnnualBonusCalcRecurrence": "False",
        "CalendarMonth": "12",
        "PeriodInMonth": "L",
        "RatePerDay": "2072.5392",
        "RatePerHour": "259.0674",
        "PensionFundStartDate": "2/2/2023 12:00:00 AM",
        "ZoneCodes": "",
        "RemunerationDefinitionHeaderCode": "BASIC_SALARY_RE",
        "PaymentRunDefCode": "CHEQ",
        "SDLExempt": "False",
        "LegallyRetiredforTaxPurpose": "False",
        "ForeignIncome": "False",
        "TaxStatusCode": "ST",
        "TaxStartDate": "2/1/2023 12:00:00 AM",
        "TaxCalculation": "A",
        "LeavePolicyCode": "ANNUAL",
        "Addresses": [],
        "Contacts": [],
        "BankAccounts": [
            {
                "AccountHolderRelationship": "O",
                "AccountName": "Mr Z Muindo",
                "BankCode": "3",
                "AccountTypeCode": "CA",
                "AccountNo": "467646566634",
                "BankBranchCode": "340",
                "Ccy": "KES",
                "DefaultInd": "True"
            }
        ],
        "DriversLicenses": [],
        "Hierarchies": [],
        "GenericFields": []
    })

    response = requests.request('POST', url=url, headers=header, data=payload)
    print(response.text)


create_employee()
