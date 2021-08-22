#4836_색칠하기
t = int(input())
 
for tc in range(t):
    arr = [[0] * 10 for _ in range(10)] #0으로 이루어진 2차원 배열 만들기
    n = int(input())
    ans = 0
    for _ in range(n):  #영역을 N번 반복해서 받아 2차원 배열에 숫자로 표시 / 마지막 한번은 else가 실행된다.
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r2 - r1 + 1): #range 범위는 1 작은 값까지만 하기 때문에 +1 해준다
            for c in range(c2 - c1 + 1):
                if arr[r1 + r][c1 + c] == 0:
                    arr[r1 + r][c1 + c] = color #색에 맞게 숫자 표시
                else:                           #0이 아닌곳을 모두 카운트
                    ans += 1
    print('#{} {}'.format(tc + 1, ans))


#조금 더 구체적인 풀이
T = int(input())

for i in range(1, T+1):
    arr = [[0] * 10 for _ in range(10)]

    N = int(input())
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for m in range(r1, r2 + 1):     #주어진 영역을 색에 따라 더하기 ex)1 또는 2
            for n in range(c1, c2 +1):
                arr[m][n] += color

    cnt = 0                #겹치는 부분을 카운트
    for j in range(10):
        for k in range(10):
            if arr[i][j] == 3:
                cnt += 1

    print('#{} {}'.format(i, cnt))