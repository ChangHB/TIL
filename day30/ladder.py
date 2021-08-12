#사다리 문제(4시간 고민햇으나 출력값이 이상함, 로직 어떤 부분이 잘못된건지 감도 안잡힘...)
for i in range(10):
    N= int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]  #입력값을 2차원 배열로 만든다.
    start_idx = []                                               #처음 사다리가 시작 지점 리스트
    for j in range(100):
        if arr[0][j] == 1:                                       # 1인 경우 사다리 시작 지점
            start_idx.append(j)

    dr = [0, 0, 1]  #좌 우 아래
    dc = [-1, 1, 0]


    ans =0
    for k in start_idx:
        r = 1
        c = k
        while True:
            if r == 99:                              # 맨 밑에 도착했을 떄 
                break

            if 0 < c < 100 and arr[r][c - 1] == 1:   # 왼쪽이 1일 때 
                d = 0
                while True:
                    r += dr[0]
                    c += dc[0]
                    if c ==0 or arr[r][c - 1] == 0:  # 계속가다가 0이면 탈출
                        break

            elif 0 <= c < 99 and arr[r][c + 1] == 1: # 오른쪽이 1일 때 
                d = 1
                while True:
                    r += dr[1]
                    c += dc[1]
                    if c ==99 or arr[r][c + 1] == 0: # 계속가다가 0이면 탈출
                        break
            d = 2
            r += 1
            c += 0

            if arr[r][c] == 2: # 2를 만났을 때
                ans = c
                break
        if ans != 0:
            break
    print(ans)


