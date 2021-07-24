#논리 연산자 연습
def T():
    print("트루")
    return True

def F():
    print("펄쓰")
    return False

if F() or F():
    print("이거나옴?")

arr = [1, 2, 3]
if F() and arr[5]:
    print("이거에러나냐?")