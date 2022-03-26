import pytest
import requests
from lib.base_case import BaseCase
from lib.Assertions import Assertions
from datetime import datetime

@allure.epic("Регистрация")
class TestUserRegister(BaseCase):

    @allure.feature("Позитивный")
    @allure.story("Удачная регистрация")
    def test_create_user_successfully(self):
        data=self.prepare_registration_data()

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.feature("Негативный")
    @allure.story("Не удачная регистрация")
    def test_create_user_with_existing_email(self):
        email= 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)


        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    @allure.feature("Негативный")
    @allure.story("Не корректный email")
    def test_create_user_without_dog(self):
        email = 'namelogin.ru'
        data = self.prepare_registration_data(email)

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
    @allure.feature("Негативный")
    @allure.story("Не корректные параметры регистрации")
    def test_create_user_without_params(self, data):
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)


        print(response.text)

    @allure.feature("Негативный")
    @allure.story("Короткое имя пользователя")
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