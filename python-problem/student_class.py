import functions_enrolled
class Student:
    name =None
    age =None
    is_enrolled = None
    gpa = None
    gender = None
    def __init__(self):
        self.name = functions_enrolled.forNames()
        self.age = functions_enrolled.forAgeStudent()
        self.is_enrolled=functions_enrolled.isEnrolling()
        self.gender = functions_enrolled.GenderSelection()
        self.gpa = functions_enrolled.forGpaStudent()
    def printTheValue(self):
        print('')
        print('')
        print('The student name is '+ self.name)
        if(self.age>=18):
            print(self.name + ' is ',self.age ,'years old')
        if(self.is_enrolled=='yes'):
            print(self.is_enrolled, ' ', self.gender , 'is enrolled')
        else:
            print(self.is_enrolled, '', self.gender , 'is not enrolled')
        print(self.gender+' has acheived ', self.gpa , ' in the last semester')

stu = Student()

stu.printTheValue()