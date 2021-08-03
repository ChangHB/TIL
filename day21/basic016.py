#이상한 출석 번호 부르기2
n = int(input())
a = input().split()

for i in range(n): #인덱스로 접근하여 정수로 변환 후 다시 넣음
    a[i] = int(a[i])

for i in range(n-1, -1, -1): #거꾸로 출력
    print(a[i], end=' ')

#이상한 출석 번호 부르기3
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

print(min(a)) #가장 빠른 번호를 출력

#바둑판에 흰 돌 놓기
d=[]                   #대괄호 [ ] 를 이용해 아무것도 없는 빈 리스트 만들기
for i in range(20) :
  d.append([])         #리스트 안에 다른 리스트 추가해 넣기(20줄 만들기)
  for j in range(20) : 
    d[i].append(0)    #리스트 안에 들어있는 리스트 안에 0 추가해 넣기

n = int(input())         #바둑판에 놓는 횟수
for i in range(n) :      #n만큼 반복
  x, y = input().split()   
  d[int(x)][int(y)] = 1  

for i in range(1, 20) :
  for j in range(1, 20) : 
    print(d[i][j], end=' ')    #공백을 두고 한 줄로 출력
  print()                          #줄 바꿈


  # [0 for j in range(20)]  #20개의 0이 들어간 [0, 0, 0, ... , 0, 0, 0] 리스트
  
  # List Comprehensions
  # d = [[0 for j in range(20)] for i in range(20)] 20 x 20 리스트