import random
menu = ['롯데리아','김밥천국','홍콩반점']

choice = random.choice(menu)
print(choice)

#로또 번호
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
lotto = random.sample(numbers,6)
print(lotto)