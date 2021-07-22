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

#6059

# a = [1,2,'6',[]]

# def my_all(elements):
#     if elements ==[] :
#         return True 
#     else:
#         for n in elements:
#             if type(n) == list:
#                 result = False
#                 break                
#             else:
#                 result = True
#         return result

# def get_strong_word(*words):
#     if len(words)==2:
#         for i in words:
#             for j in words[i]:
#                 hap += ord(words[i][j])
#                 print(hap)


#         # if ord(words[0]) > ord(words[1]):
#         #     return words[0]
#         # return words[1]

# print(get_strong_word('tom','john'))

# def get_strong_word(*words):
#     hap1 = 0
#     hap2 = 0
#     for i in words:
#     	for j in i:
#         	hap1 += ord(j)
#             hap2 = hap1
#         if hap1 > hap2:
#             return words[0]
       
        	    
print(get_strong_word('tom','john'))
