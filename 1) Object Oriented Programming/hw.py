

class Animal:
    def __init__(self,name,num_legs):
        self.name=name
        self.num_legs=num_legs
    def display(self):
        print('Name:',self.name)
        

animals=[]
for i in range(0,5,1):
    print("Enter your animal's name")
    n=input()
    print('Enter the number of legs this animals has')
    l=int(input())
    a=Animal(n,l)
    animals.append(a)

for i in animals:
    i.display()
    
