import requests
TOKEN = '1887308085:AAE70NF-XJxxc3gnGyknL4DE7RMwX31aRm8'
URL = f'https://api.telegram.org/bot{TOKEN}'

#응답 내용 저장하기
update_url = f'{URL}/getUpdates'
response = requests.get(update_url).json()

#chat_id 뽑아내기
chat_id = response.get('result')[0].get('message').get('chat').get('id')

#메시지를 보내보자
#필수조건
#1. chat_id
#3. text

last_message = response.get('result')[-1].get('message').get('text')


key = '9HtWFgH89WAMnYVb9%2FgsDcVLwmcUfwUkUnvTIO5t8FNZTHGTCH33nykeFVGQKyRUUKA7lUw5CBVB7QP4SDA6Vg%3D%3D'
local = '부산'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&sidoName={local}&returnType=json'

response_dust = requests.get(url).json()

dust = response_dust.get('response')['body']['items'][1]['pm10Value']

if last_message == '미세먼지':
    text2 = f"부산태종대의 미세먼지 농도는 {dust}입니다."
elif last_message == '안녕':
    text2 = "안녕하세요 저는 심심이 입니다"
else:
    text2 = "ㄴㄴ"
    

message_url = f'{URL}/sendMessage?chat_id={chat_id}&text={text2}'


requests.get(message_url)