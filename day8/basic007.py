# 6052 정수 입력받아 참 거짓 평가하기
n = int(input())
print(bool(n))

#참 거짓 바꾸기
a = bool(int(input()))
print(not a)

#둘 다 참일 경우만 참 출력하기
a, b = input().split()
print(bool(int(a)) and bool(int(b)))

#하나라도 참이면 참 출력하기
a, b = input().split()
print(bool(int(a)) or bool(int(b)))

#참/거짓이 서로 다를 때에만 참 출력하기
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))

#참/거짓이 서로 같을 때에만 참 출력하기
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and d) or ((not c) and (not d)))

#둘 다 거짓일 경우만 참 출력하기
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((not c) and (not d))