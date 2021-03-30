print("please enter the no of rows", end="")
n = int(input())
for row in range (1,n+1):
    for no_of_stars in range(row):
        print("*",end=" ")
    
    print()
