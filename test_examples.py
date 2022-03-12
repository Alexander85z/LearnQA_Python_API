import requests


class TestExample:
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(dict(response.headers))

        headers_value = response.headers['x-secret-homework-header']
        assert headers_value == 'Some secret value' , f"Неверный куки"