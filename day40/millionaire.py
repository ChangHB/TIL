#1859_백만장자프로젝트
import sys

sys.stdin = open("input_1859.txt", "r")
#1. 오른쪽으로 이동하면서 나머지 모두와 비교하며 가장 큰값에서 빼서 이익을 저장
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split())) #가격들을 입력을 받았다.

    ans = 0

    for i in range(N-1): #마직막 날은 사든 안사든 상관없음.
        max_cost = cost[i]
        for j in range(i+1, N):
            if max_cost < cost[j]:
                max_cost = cost[j]

        if max_cost > cost[i]:
            ans += max_cost - cost[i] #이익을 구하여 더한다.

    print('#{} {}'.format(tc, ans))

#2. 반대로 생각(뒤에서부터 가장 큰값을 찾고 이익을 계산)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))

    ans = 0

    max_cost = cost[-1]

    for i in range(N -2, -1, -1):
        #내가 가진 값보다 보고 있는 값이 작을때
        if max_cost > cost[i]:
            ans += max_cost - cost[i]
        else:
            max_cost = cost[i]
    print('#{} {}'.format(tc, ans))

#3.사는게 이득인지 아닌지 체크
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))

    ans = 0

    is_sell = [False] * N #기본값으로 False를 두어 안산다고 표시

    # 확인하는 과정을 반복문으로 구현
    for i in range(N - 1):
        for j in range(i + 1, N):
            if cost[i] < cost[j]:
                is_sell[i] = True
                break  # 더 큰값이 있다면 반목분을 끝내기 때문에 비교적 빠름
    buy_cost = 0
    buy_cnt = 0

    for i in range(N):
        if is_sell[i]: #True 이면 사는게 이득이었기에 비용과 갯수를 저장
            buy_cost += cost[i]
            buy_cnt += 1
        else:
            ans += (cost[i] * buy_cnt) - buy_cost
            buy_cost = 0
            buy_cnt = 0

    print("#{} {}".format(tc, ans))


