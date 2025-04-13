import pprint

import requests

url = 'http://5.63.153.31:5051/v1/account'
headers = {
    "accept": "*/*",
    "Content-type": "application/json"

}

json = {
    "login": "vmenshikov_test2",
    "email": "vmenshikov_test2@mail.ru",
    "password": "123456789"
}

responce = requests.post(
    url=url,
    headers=headers,
    json=json
)
print(responce.status_code) # 201
#pprint.pprint(responce.json())

# activate user
url = 'http://5.63.153.31:5051/v1/account/dd4ed1b4-0f8c-4e65-8447-271fb81eeee1'
headers = {
    "accept": "text/plain"

}

responce = requests.put(
    url=url,
    headers=headers
)
print(responce.status_code) # 200
pprint.pprint(responce.json())
responce_json = responce.json()
print(responce_json["resource"]["rating"]["quantity"]) # 0