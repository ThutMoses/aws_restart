#print comment student grades

def getstudent_id():
    print ("ENTER STUDENT ID:")
    identity = int(input())
    return identity

def getexam_score ():
    print ("ENTER EXAM SCORE:")
    examscore = int(input())
    return examscore

def printcomment():
    if grade == '100':
        print ("COMMENT:         keep it up")
    elif grade == '90 <= final score <= 99':
        print ("COMMENT:         Excellent")
    elif grade == '80 <= final score <= 90':
        print ("COMMENT:         very good")
    elif grade == '70 <= final score <= 80':
        print ("COMMENT:         good")
    elif grade == '60 <= final score <= 70':
        print ("COMMENT:         put more effort")
    elif grade == '50 <= final score <= 60':
        print ("COMMENT:         You have to improve")
    else: grade =='50 <= final score'
    print ("COMMENT:         you have failed")
