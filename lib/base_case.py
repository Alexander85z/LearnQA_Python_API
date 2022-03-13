import json.decoder

from requests import Response

class BaseCase:
    def get_cookie (self, response: Response, cooke_name):
        assert cooke_name in response.cookies, f"Cannot find cookie with name {cooke_name} in the last response"
        return response.cookies[cooke_name]
    def get_header (self, response: Response, headers_name):
        assert headers_name in response.headers, f"Cannot find heaser with name {headers_name} in the last response"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"
        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

        return response_as_dict[name]