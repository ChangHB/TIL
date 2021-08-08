#2차원 리스트 - 깊은복사 효과 낼수없다...
arr = [
    [1,2,3],
    [4,5,6]
]
a = arr[:] #슬라이스 처음 : 끝

a[0][0] = 321

print(arr)

#반복문 딥카피
b = []

for i in arr :
    tmp = []
    for j in i :
        tmp.append(j)
    b.append(tmp)
b[0][0] = 0

print(arr)
print(b)

#copy 모듈 - 내부 리스트까지 복사
import copy

a = [1, 2, [1, 2]]
b = copy.deepcopy(a)

b[2][0] = 3
print(a, b)

#반복문
c_list = []
for n in numbers:
    c_list.append(n **3)
c_list

#List Comprehension
c_list2 = [n**3 for n in numbers]

#list.remove() 결과값을 리스트 표현문으로 어떻게 쓸까...?

