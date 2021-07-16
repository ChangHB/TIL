import requests
name = 'Bob'
url = f'https://api.nationalize.io?name={name}'
response = requests.get(url).json()


name = response['name']
country_id = response['country'][0]['country_id']
probability = response['country'][0]['probability']*100

print(f'{name}의 국적은 {probability}%로 {country_id}이다.')