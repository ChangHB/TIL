##기초-입출력##
#입력한 값 출력
a = input() 
b = input()
print(a)
print(b)
#정수로 변환
n = input()
n = int(n)
print(n)
#공백으로 나눠서 출력하기
a, b = input().split()
print(a)
print(b)
#시간 : 로 표현하기
a, b = input().split(':')
print(a, b, sep=':')
#연도.월.일 일-월-연도로 표현하기
y, m, d = input().split('.')
print(d, m, y, sep='-')
#주민번호 - 없애기
a, b = input().split('-')
print(a, b, sep='')
#한글자씩 출력
s = input()
print(s[0])
print(s[1])
#연월일 나눠서 출력
s = input()
print(s[0:2], s[2:4], s[4:6])
#시:분:초 입력 시 분만 출력
a, b, c = input().split(':')
print(b)
#단어 2개 공백 붙이기
w1, w2 = input().split()
s = w1 + w2
print(s)