import requests
import pytest


class TestUserAuth:
    exclude_param = [
        ('no_cookie'),
        ('no_token')
    ]

    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response_one = requests.post('https://playground.learnqa.ru/api/user/login', data=data)
        assert 'auth_sid' in response_one.cookies, 'There is no auth cookie'
        assert 'x-csrf-token' in response_one.headers, 'There is no CSRF token'
        assert 'user_id' in response_one.json(), 'There is no user id'
        self.auth_sid = response_one.cookies.get('auth_sid')
        self.token = response_one.headers.get('x-csrf-token')
        self.user_id_from_auth_method = response_one.json()['user_id']

    def test_auth_user(self):
        response_two = requests.get(
            'https://playground.learnqa.ru/api/user/auth',
            headers={'x-csrf-token': self.token},
            cookies={'auth_sid': self.auth_sid}
        )
        assert 'user_id' in response_two.json(), 'There is no user id'
        user_id_from_check_method = response_two.json()['user_id']
        assert self.user_id_from_auth_method == user_id_from_check_method, 'User id is not equal'

    @pytest.mark.parametrize('condition', exclude_param)
    def test_negative_auth_test(self, condition):

        if condition == 'no_cookie':
            response_two = requests.get('https://playground.learnqa.ru/api/user/auth',
                                        headers={'x-csrf-token': self.token})
        else:
            response_two = requests.get('https://playground.learnqa.ru/api/user/auth',
                                        cookies={'auth_sid': self.auth_sid})

        assert 'user_id' in response_two.json(), 'There is no user id'

        user_id_from_check_method = response_two.json()['user_id']
        assert user_id_from_check_method == 0, 'User is authorized'
