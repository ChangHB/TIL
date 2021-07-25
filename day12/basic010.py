#정수 2개 입력받아 큰 값 출력하기
a, b = input().split()
a = int(a)  #변수 a에 저장되어있는 값을 정수로 바꾸어 다시 변수 a에 저장
b = int(b)
c = (a if (a>=b) else b)
print(int(c))

#정수 3개 입력받아 가장 작은 값 출력하기
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = (a if a<b else b) if ((a if a<b else b)<c) else c
print(int(d))

#정수 3개 입력받아 짝수만 출력하기
a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a%2==0 :  #논리적으로 한 단위로 처리해야하는 경우 콜론(:)을 찍고, 들여쓰기로 작성 한다.
  print(a)

if b%2==0 :
  print(b) 

if c%2==0 :
  print(c) 

#정수 3개 입력받아 짝/홀 출력하기
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a%2==0 :
  print("even")
else :
  print("odd")

if b%2==0 :
  print("even")
else :
  print("odd")

if c%2==0 :
  print("even")
else :
  print("odd")

#정수 1개 입력받아 분류하기
n= int(input())
if n<0 :
  if n%2==0 :
    print('A')      #주의 : 변수 A와 문자열 'A' / "A" 는 의미가 완전히 다르다. 
  else :
    print('B')
else :
  if n%2==0 :
    print('C')
  else :
    print('D')

#점수 입력받아 평가 출력하기
n= int(input())
if n>=90 :
  print('A')
else :
  if n>=70 :
    print('B')
  else :
    if n>=40 :
      print('C')
    else :
      print('D') 

#평가 입력받아 다르게 출력하기
n= str(input())
if n=='A' :
  print('best!!!')
else :
  if n=='B' :
    print('good!!')
  else :
    if n=='C' :
      print('run!')
    else :
      print('slowly~')

#월 입력받아 계절 출력하기
n= int(input())
if n//3==1 :
  print("spring")
else : 
    if n//3==2 :
        print("summer")
    else : 
        if n//3==3 :
            print("fall")
        else :
            print("winter")

#6071
#0 입력될 때까지 무한 출력하기
n = 1      #처음 조건 검사를 통과하기 위해 0 아닌 값을 임의로 저장
while n!=0 :
  n = int(input())
  if n!=0 :
    print(n)


