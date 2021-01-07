#1. write a program which takes 3 numbers from user. and prints the total and product of the numbers.
#repeat 3 times

print ("Please enter 3 numbers")

def addNumbers(num1,num2,num3):
    return num1 + num2 + num3

for x in range (0,4):
    num1=int(input("Enter first number"))
    num2=int(input("Enter second number"))
    num3=int(input("Enter third number"))
    Total = addNumbers (num1, num2, num2)
    print (Total)
addNumbers (num1,num2,num3)
