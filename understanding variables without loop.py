#variables

print("Hi All")
studentRollno=100
studentName="Asma"
studentAge=1

#can get input 

studentRollno=int(input("Enter your Roll Number"))
studentName=input("Enter your name")
studentAge=int(input("Enter your Age"))
subject=input("Enter the subject")
marks=int(input("Enter your marks"))

#display details

print("Student Details")
print("Roll Number: {0}, Name: {1}, Age: {2}, subject: {3}, Marks: {4} ".format (studentRollno,studentName,studentAge,subject,marks))

#or

print("Roll Number : "+str(studentRollno) + ", Name: "+studentName + ", Age: "+str(studentAge))

print("Program completed")
