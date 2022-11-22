import requests


def test_request_cookie_method():
    link = 'https://playground.learnqa.ru/api/homework_cookie'
    response = requests.get(link)
    values_from_cookie = response.cookies.values()
    print(f'Cookie: {values_from_cookie}')
    assert values_from_cookie, f'Empty cookie'
