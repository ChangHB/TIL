#3 6 9 게임의 왕이 되자
n = int(input())
for i in range(1, n+1) :
  if i%10==3 or i%10==6 or i%10==9:
    print("X", end=' ')   #출력 후 공백문자(빈칸, ' ')로 끝냄
  # elif i%10==6 :
  #   print("X", end=' ')
  # elif i%10==9 :
  #   print("X", end=' ')
  else:
    print(i, end=' ')

#빛 섞어 색 만들기
r, g, b = list(map(int, input().split()))
cnt = 0
for i in range(r):
  for j in range(g):
    for k in range(b):
      print(i, j, k)
      cnt += 1
print(cnt)

