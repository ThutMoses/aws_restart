# Accept 2 numbers and display the smallest of the two

num1=int(input('enter the first number: '))
num2=int(input('Enter second number: '))

def smallest_num (num1, num2):
    if (num1 < num2):
        smallest_num = num1
    elif (num2 < num1):
        smallest_num = num2
    print("The smallest of the two numbers is: ",smallest_num)
smallest_num(num1, num2)
    
