import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")


print(len(response.history))
for name_url in response.history: print( name_url.status_code, name_url.url)






