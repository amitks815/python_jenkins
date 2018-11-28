import requests
import json

base_url="https://reqres.in"
dataload={
    "name": "amit",
    "job": "singh"
}

response=requests.put(base_url+'/api/users/2',data=dataload)

print(response.json())

print(response.status_code)
