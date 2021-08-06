#성실한 개미
num = 4
# d=[]
# for i in range(num) :
#     a,b,c,e,f,g,h,i,j,k =input().split()
#     d.append([a,b,c,e,f,g,h,i,j,k])

big_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 2, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

x = 1
y = 1
n = 1
big_data[x][y] = 9

while True:    
    if big_data[x][y] ==2 or big_data[x][y] ==2:
        break
    elif big_data[x][y+n]==1 :
        x = x+n
        big_data[x][y] = 9
        print(big_data[x][y])
    else:
        y= y+n
        big_data[x][y] = 9
        print(big_data[x][y])

for i in range(1, 10) :
  for j in range(1, 10) : 
    print(big_data[i][j], end=' ')    #공백을 두고 한 줄로 출력
  print() 


