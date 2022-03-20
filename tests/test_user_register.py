import pytest
import requests
from lib.base_case import BaseCase
from lib.Assertions import Assertions
from datetime import datetime

class TestUserRegister(BaseCase):
    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"

    def test_create_user_successfully(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email= 'vinkotov@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)


        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"



    def test_create_user_without_dog(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'namelogin.ru'
            }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        Assertions.assert_format_text(response, "Invalid email format")


    data1 = [({
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'name@login.ru'
            }),
        ({
            'password': '123',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'name@login.ru'
            }),
        ({
            'password': '123',
            'username': 'learnqa',
            'lastName': 'learnqa',
            'email': 'name@login.ru'
            }),
        ({
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'email': 'name@login.ru'
            }),
        ({
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa'
            }),
        ({
            'password': '123',
            'username': 'q',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'name@login.ru'
        }),
        ({
            'password': '123',
            'username': '12311111231313213213212332156487513211231231313213213212332156487513211231231313213213212332156487513211231231313213213212332156487513211231231313213213212332156487513211231231313213213212332156487513211231231313213213212332156487513211231231313213213212',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'name@login.ru'
        })
    ]
    @pytest.mark.parametrize ('data', data1)
    def test_create_user_without_params(self, data):
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)


        print(response.text)


    def test_create_user_min_len_name(self):
        data = {
            'password': '123',
            'username': 'q',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': 'name@login.ru'
            }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)