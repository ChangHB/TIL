#정수 1개 입력받아 카운트다운 출력하기
n = int(input())
while n!=0 :
  print(n)
  n = n-1

#짝수 합 구하기
n = int(input())
s = 0
for i in range(1, n+1) :
  if i%2==0 :
    s += i
print(s)

#원하는 문자가 입력될 때까지 반복 출력하기
n = input()
while n != 'q' :
    n = input()

#언제까지 더해야 할까?
t = int(input())
s = 0
n = 0
while s<t :
  n +=1
  s +=n
print(n,s)

#주사위 2개 던지기
n = 6
m = 6
for i in range(1, n+1):
    for j in range(1, m+1) :
        print((j, i,), end=' ')
    print() 

#16진수 구구단 출력하기 A, B, C, D, E, F 중 하나가 입력될 때,
#1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
n=input()
for i in range(1,16):
    s=int(n,16) #주어진 값을 16진수로 인식한 후 10진수 정수형태로 변환
    print('%x' %s,  '*%x' %i,  '=%x' %(s*i), sep='')
    # n에 저장되어있는 값을 16진수(hexadecimal) 형태로 출력
    