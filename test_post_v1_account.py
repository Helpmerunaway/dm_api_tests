import requests


def test_post_v1_account():
    # регистрация пользователя
    login = "vmenshikov_test"
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
    # получить письма из почтового сервера

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US, en; q=0.9',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0(Macintosh; Intel Mac OS X 10_15_7) AppleWebkit/537.36 (KHTML like Gecko) Chrome / 122.0.0.0 Safari /537.36',
    }
    params = {
        'limit': '50',
    }

    response = requests.get ('http://5.63.153.31:5025/api/v2/messages', params=params, verify=False)
    print(responce.status_code)
    print(responce.text)
    # получить активационный токен
    ...
    headers = {
        'accept': 'text/plain',
    }
    response = requests.put('http://5.63.153.31:5051/v1/account/dd4ed1b4-0f8c-465-8447-271fb81eeee1', headers=headers)
    # авторизоваться
    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }
    response = requests.post('http://5.63.153.31:5051/v1/account/login', json=json_data)
    print(responce.status_code)
    print(responce.text)