import requests


def test_request():
    link = 'https://playground.learnqa.ru/api/homework_header'
    response = requests.get(link)
    headers_from_response = response.headers
    print(f'Cookie: {headers_from_response}')
    assert headers_from_response, f'Empty header'
