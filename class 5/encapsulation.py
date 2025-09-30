from traceback import print_tb


class Student:

    def __init__(self, name):
        self.name = name      #public 
        self._gpa = 3.5       #protected 
        self.__password = "1234"   #private


student1 = Student("Matthew")

student1._gpa = 4.0


print(student1.name)
print(student1._gpa)
print(student1.__password)