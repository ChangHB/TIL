#바둑알 십자 뒤집기
n = int(input())
d=[]
for i in range(20) :
  d.append([])         #리스트 안에 다른 리스트 추가해 넣기(20줄 만들기)
  for j in range(20) : 
    d[i].append(0) 

for i in range(n) :  #n번만큼 반복
  x,y=input().split()
  for j in range(1, 20) : # 뒤집기 19 *19 만들기 
    if d[j][int(y)]==0 :
      d[j][int(y)]=1
    else :
      d[j][int(y)]=0

    if d[int(x)][j]==0 :
      d[int(x)][j]=1
    else :
      d[int(x)][j]=0

for i in range(1, 20) :
  for j in range(1, 20) : 
    print(d[i][j], end=' ')    #공백을 두고 한 줄로 출력
  print() 


#설탕과자 뽑기
x,y=input().split()

#기본 판 만들기
d=[]
for i in range(int(x)) :
  d.append([])         
  for j in range(int(y)) : 
    d[i].append(0)

#입력값 반복 적용하기
n = int(input())
for i in range(n):
    a,b,e,f=input().split()
    m=0
    e= int(e)-1
    f= int(f)-1
    if int(b)==0:
        for i in range(int(a)):
            d[e][f+m]=1
            m += 1
    else:
        for i in range(int(a)):
            d[e+m][f]=1
            m += 1

for i in range(int(x)) :
  for j in range(int(y)) : 
    print(d[i][j], end=' ')    #공백을 두고 한 줄로 출력
  print()