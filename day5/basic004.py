#정수 1개 입력받아 부호 바꾸기
n = int(input())
print(-n) 

#문자 1개 입력받아 다음 문자 출력하기
n = ord(input())
print(chr(n+1))

#정수 2개 입력받아 차 계산하기
a, b = input().split()
c = int(a) - int(b)
print(c)

#실수 2개 입력받아 곱 계산하기
f1, f2 = input().split()
m = float(f1) * float(f2)
print(m)

#단어 여러 번 출력하기
w, n = input().split()
print(w*int(n))

#문장 여러 번 출력하기
n = input()
s = input()
print(int(n)*s)

#정수 2개 입력받아 거듭제곱 계산하기
a, b = input().split()
c = int(a)**int(b) 
print(c)

#실수 2개 입력받아 거듭제곱 계산하기
f1, f2 = input().split()
c = float(f1)**float(f2) 
print(c)

#정수 2개 입력받아 나눈 몫 계산하기
a, b = input().split()
print(a//b)

#41 정수 2개 입력받아 나눈 나머지 계산하기
a, b = input().split()
print(a%b)