"""
Take input of age of 3 people by user and determine oldest and youngest among them.

"""

print("Enter age First person")
First = int(input())

print("Enter the age of second person")
Second = int(input())

print("Enter the age of third person")
Third = int(input())

if (First >= Second and First >= Third):
    print("First is oldest")
elif(Second >= First and Second >= Third):
    print("seond is oldest")
elif(Third >= First and Third >= Second):
    print("third is oldest")
else:
    print("all are equal")    