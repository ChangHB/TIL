#6059 
# 비트단위로 NOT 하여 출력하기
#컴퓨터에 저장되는 모든 데이터들은 2진수 형태로 바뀌어 저장된다. 0과 1 
#4bit 기준 0010 1101
a = 5
print(~a)

#비트단위로 AND 하여 출력하기
# 둘다 1이면 1, 하나라도 0 이면 0
a, b = input().split()
print(int(a) & int(b))

#비트단위로 OR 하여 출력하기
# 둘다 0이면 0, 하나라도 1 이면 1
a, b = input().split()
print(int(a) | int(b))

#비트단위로 XOR 하여 출력하기
#다른부분 1 같으면 0
a, b = input().split()
print(int(a) ^ int(b))