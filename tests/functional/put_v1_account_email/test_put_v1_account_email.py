# HOMEWORK 1

import pprint

from json import loads

import pytest

from api_class_client.class_client import (
    ApiClassClient,
    get_activation_token_by_login,
)
from conftest import user_data
@pytest.mark.skip
def test_put_account_email(user_data):
    """
    PUT
    /v1/account/email
    Change registered user email
    :param user_data:
    :return:
    """
    mailhog_api = ApiClassClient(host='http://5.63.153.31:5025')
    class_client_api = ApiClassClient(host='http://5.63.153.31:5051')
    # создание пользователя
    response = class_client_api.post_v1_account(json_data=user_data)
    assert response.status_code == 201, f"Status code: {response.status_code}"
    # получение письма из почтового сервера
    response = mailhog_api.get_api_v2_messages(limit=100)
    print(response.status_code)
    print(response.text)
    pprint.pprint(response.json)
    assert response.status_code == 200, f"Status code: {response.status_code}"
    # получение токена
    token = get_activation_token_by_login(user_data['login'], response)
    print(token)
    assert token is not None, f"Token {user_data['login']} not found"
    # активация пользователя
    response = class_client_api.put_v1_account_token(token=token)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, f"user not activated: {response.status_code}"

    # авторизоваться
    response = class_client_api.post_v1_account_login(json_data={
        'login': user_data['login'],
        'password': user_data['password'],
        'rememberMe': True,
    })
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, f"user cant authorize: {response.status_code}"
    # TODO: не доделаны шаги
    #  - Меняем емейл
    #  - Пытаемся войти, получаем 403 -
    #  - На почте находим токен по новому емейлу для подтверждения смены емейла
    #  - Активируем этот токен -
    #  - Логинимся