import requests
#
# response = requests.get('https://api.github.com')
# print(response.status_code)
# print(response.content)


url = 'https://api.github.com/search/repositories'
# Эквивалентно URL с параметрами
# url = 'https://api.github.com/search/repositories?q=python&sort=stars'
params = {'q': 'python', 'sort': 'stars'}
response = requests.get(url, params=params)
print('response.content ------------------------------- '.upper())
print(response.content)
print('response.text ----------------------------------'.upper())
print(response.text)
print('response.json() -------------------------------'.upper())
print(response.json())
