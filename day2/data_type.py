# 산술연산자 + - / // * ** %

# 비교연산자 == != > < >= <= 


#----------------------------------


# 논리연산자 and or

# 비트연산자 & | ^ ~ << >>

import requests

response = requests.get("https://www.naver.com")
print(response)
response2 = requests.get("https://www.naver.com").text
print(response2)