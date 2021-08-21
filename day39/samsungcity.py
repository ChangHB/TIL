#6485_삼성시의 버스노선
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

#2. 정류장을 미리 계산
T = int(input())
for tc in range(1, T + 1):
    N = int(input())       # 버스 노선 수

    start = [0] * 5001     # 출발 정류장 표시
    end = [0] * 5001       # 도착 정류장 표시
    bus_stop = [0] * 5001  # 계산한 버스 표시

    for i in range(N): #출발지점과 도착지점을 각각의 리스트에 체크
        A, B = map(int, input().split())
        start[A] += 1
        end[B] += 1

    # 버스 계산 끝!!!
    for i in range(len(bus_stop) - 1): #모든 정류장의 버스를 계산
        bus_stop[i + 1] = bus_stop[i] - end[i] + start[i + 1] 
        #현재 정류장 버스 수에서 도착 정류장 만큼 빼고
        #다음 정류장 시작 정류장 만큼 더하고

    P = int(input())
    print("#{}".format(tc), end=" ")
    for i in range(P):
        C = int(input())  # 우리가 확인하고 싶은 정류장 번호.
        print(bus_stop[C], end=" ")
    print()