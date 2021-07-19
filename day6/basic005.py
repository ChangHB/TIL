#실수 1개 입력받아 소숫점이하 자리 변환하기
a = float(input())
print(format(a, ".2f") )

#실수 2개 입력받아 나눈 결과 계산하기
a, b = input().split()
print(format(float(a)/float(b), ".3f") )

#정수 2개 입력받아 자동 계산하기
a, b = input().split()
print(int(a)+int(b))  #합
print(int(a)-int(b))  #차
print(int(a)*int(b))  #곱
print(int(a)//int(b)) #몫
print(int(a)%int(b))  #나머지
print(format(int(a)/int(b),".2f"))  #소수점 이하 둘째 자리까지

#정수 3개 입력받아 합과 평균 출력하기
a, b, c = input().split()
print(int(a)+int(b)+int(c))
print((int(a)+int(b)+int(c))/3)

#정수 1개 입력받아 2배 곱해 출력하기
n = int(input())
print(n<<1)  #10을 2배 한 값인 20 이 출력된다.
print(n>>1)  #10을 반으로 나눈 값인 5 가 출력된다.
print(n<<2)  #10을 4배 한 값인 40 이 출력된다.
print(n>>2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력된다.

#6047  2의 거듭제곱 배로 곱해 출력하기
a, b = input().split()
print(int(a)*2<<int(b))
print(2<<int(b))