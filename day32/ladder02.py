for i in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for j in range(100)]
    r = 0
    ans = 0
    for c in range(100):
        if arr[0][c] == 1:
            while r < 99:
                r += 1
                if c < 99 and arr[r][c+1] == 1:
                    while arr[r][c+1] != 0:
                        c += 1
                elif c > 0 and arr[r][c-1] == 1:
                    while arr[r][c-1] != 0:
                        c -= 1
            if arr[99][c] == 2:
                ans = c
                    
    print('#{} {}'.format(i, ans))