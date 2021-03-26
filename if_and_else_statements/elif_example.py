"""
if
else
"""

user_input = int(input())

if(user_input % 5 == 0 and user_input % 3 == 0):
    print("FIZZ_BUZZ")
elif(user_input % 3 ==0):
    print("FIZZ")
elif(user_input % 5 ==0):
    print("FUZZ")
else:
    print("wrong input")        
