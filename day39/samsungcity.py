import sys

sys.stdin = open("input_6485.txt", "r")

#1. 모든 노선 체크
def bus_count(bus_stop):
    cnt = 0

    for i in range(N):
        if bus_route[i][0] <= bus_stop <= bus_route[i][1]:
            cnt += 1

    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())     #버스 노선 수

    bus_route = []       #버스 노선들을 저장해 놓을 리스트

    for i in range(N):
        A, B = map(int, input().split())
        bus_route.append((A, B))        #튜플 형태로 저장

    P = int(input())
    ans = [] #버스 수를 저장해 놓을 리스트

    for i in range(P):
        C = int(input())            # 1 2 3 4 5 입력 받는 순서대로 
        ans.append(bus_count(C))    # 함수를 써서 리스트에 저장

    print('#{}'.format(tc), end=" ")
    print(' '.join(map(str, ans))) #join 메서드를 쓰기 위해서 str 형태로 변환한다.