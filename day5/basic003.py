#정수 2개 입력받아 합 계산하기
a, b = input().split()
c = int(a) + int(b)
print(c)

#실수 2개 입력받아 합 계산하기
a = input()
b = input()
c = float(a) + float(b)
print(c)

#10진 정수 입력받아 16진수로 출력하기
a = input()
n = int(a)      #입력된 a를 10진수 값으로 변환해 변수 n에 저장
print('%x'% n)  #n에 저장되어있는 값을 16진수(hexadecimal) 소문자 형태 문자열로 출력

#16진수를 입력받아 8진수(octal)로 출력해보자.
a = input()
n = int(a, 16)   #입력된 a를 16진수로 인식해 변수 n에 저장
print('%o' % n)  #n에 저장되어있는 값을 8진수(octal) 형태 문자열로 출력

#영문자 1개 입력받아 10진수로 변환하기
n = ord(input()) #입력받은 문자를 10진수 유니코드 값으로 변환한 후, n에 저장한다. A:65, B:66, C:67 ....
print(n)         #ord(c) : 문자 c 를 10진수로 변환한 값 

#정수 입력받아 유니코드 문자로 변환하기
c = int(input())
print(chr(c))  #c에 저장되어 있는 정수 값을 유니코드 문자(chracter)로 바꿔 출력한다.

