import requests
import json

base_url="https://reqres.in"
response=requests.get(base_url+'/api/users/2') # response will return object type data

#data=response.json()
with open ('get_data.json','w') as obj:
    json.dump(response.json(),obj)
#
# with open ('get_data.json','r') as fo:
#     data=json.load(fo)

    # for val in data:
    #     print(val[])
print(response.status_code)
