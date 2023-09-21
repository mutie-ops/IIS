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
        "EmployeeCode": "EOO12",
        "CompanyCode": "FINTECH",
        "DateEngaged": "2/1/2023 12:00:00 AM",
        "JobTitleTypeCode": "SA",
        "JobGradeCode": "AA",
        "DateJoinedGroup": "2/1/2023 12:00:00 AM",
        "LeaveStartDate": "2/1/2023 12:00:00 AM",
        "EntityCode": "1223",
        "TaxNo": "g45643663b56",
        "TitleTypeCode": "MR",
        "Initials": "B",
        "FirstName": "Caleb",
        "KnownAsName": "Caleb",
        "LastName": "Muinde",
        "IDNumber": "453443543245",
        "BirthDate": "10/12/1958 12:00:00 AM",
        "Gender": "M",
        "LanguageTypeCode": "ENG",
        "NationalityCountryCode": "KEN",
        "Disabled": "False",
        "CompanyRuleCode": "FINTECH_PAY",
        "HoursPerPeriod": "193.0000",
        "HoursPerDay": "8.0000",
        "AnnualSalary": "480000.0000",
        "PeriodSalary": "40000.0000",
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
                "AccountName": "Mr M Mutisya",
                "BankCode": "3",
                "AccountTypeCode": "CA",
                "AccountNo": "4677844634",
                "BankBranchCode": "340",
                "Ccy": "KES",
                "DefaultInd": "True"
            }
        ],
        "DriversLicenses": [],
        "Hierarchies": [],
        "GenericFields": []
    })

    response = requests.request('POST',url=url, headers=header,data=payload)
    print(response.text)


create_employee()