import time

'''def counter():
    for i in range(10,0,-1):
        print(i)
        time.sleep(1)

counter()
print('Ready or not here I come!')'''


'''print('How many lines do you want to add?')
n=int(input())
for i in range(0,n,1):
    print('8 8 8 8 8 8')
    print()
    print('& & & & & &')
    print()'''
    
'''s1=[]
s2=[]
s3=[]
s4=[]
s5=[]
subjects=['math','science','english','history']
scores=[s1,s2,s3,s4,s5]

for student in range(1,6,1):
    for subject in range(0,4,1):
        print ('Enter student',str(student)+"'s score for",subjects[subject])
        scores.append(int(input))'''
        
print('Enter your name')
n=input()
print('Enter your age')
a=input()
s='My name is {name} and I am {age} years old'.format(name=n,age=a)
print(s)
