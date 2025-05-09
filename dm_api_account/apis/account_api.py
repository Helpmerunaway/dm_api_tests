import requests


class AccountApi:
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
