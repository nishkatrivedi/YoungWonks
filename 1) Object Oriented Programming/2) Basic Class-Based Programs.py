#Question 1
'''class Shape:
    def __init__(self,sides,shape):
        self.sides=sides
        self.shape=shape
shape1=
shape2=Shape(3,'triangle')
shape3=Shape(1,'circle')
shape4=Shape(5,'pentagon')

shapes=[Shape(4,'rectangle'),shape2,shape3,shape4]

for i in range(0,4,1):
    print(shapes[i].sides)
    print(shapes[i].shape)'''

#Question 2
'''names=[]
class Dog:
    def __init__(self,name,eye_color,fur_color,breed,age):
        self.name=name
        self.eye_color=eye_color
        self.fur_color=fur_color
        self.breed=breed
        self.age=age

    def show_info(self):
        print("My dog's name is",self.name,"and he/she is a",self.age,"year old",self.breed,", with",self.eye_color,"eyes and",self.fur_color,"colored fur")
    def increase(self):
        self.age+=1
dog1=Dog('Puppy','brown','golden','golden retriever',5)

dog2=Dog('Cupcake','blue','white','pomeranian',2)'''




#Question 3
'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.petlist=[]
    def show_names(self):
       print(self.name)
       for i in self.petlist:
            i.show_info()
    def add_pet(self,dog):
        self.petlist.append(dog)

person1=Person('Nishka',13)
person2=Person('bob',10)

person1.add_pet(dog1)
person2.add_pet(dog2)

person1.show_names()
person2.show_names()'''

#Question 4
'''class Account:
    def __init__(self,name,number,balance):
        self.name=name
        self.number=number
        self.balance=balance
    def deposit(self):
        print('How much money would you like to add?')
        a=int(input())
        self.balance=self.balance+a
    def withdraw(self):
        print('How much money would you like to withdraw?')
        w=int(input())
        self.balance=self.balance-w
    def show_balance(self):
        print('Name:',self.name,'Number:',self.number,'Balance:',self.balance)

        
    
account1=Account('Bob',143,500)
print('What would you like to do with your account?')
c=input()
if c=='deposit':
    account1.deposit()
    account1.show_balance()
    
elif c=='withdraw':
    account1.withdraw()
    account1.show_balance()
elif c=='show balance':
    account1.show_balance()
else:
    print('Please try again')'''


#Question 5         
'''class State:
    def __init__(self,name,capital,population):
        self.name=name
        self.capital=capital
        self.population=population
    def show_info(self):
        print(self.name)
        print(self.capital)
        print(self.population)
    def is_state(self,name):
         return self.name==name
        
massachusetts=State('massachusetts','Boston',7000000)
florida=State('florida','Tallahassee',22000000)
california=State('california','Sacramento',5000000)
colorado=State('colorado','Denver',8000000)
maryland=State('maryland','Annapolis',14000000)

states=[massachusetts,florida,california,colorado,maryland]
print('Which state would you like to find?')
s=input()
for i in states:
    print(i.name,s)
    if i.is_state(s):
        i.show_info()'''

#Question 6

'''class Shopping:
    def __init__(self,name):
        self.shop_name=name
        self.cart={}

    def add_item(self,item,quantity):
        
        if item in self.cart:
            self.cart[item]+=quantity
        else:
            self.cart[item]=quantity
        
    def remove_item(self,item):
        if item in self.cart:
            self.cart.pop(item)

    
            

shopping_bag=Shopping('Walmart')
##shopping_bag.add_item('strawberries',5)
##shopping_bag.add_item('carrots',2)'''

#Question 8

'''class Phonebook:
    def __init__(self):
        self.contacts={}
        
    def add_entry(self,name,number):
        
        if name in self.contacts:
            print(self.contacts)
            print('Contact already exists.')
        else:
            self.contacts[name]=number
            
    def remove_entry(self,name):
        if name in self.contacts:
            print('Would you like to remove',name,'from your contacts?')
            r=input()
            if r=='yes':
                self.contacts.pop(name)
            elif r=='no':
                print('Please try again')
        else:
            print('Contact not found.')
            
    def display(self,name):
        if name in self.contacts:
            print(self.contacts[name])
        else:
            print('Phone number not found.')
    def display_all(self):
        for c in self.contacts:
            print(c,':',self.contacts[c])
        

my_contacts=Phonebook()'''

#Question 9

class Zoo:
    def __init__(self,name):
        self.name=name
        self.p={}
        self.f={}
        self.h={}
       
    def add_animal(self,animal,population,food,habitat):
        self.p[animal]=population
        self.f[animal]=food
        self.h[animal]=habitat

    def remove_animal(self,animal):
        if animal in self.p:
            self.p.pop(animal)
        if animal in self.f:
            self.f.pop(animal)
        if animal in self.h:
            self.h.pop(animal)
    def display_animal(self):
        for animal in self.p:
            print(animal,':')
            print('Population:',self.p[animal])
            print('Food:',self.f[animal])
            print('Habitat:',self.h[animal])
            print()
zoo1=Zoo('SFzoo')


    
        
        
    
        
    
    

