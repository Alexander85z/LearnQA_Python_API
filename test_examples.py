import requests


class TestExample:
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(dict(response.cookies))
        cookies_key = response.cookies.keys()
        cookies_value = response.cookies.values()
        assert cookies_key == cookies_key
        assert cookies_value == cookies_value