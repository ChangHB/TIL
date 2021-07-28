#6084 소리 파일 저장용량 계산하기

# h, b, c, s = int(input()).split() 문법적 오류
h, b, c, s = list(map(int, input().split()))
result = h*b*c*s/8/1024/1024
print(round(result,1), end =' MB')

#그림 파일 저장용량 계산하기
w, h, b = list(map(int, input().split()))
result = w*h*b/8/1024/1024
print(round(result,2), end =' MB')

#거기까지! 이제 그만~
s = 0
c = 0
n = int(input())
while True :
  s += c
  c += 1
  if s>=n :
    break
print(s)