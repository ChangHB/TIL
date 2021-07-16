import requests

key = '9HtWFgH89WAMnYVb9%2FgsDcVLwmcUfwUkUnvTIO5t8FNZTHGTCH33nykeFVGQKyRUUKA7lUw5CBVB7QP4SDA6Vg%3D%3D'
local = '부산'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&sidoName={local}&returnType=json'


response = requests.get(url).json()
dust = response.get('response')['body']['items'][2]['pm10Value']
#차근차근 접근도 가능하다

#부산의 미세먼지 농도는 oooo입니다.
print(f'부산태종대의 미세먼지 농도는 {dust}입니다.')



