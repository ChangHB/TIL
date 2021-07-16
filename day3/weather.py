import requests

name='1132599'
url=f'https://www.metaweather.com/api/location/{name}'

#json을 이용해서 dict 형태로 변환(수레바퀴 두 번 만들지마라)
response = requests.get(url).json()
print(response)

#response.get('consolidated_weather')[2]['weather_state_name']
#response['consolidated_weather'][2]['weather_state_name']
the_day_after = response.get('consolidated_weather')[2]['weather_state_name']
print(f'서울의 모레 날씨는 {the_day_after}입니다.')