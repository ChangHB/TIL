#고지식한 패턴 검색 알고리즘

def gozisik(word):
    t = "This my home"
    p = word
    N = len(t)
    M = len(p)
    i, j = 0, 0
    while j< M and i < N:
        if t[i] != p[j]: #다를 때
            i = i-j+1    #비교지점으로 다시 돌아오기(+1은 오른쪽을 한칸씩 이동)
            j = 0        #패턴은 다시 첨부터 비교하기위해 인덱스 0으로 초기화
        i = i + 1 #같을 때 계속 비교
        j = j + 1 #같을 때 계속 비교
    if j==M:      #패턴 마지막 글자까지 같으면
        return i - M #패턴과 같은 부분의 시작 인덱스
    else:
        return -1

print(gozisik('hi'))