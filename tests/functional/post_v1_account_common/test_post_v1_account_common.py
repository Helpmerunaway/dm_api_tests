import pprint

from json import loads

from dm_api_account.apis.account_api import AccountApi
from dm_api_account.apis.login_api import LoginApi
from api_mailhog.apis.mailhog_api import MailhogApi
from faker import Faker

fake = Faker(['en-US'])
def test_post_v1_account():
    account_api = AccountApi(host='http://5.63.153.31:5051')
    login_api = LoginApi(host='http://5.63.153.31:5051')
    mailhog_api = MailhogApi(host='http://5.63.153.31:5025')
    # регистрация пользователя

    login = fake.first_name() + fake.last_name()
    email = fake.free_email()
    password = "123456789"
    json_data = {
        "login": login,
        "email": email,
        "password": password,
    }
    response = account_api.post_v1_account(json_data=json_data)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 201, f"Status code: {response.status_code}"
    # получить письма из почтового сервера

    response = mailhog_api.get_api_v2_messages(limit=50)
    print(response.status_code)
    print(response.text)
    pprint.pprint(response.json)
    assert response.status_code == 200, f"Status code: {response.status_code}"

    token = get_activation_token_by_login(login, response)
    assert token is not None, f"Token not found"
    # активация пользователя
    response = account_api.put_v1_account_token(token=token)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, f"user not activated: {response.status_code}"
    # авторизоваться
    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }
    response = login_api.post_v1_account_login(json_data=json_data)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, f"user can't authorize: {response.status_code}"


def get_activation_token_by_login(
        login,
        response
        ):
    token = None
    for item in response.json()['items']:
        body = item['Content']['Body']
        try:
            user_data = loads(body)
            user_login = user_data.get('Login')
            if user_login == login:
                token = user_data['ConfirmationLinkUrl'].split('/')[-1]
                break
        except ValueError:
            for line in body.splitlines():
                if 'ConfirmationLinkUrl' in line:
                    token = line.split('/')[-1].strip()
                    break

    if not token:
        raise ValueError(f'Не удалось найти токен активации для пользователя {login}')

    return token





