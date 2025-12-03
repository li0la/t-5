class Car(): 
    def __init__(self,speed):
        self.speed=speed
    def get_speed(self):
        return self.speed
    def set_speed(self,speed):
        self.speed=speed
car1 =Car(120)
print(car1.get_speed())
car1.set_speed('80')
print(car1.get_speed())