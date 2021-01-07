#Functions
studentRollno=100
studentName="Aws"


def acceptdetails():
    studentRollno=int(input("Enter your Roll Number"))
    studentName=input("Enter your name")

    print("Student Details")
    print("Roll Number: {0}, Name: {1} ".format (studentRollno,studentName))



#Display details
def displaydetails():
    print("Student Details")
    print("Roll Number: {0}, Name: {1} ".format (studentRollno,studentName))

def printme(somestring):
    print(somestring)

printme("Hope all of you have understood how to input from the user")    
greet="Hello !!!"

#calling the function
printme(greet)
displaydetails()
acceptdetails()
displaydetails()
