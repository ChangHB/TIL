#숫자 카드 문제 - 가장 많은 카드 출력하고 장수가 같을 때는 가장 큰 값
T = int(input())

for i in range(T):
    N = int(input())
    arr_n = list(map(int, input()))

    cnt = 0
    ans_num = 0
    ans = 0

    for j in range(len(arr_n)): 
        num = arr_n[j]          #숫자 카드 하나씩 선택
        for k in arr_n:         #숫자 카드 중 같은 숫자 찾기 반복
            if k ==num:
                cnt+=1
        if ans < cnt:
            ans = cnt
            ans_num = num
            if ans_num ==0:                 #ans == 0일 경우 출력값이 달라지는 이유는...???
                for l in range(len(arr_n)):     #숫자 카드 중 같은 숫자가 없으므로 가장 큰 값을 찾는다.
                    if arr_n[l] > ans_num:
                        ans_num = arr_n[l]      #01234 가능 55555도 가능할까....??
        cnt = 0
    print('#{} {} {}'.format(i+1, ans_num, ans ))

