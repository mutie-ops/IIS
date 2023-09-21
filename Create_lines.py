import requests
from Authorization import cookies
import json
import requests

url = "http://localhost:9000/api/apibase/Employee/Get/1009"

payload = {}
headers = {
          'Cookie': cookies
          }

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
