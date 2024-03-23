
class Car:
    def __init__(self,color,model,speed):
        self.color=color
        self.model=model
        self.speed=speed
    def increase(self):
        self.speed=self.speed+5
    def decrease(self):
        self.speed=self.speed-5
        

car1=Car('black','tesla_y',60)
car2=Car('red','nissan',30)

car1.decrease()
print(car1.speed)
for i in range(1,11,1):
    car2.increase()
    print(car2.speed)
