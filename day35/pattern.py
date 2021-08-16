#고지식한 패턴 검색 알고리즘

def gozisik():

    N, M = int(input().split())
    while j< M and i < N:
        if t[i] != p[j]: #다를 때
            i = i-j+1
            j = 0
        i = i + 1
        j = j + 1
    if j==M:
        return i - M
    else:
        return -1
