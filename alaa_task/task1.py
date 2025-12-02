class Student ():
    def __init__(self,name,age):
        self.__name= name
        self.__age = age
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name 
        
    def get_age (self):
        return self.__age
    def set_age (self,age):
        self.__age=age

st1=Student("alaa",20 )
std_name=st1.get_name
print(std_name())
st1.set_name ("alaa hany")
print(std_name())

age1=st1.get_age
std_age=st1.get_age
print(std_age())
st1.set_age (50)
print(std_age())