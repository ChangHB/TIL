#4861_회문
def isPal(text):
    for i in range(len(text)//2):
        if text[i] != text[len(text)-i-1]:
            break
    else:
        return True  #모두 다 같으면 True
    return False     #break 빠져나와서 False 값

def isrowcol(N, M, arr):
    #가로에 대한 검사
    for r in range(N):
        for c in range(N-M+1):
            tmp_text = ''
            for c_idx in range(c, c+M):
                tmp_text += arr[r][c_idx]
            if isPal(tmp_text):
                return tmp_text
    
    # 세로에 대한 검사
    for c in range(N):
        for r in range(N-M+1):
            tmp_text = ''
            for r_idx in range(r,r+M):
                tmp_text += arr[r_idx][c]
            if isPal(tmp_text):
                return tmp_text
    
    return None

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    print('#{} {}'.format(tc, isrowcol(N, M, arr)))