import pprint

import requests
from json import loads

def test_post_v1_account():
    # регистрация пользователя
    login = "vmenshikov_test666"
    email = f"{login}@mail.ru"
    password = "123456789"
    json_data = {
        "login": login,
        "email": email,
        "password": password,
    }
    responce = requests.post("http://5.63.153.31:5051/v1/account", json=json_data)
    print(responce.status_code)
    print(responce.text)
    assert responce.status_code == 201, f"Status code: {responce.status_code}"
    # получить письма из почтового сервера

    params = {
        'limit': '50',
    }

    response = requests.get('http://5.63.153.31:5025/api/v2/messages', params=params, verify=False)
    print(response.status_code)
    print(response.text)
    pprint.pprint(response.json)
    assert responce.status_code == 200, f"Status code: {responce.status_code}"

    token = None
    # получить активационный токен
    for item in response.json()['items']:
        user_data = loads(item["Content"]["Body"])
        user_login = user_data["login"]
        # получаем токен из словаря
        if user_login == login:
            print(user_login)
            token = user_data["ConfirmationLinkUrl"].split("/")[-1]
            print(token)
    assert token is not None, f"Token not found"
    # активация пользователя
    headers = {
        'accept': 'text/plain',
    }
    response = requests.put(f'http://5.63.153.31:5051/v1/account/{token}', headers=headers)
    print(response.status_code)
    print(response.text)
    assert responce.status_code == 200, f"user not activated: {responce.status_code}"
    # авторизоваться
    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }
    response = requests.post('http://5.63.153.31:5051/v1/account/login', json=json_data)
    print(response.status_code)
    print(response.text)
    assert responce.status_code == 200, f"user can't authorize: {responce.status_code}"
