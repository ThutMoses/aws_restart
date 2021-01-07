#1. create a function which takes 2 arguments (name and age) and display the same

def sayhello ():
    print ("hello")

sayhello()

def sayhi (name):
    print ("Hi " + name)

sayhi ("Faith")

def greetall ():
    return "Hello All !!!!"


result=greetall ()
print (result)

myList=[]

def greetlist():
    myList=["Hi", "Hello", 100,50,25, "bye"]
    return myList

#print(greetlist ())

for item in greetlist ():
    print (item)

def printgenius (name):
    return name + " is a genius"

print(printgenius ("Moses"))

studentName=input("Enter your name")
data=printgenius (studentName)
print(data)

