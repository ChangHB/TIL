#1954달팽이 문제 연습문제3

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = 5
A = [[0]*N for _ in range(N)]
cnt = 1
i, j = 0, -1
k = 0
while cnt <= N*N:
    ni, nj = i + di[k], j + dj[k]
    if 0<= ni <N and 0<=  nj <N and A[ni][nj] == 0:
        A[ni][nj] = cnt
        cnt += 1
        i, j = ni, nj
    else:
        k = (k+1)%4

for i in range(N):
    print(A[i])