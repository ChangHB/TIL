#3의 배수는 통과
n= int(input())
for i in range(1, n+1):
    if i % 3 ==0:
        continue
    print(i, end=' ')

#수 나열하기1
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print(a + b*(c-1))

#수 나열하기2
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print(a * b**(c-1))

#수 나열하기3
a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
ans = 0
for n in range(d-1): #반복문으로 푸는게 맞는것인가...?
    ans += c*b**n
ans += a*b**(d-1)
print(ans)

