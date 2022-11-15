from requests import api

link = 'https://playground.learnqa.ru/ajax/api/compare_query_type'
methods = ('GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD', 'PATCH')

# requests without data/param
for i in methods:
    response = api.request(i, link)
    print(f'Method: {i}, without data in requests, response: {response.text}')


# requests + valid data/param
for i in methods:
    for k in methods:
        if i == 'GET':
            response = api.request(i, link, params={'method': i})
            print(f'Method: {i}, with param/data, response: {response.text}')
        else:
            response = api.request(i, link, data={'method': i})
            print(f'Method: {i}, with param/data, response: {response.text}')


# mix requests
for i in methods:
    for k in methods:
        if i == 'GET':
            response = api.request(i, link, params={'method': k})
            print(f'Method: {i}, with param/data {k}, response: {response.text}')
        else:
            response = api.request(i, link, data={'method': k})
            print(f'Method: {i}, with param/data {k}, response: {response.text}')
