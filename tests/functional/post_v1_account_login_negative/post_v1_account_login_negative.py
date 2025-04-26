# HOMEWORK 1

import pprint

from json import loads
from api_class_client.class_client import (
    ApiClassClient,
    get_activation_token_by_login,
)
from conftest import user_data

def test_negative_account_login(user_data):
    """
    Login
    POST
    /v1/account/login
    Authenticate via credentials without activation
    :param user_data:
    :return:
    """
    class_client_api = ApiClassClient(host='http://5.63.153.31:5051')
    # создание пользователя
    response = class_client_api.post_v1_account(json_data=user_data)
    assert response.status_code == 201, f"Status code: {response.status_code}"
    # авторизоваться
    response = class_client_api.post_v1_account_login(json_data={
        'login': user_data['login'],
        'password': user_data['password'],
        'rememberMe': True,
    })
    print(response.status_code)
    print(response.text)
    assert response.status_code == 403, f"user can authorize without activating: {response.status_code}"
