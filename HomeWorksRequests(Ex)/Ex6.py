import requests

response = requests.get('https://playground.learnqa.ru/api/long_redirect')
if response.history:
    for resp in response.history:
        print(resp)
    print(f'final url: {response.url}')
else:
    print(f'Request was not redirected')
