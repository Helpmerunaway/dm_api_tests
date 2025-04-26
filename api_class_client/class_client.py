import requests
from json import loads

def get_activation_token_by_login(
        login,
        response
        ):
    token = None
    for item in response.json()['items']:
        body = item['Content']['Body']
        try:
            user_data_body = loads(body)
            user_login = user_data_body.get('Login')
            if user_login == login:
                token = user_data_body['ConfirmationLinkUrl'].split('/')[-1]
                break
        except ValueError:
            for line in body.splitlines():
                if 'ConfirmationLinkUrl' in line:
                    token = line.split('/')[-1].strip()
                    break

    if not token:
        raise ValueError(f'Cant find token {login}')

    return token


class ApiClassClient:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers

    def post_v1_account(
            self,
            json_data
        ):
        """
        Account
        POST
        /v1/account
        Register new user
        :param json_data:
        :return:
        """
        responce = requests.post(
            url=f"{self.host}/v1/account",
            json=json_data)
        return responce

    def put_v1_account_token(
            self,
            token
        ):
        """
        PUT
        /v1/account/{token}
        Activate registered user
        :param token:
        :return:
        """
        headers = {
            'accept': 'text/plain',
        }
        response = requests.put(
            url=f'{self.host}/v1/account/{token}',
            headers=headers
            )
        return response

    def post_v1_account_login(
            self,
            json_data
            ):
        """
        POST
        /v1/account/login
        Authenticate via credentials
        :param json_data:
        :return:
        """
        response = requests.post(
            url=f'{self.host}/v1/account/login',
            json=json_data
            )
        return response

    def get_api_v2_messages(
            self,
            limit=50
    ):
        """
        Get users
        :return:
        """
        params = {
            'limit': limit,
        }
        response = requests.get(
            url=f'{self.host}/api/v2/messages', params=params,
            verify=False
            )
        return response