import pytest
from faker import Faker
fake = Faker(['en-US'])


@pytest.fixture()
def user_data():
    login = fake.first_name() + fake.last_name()
    email = fake.free_email()
    password = fake.password()
    return {'login': login, 'password': password, 'email': email}
    # json_data = {
    #     "login": login,
    #     "email": email,
    #     "password": password,
    # }
    # return json_data