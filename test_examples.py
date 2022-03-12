import requests


class TestExample:
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(dict(response.cookies))

        cookies_value = response.cookies.values()
        assert cookies_value == ['hw_value'] , f"Неверный куки"