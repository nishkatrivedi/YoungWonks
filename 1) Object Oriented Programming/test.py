import random
class Person:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
        self.planet='Earth'
    def display(self):
        self.height=random.randint(1,100)
        print(self.name,self.height)
    def grow(self):
        self.age+=1
    def show_height(self):
        print(self.height)

person1=Person('Nishka',5,10)
##person2=Person('Bob',2,30)

person1.display()
print(person1.name,person1.height)
