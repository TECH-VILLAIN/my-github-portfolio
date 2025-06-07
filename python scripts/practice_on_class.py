from operator import truediv


class Student(object):
    def __init__(self,name,age,department):
        self.name = name
        self.age = age
        self.department = department
    def introduce(self):
        print( f"hi i am {self.name},i am from {self.department}")
    def isadult(self):
       if self.age >= 18 :
        print(True)
       else:
        print(False)
student1 = Student("john",20,"computer science")
student1.introduce()
student1.isadult()