class Student:
    #this def is right into the class.
    def __init__(self,name,age):
        #this self is inside the first def.
        self.__name=name
        self.__age = age
    #and this def too is inside the class.
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age

    def set_name(self,name):
        self.__name=name
    def set_age(self,age):
        self.__age=age

std1 =Student('basmalla',20)    #object
std2 = Student("ahmed", 23)     #object
print(std1.get_name())
print(std2.get_name())
std1.set_name("basmalla ahmed")
std2.set_name("ahmed ellaban")
print(std1.get_name())
print(std2.get_name())
print(std1.get_age())
print(std2.get_age())
std1.set_age("21")
std2.set_age("22")
print(std1.get_age())
print(std2.get_age())
