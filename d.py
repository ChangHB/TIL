import requests
from bs4 import BeautifulSoup


url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text

data = BeautifulSoup(response, 'html.parser')



dollar = data.select_one('span.value')
result = dollar.text
print(result)



change = data.select_one('.change')
sale = change.text
print(sale)

print(f'현재 달러 환율은 {result}원 -{sale} 입니다.')
#exchangeList > li.on > a.head.usd > div > span.value
#content > div.article2 > div.section1 > div.group1 > table > tbody > tr.down.bold > td:nth-child(2)