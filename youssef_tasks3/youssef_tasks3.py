class Student:
    def __init__(self, name, age):
        self.__name = name
        self.age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.__age = age
student1 = Student("usef", 20)
student_age= student1.get_age()  
student1 = Student("usef", 20)  
student_name = student1.get_name()
print(student_name)
print(student_age)
