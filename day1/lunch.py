import random
menu = ['롯데리아','김밥천국','홍콩반점']

choice = random.choice(menu)
print(choice)

#로또 번호
numbers = range(1,45)
lotto = random.sample(numbers,6)
print(lotto)