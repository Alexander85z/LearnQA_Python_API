import pytest
import requests


class TestExample:
    user_agent = [({"User-Agent":
                        'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}),
                  ({
                      'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'})
                  ]
    response_body = [({'platform': 'Mobile', 'browser': 'No', 'device': 'Android'}),
                     ({'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'})
                     ]


    @pytest.mark.parametrize('headers2', user_agent)
    @pytest.mark.parametrize('response_body1', response_body)
    def test_mobile(self, headers2, response_body1):
        headers1 = headers2
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers=headers1)
        print(response.text)
        response_body2=response_body1
        parsing1 = response.json()
        assert response_body2['platform'] == parsing1['platform'], f"Платформа определена некорректно"
        assert response_body2['browser'] == parsing1['browser'], f",Браузер определен некорректно"
        assert response_body2['device'] == parsing1['device'], f"Девайс определен некорректно"

        print(parsing1['platform'])
        print(response_body2['platform'])
