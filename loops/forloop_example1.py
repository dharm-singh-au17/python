
for j in range (1,10):

    i = int(input("enter input"))

    if (i % 5 ==0 and i % 3 ==0):
        print("FIZZ_FUZZ")
        
    elif (i % 3 == 0):
        print("FIZZ")
    elif (i % 5 == 0):
        print("FUZZ")
    else:
        print(i)