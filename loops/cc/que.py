# x = 50
# def func(x):

#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)
# func(x)
# print('x is now', x)

"""
output question no 2
x is 50
Changed local x to 2
x is now 50
# """
# for i in range(10):
#     cnt = 0
#     while cnt < 10:
#         print(cnt)
    
#         cnt += 1

# cnt1 = 0
# while cnt1 < 5:
#     cnt2 = 0
#     while cnt2 < 5:
#         if cnt2 == 3:
#             break
#         if cnt2 ==0 or cnt2 ==1:
#             cnt2 += 1
#             continue
#         print(cnt2)
#         cnt2 += 1
#     cnt1 += 1

"""
question = given n print the sum of cube of all the no from 1 to n ?

"""

print("enter the number")

n = int(input())
for i in range (1,n+1):
    cube = i**3

print(cube)