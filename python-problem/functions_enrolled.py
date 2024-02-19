def GenderSelection():
        while True:
            gender = str(input("His/Her gender?-> he/she : "))
            if(gender =='he' or gender == 'she'):
                return gender
def forNames():
        nameOfStudent = str(input("enter the student name : "))
        return nameOfStudent
def forGpaStudent():
     gpa = float(input("please enter the Gpa, a float: "))
     return gpa
def forAgeStudent():
        age = int(input("please enter the age, a digit: "))
        return age
def isEnrolling():
        while True:
            isEnrolled = str(input("is he/she enrolled: yes/no : "))
            if(isEnrolled =='yes' or isEnrolled == 'no'):
                return isEnrolled