import requests
import time
from random import randint


link = 'https://playground.learnqa.ru/ajax/api/longtime_job'
parameters = {'token': ''}

# first request
response_one = requests.get(link)
parser_response_text = response_one.json()
parameters['token'] = parser_response_text['token']

# timeouts and second request
timeout_for_task = parser_response_text['seconds']
moment_for_check_status = randint(0, timeout_for_task)
print(f'Time to ready: {timeout_for_task}, time to check: {moment_for_check_status}')
time.sleep(moment_for_check_status)
response_two = requests.get(link, params=parameters)
print(f'Check status: {response_two.json()}')
time.sleep(timeout_for_task - moment_for_check_status +1)

# third request
response_three = requests.get(link, params=parameters)
if response_three.json()['status'] == 'Job is ready':
    print(f'End timeout, status: {response_three.json()}')
else:
    print(f"Error, status: {response_three.json()['status']}")

