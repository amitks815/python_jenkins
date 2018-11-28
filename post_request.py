import requests
import json

base_url="https://reqres.in"
dataload={
    "name": "amit",
    "job": "singh"
}

response=requests.post(base_url+'/api/users',data=dataload)

print(response.json())
print(response.status_code)
