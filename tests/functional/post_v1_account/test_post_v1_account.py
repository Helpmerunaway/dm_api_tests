# HOMEWORK 1

import pprint

from json import loads
from api_class_client.class_client import (
    ApiClassClient,
    get_activation_token_by_login,
)
from conftest import user_data


def test_register_new_user(user_data):
    """
    POST
    /v1/account
    Register new user
    :param user_data:
    :return:
    """
    class_client_api = ApiClassClient(host='http://5.63.153.31:5051')
    response = class_client_api.post_v1_account(json_data=user_data)
    print(response.status_code)
    print(user_data)
    assert response.status_code == 201, f"Status code: {response.status_code}"