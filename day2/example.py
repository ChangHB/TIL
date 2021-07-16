import requests
name = 'Bob'
url = f'https://api.agify.io?name={name}'

response = requests.get(url).json()

print(response, type(response))

url2 = f'https://api.nationalize.io?name={name}'
result = requests.get(url2).json()


name = result['name']
country_id = result['country'][0]['country_id']
probability = result['country'][0]['probability']

print(f'{name}의 국적은 {country_id}')