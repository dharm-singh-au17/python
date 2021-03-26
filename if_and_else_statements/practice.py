"""
If a no is divisible by 3 print FIZZ
If a no is divisible by 5 print FUZZ
and if a no is divisible by both 3 and 5 print FIZZ_BUZZ

"""

user_input = int(input())

if (user_input % 5 == 0 and user_input % 3 ==0):
    print("FIZZ_BUZZ")
else:
    if(user_input % 5 ==0):
        print("FUZZ")
    if(user_input % 3 ==0):
        print("FIZZ")    