from tkinter import *
from tkmacosx import Button
import webbrowser
from tkinter import messagebox
import random,time,webcolors,pytz
from datetime import datetime
root=Tk()
root.title('Hello World')

#basic application
'''
def clear():
    name_entry.delete(0,END)

def submit():
    a=name_entry.get()
    print(a)

name_label=Label(root,text='Name')
name_label.pack()

name_entry=Entry(root)
name_entry.pack()

exit_button=Button(root,text='Exit',fg='red',command=quit)
exit_button.pack(side=LEFT)

clear_button=Button(root,text='Clear',fg='blue',command=clear)
clear_button.pack(side=RIGHT)

submit_button=Button(root,text='Submit',fg='green',command=submit)
submit_button.pack()

root.mainloop()'''
'''
def clear():
    name_entry.delete(0,END)

def submit():
    a=name_entry.get()
    print(a)

name_label=Label(root,text='Name')
name_label.grid(row=0,column=0)

name_entry=Entry(root)
name_entry.grid(row=0,column=1)

exit_button=Button(root,text='Exit',fg='red',command=quit)
exit_button.grid(row=1,column=1)

clear_button=Button(root,text='Clear',fg='blue',command=clear)
clear_button.grid(row=1,column=0)

submit_button=Button(root,text='Submit',fg='green',command=submit)
submit_button.grid(row=2,column=0)

root.mainloop()'''

#################################

#exercise 1
#form application

'''def clear():
    for entry in [firstname_entry,lastname_entry,grade_entry,age_entry,city_entry]:
        entry.delete(0,END)
        
def submit():
    for entry in [firstname_entry,lastname_entry,grade_entry,age_entry,city_entry]:
        students=open('student_info.txt','a')
        students.write(entry.get())
    students.close()
                      
title=Label(root,text='Please enter the following information')
title.pack()

firstname_label=Label(root,text='First Name')
firstname_label.pack()
firstname_entry=Entry(root)
firstname_entry.pack()


Label(root,text='Last Name').pack()
lastname_entry=Entry(root)
lastname_entry.pack()

age_label=Label(root,text='Age').pack()
age_entry=Entry(root)
age_entry.pack()

grade_label=Label(root,text='Grade').pack()
grade_entry=Entry(root)
grade_entry.pack()

city_label=Label(root,text='City').pack()
city_entry=Entry(root)
city_entry.pack()

done_button=Button(root,text='Submit',fg='blue',command=submit)
done_button.pack(side=LEFT)

clear_button=Button(root,text='Clear',fg='red',command=clear).pack(side=RIGHT)



root.mainloop()'''

'''def clear():
    for entry in [firstname_entry,lastname_entry,grade_entry,age_entry,city_entry]:
        entry.delete(0,END)
        
def submit():
    for entry in [firstname_entry,lastname_entry,grade_entry,age_entry,city_entry]:
        students=open('student_info.txt','a')
        students.write(entry.get())
    students.close()
                      
title=Label(root,text='Please enter the following information')
title.grid(row=0,column=0,columnspan=2)

firstname_label=Label(root,text='First Name')
firstname_label.grid(row=1,column=0)
firstname_entry=Entry(root)
firstname_entry.grid(row=1,column=1)


Label(root,text='Last Name').grid(row=2,column=0)
lastname_entry=Entry(root)
lastname_entry.grid(row=2,column=1)

age_label=Label(root,text='Age').grid(row=3,column=0)
age_entry=Entry(root)
age_entry.grid(row=3,column=1)

grade_label=Label(root,text='Grade').grid(row=4,column=0)
grade_entry=Entry(root)
grade_entry.grid(row=4,column=1)

city_label=Label(root,text='City').grid(row=5,column=0)
city_entry=Entry(root)
city_entry.grid(row=5,column=1)

done_button=Button(root,text='Submit',fg='blue',command=submit)
done_button.grid(row=6,column=0)

clear_button=Button(root,text='Clear',fg='red',command=clear).grid(row=6,column=1)
#clear_button.pack(side=RIGHT)


root.mainloop()'''
'''
color1='white'
color2='black'
r=0
c=0
for row in range(0,8,1):
    r+=1
    c=0
    
    for column in range(0,8,1):
        label=Label(root,text='',bg=color1,width=3)
        label.grid(row=r,column=c)
        c+=1
        color1,color2=color2,color1
    color1,color2=color2,color1
        
root.mainloop()'''
'''
def calculate():
    ftemp=int(fahrenheitentry.get())
    ctemp=(ftemp-32)*5/9
    celsiusentry.insert(0,ctemp)

def clear():
    for entry in [fahrenheitentry,celsiusentry]:
        entry.delete(0,END)
   
fahrenheitlabel=Label(root,text='Fahrenheit')
fahrenheitlabel.grid(row=0,column=0)
fahrenheitentry=Entry(root)
fahrenheitentry.grid(row=0,column=1)

Label(root,text='Celsius').grid(row=1,column=0)
celsiusentry=Entry(root)
celsiusentry.grid(row=1,column=1)

calculatebutton=Button(root,text='Calculate',fg='blue',command=calculate)
calculatebutton.grid(row=2,column=0)

clearbutton=Button(root,text='Clear',fg='red',command=clear)
clearbutton.grid(row=2,column=1,sticky=EW)

root.mainloop()
'''

##def openfacebook():
##    webbrowser.open_new_tab('https://www.facebook.com')
'''
usernames={'facebook':'facebookuser','instagram':'instauser','snapchat':'snapuser','twitter':'twitteruser'}


def opensite(app):
    webbrowser.open_new_tab(f'https://www.{app}.com')
    usernamelabel['text']=usernames[app]

c=r=0
for site in usernames:
    button=Button(root,text=site,fg='black',bg='lightblue',command=lambda site=site: opensite(site))
    button.grid(row=r,column=c,sticky=EW)
    
    
    c+=1
    if c>=2:
        c=0
        r+=1



instabutton=Button(root,text='Instagram',fg='white',bg='orange',command=lambda: opensite('instagram'))
instabutton.grid(row=1,column=0,sticky=EW)

facebookbutton=Button(root,text='Facebook',fg='white',bg='blue',command=lambda: opensite('facebook'))
facebookbutton.grid(row=0,column=0,sticky=EW)

snapbutton=Button(root,text='Snapchat',fg='black',bg='yellow',command=lambda: opensite('snapchat'))
snapbutton.grid(row=1,column=1,sticky=EW)

twitterbutton=Button(root,text='Twitter',fg='black',bg='lightblue',command=lambda: opensite('twitter'))
twitterbutton.grid(row=0,column=1,sticky=EW)

usernamelabel=Label(root,text='')
usernamelabel.grid(row=2,column=0,columnspan=2,sticky=EW)'''


'''
info={'facebookuser':'facebookpassword','instagramuser':'instapassword','snapchatuser':'snappassword','twitteruser':'twitterpassword'}

def clear():
    for entry in [usernameentry,passwordentry]:
        entry.delete(0,END)

def login():
    username=usernameentry.get()
    password=passwordentry.get()
    if username in info:
        if info[username]==password:
            print('accessgranted')
            m1=messagebox.showinfo('Congratulations','Access Granted')
            print(m1)
        else:
            print('accessdenied')
            m2=messagebox.showerror('Error','Incorrect Password')

    else:
        print('accessdenied')
        m2=messagebox.showerror('Error','Incorrect Username')
        
Label(root,text='Username',font='Arial 10 bold').grid(row=0,column=0)
Label(root,text='Password',font='Arial 10 bold').grid(row=1,column=0)

usernameentry=Entry(root)
usernameentry.grid(row=0,column=1)

passwordentry=Entry(root)
passwordentry.grid(row=1,column=1)

clearbutton=Button(root,text='Clear',fg='red',command=clear)
clearbutton.grid(row=2,column=0,sticky=EW)
loginbutton=Button(root,text='Login',fg='blue',command=login)
loginbutton.grid(row=2,column=1,sticky=EW)'''

'''
def clear():
    for entry in [numentry]:
        entry.delete(0,END)
        
def guess():
    num=int(numentry.get())
    if num<realnum:
        more=messagebox.showinfo('More','The real number is greater than your guess')
    elif num>realnum:
        less=messagebox.showinfo('Less','The real number is less than your guess')
    elif num==realnum:
        equal=messagebox.showinfo('Correct!','Correct!')
        
realnum=random.randint(1,100)
Label(root,text='Guess number from 1-100').grid(row=0,column=0)
numentry=Entry(root)
numentry.grid(row=0,column=1)

clearbutton=Button(root,text='Clear',fg='blue',command=clear)
clearbutton.grid(row=1,column=0,sticky=W)
guessbutton=Button(root,text='Guess',fg='darkgreen',command=guess)
guessbutton.grid(row=1,column=0,columnspan=2)
quitbutton=Button(root,text='Quit',fg='red',command=quit)
quitbutton.grid(row=1,column=1,sticky=E)'''


'''

wordlist=['apple','banana','carrot','dragonfruit','egg','fish','grapes']
start=True
points=0

def submit():
    global points
    entryword=wordentry.get()
    if entryword==wordlist[0]:
        if len(wordlist)==1:
            points+=1
            pointslabel['text']='Points:'+str(points)
            finish=messagebox.showinfo('Done','Game Over! Total points:'+str(points))
            return
        wordlist.remove(wordlist[0])
        correct=messagebox.showinfo('Correct','Correct!')
        wordentry.delete(0,END)
        changebutton()
        points+=1
        pointslabel['text']='Points:'+str(points)
        
    elif entryword!=wordlist[0] :
        incorrect=messagebox.showinfo('Incorrect','Incorrect,try again')
        changebutton()
        wordentry.delete(0,END)
        

def jumbleword(word):
    jumble=word
    jumble=list(jumble)
    random.shuffle(jumble)
    jumble=''.join(jumble)
    return jumble


def changebutton():
    start=False
    random.shuffle(wordlist)
    
    jumble=jumbleword(wordlist[0])
    
    print(jumble)
    print(wordlist)
    wordlabel['text']=jumble
    startbutton['text']='GUESS THE JUMBLED WORD'
    wordlabel['bg']='aqua'
    pointslabel.grid(row=2,column=0,sticky=EW)
    
startbutton=Button(root,text='CLICK TO START',bg='orange',fg='black',command=changebutton)
startbutton.grid(row=0,column=0,columnspan=2,sticky=EW)



    
    
wordentry=Entry(root)
wordentry.grid(row=1,column=1)

wordlabel=Label(root,text='')
wordlabel.grid(row=1,column=0,sticky=EW)

submitbutton=Button(root,text='Submit',fg='darkgreen',command=submit)
submitbutton.grid(row=2,column=1,sticky=EW)

pointslabel=Label(root,text='Points:0',fg='blue')


root.mainloop()'''

'''
def randomnum():
    r=numentry.get()
    s,e=r.split('-')
    s=int(s)
    e=int(e)
    n=random.randint(s,e)
    result.set(n)
    ##number.set(n)
    ##number['text']=str(n)

result=IntVar()
number=Label(root,textvariable=result)
number.grid(row=1,column=0)

numentry=Entry(root)
numentry.grid(row=0,column=1)

generate=Button(root,text='Generate',command=randomnum)
generate.grid(row=1,column=1)'''

'''
def square():
    n=int(numentry.get())
    n=n**2
    n=round(n,2)
    r.set(n)
    
def sqrt():
    n=int(numentry.get())
    n=n**0.5
    n=round(n,2)
    r.set(n)

Label(root,text='Number').grid(row=0,column=0)
numentry=Entry(root)
numentry.grid(row=0,column=1)

r=DoubleVar()
numlabel=Label(root,textvariable=r)
numlabel.grid(row=1,column=1)

squarebutton=Button(root,text='Square',command=square)
squarebutton.grid(row=2,column=0)

sqrtbutton=Button(root,text='Square Root',command=sqrt)
sqrtbutton.grid(row=2,column=1)

root.mainloop()'''




'''
def subtract():
    if itemnumber.get()>1:
        itemnumber.set(itemnumber.get()-1)
    
    
def add():
    itemnumber.set(itemnumber.get()+1)

def additem():
    items[itementry.get()]=itemnumber.get()
    print(items)
    itementry.delete(0,END)
    itemnumber.set(0)
    

def checkout():
    msg=messagebox.showinfo('Cart',items)
    if msg=='ok':
        root.destroy()

items={}

itemnumber=IntVar()


Label(root,text='Please enter an item').grid(row=0,column=0)
Label(root,text='Choose the quantity').grid(row=1,column=0)

itementry=Entry(root)
itementry.grid(row=0,column=1,columnspan=3)

minus=Button(root,text='-',fg='red',command=subtract)
minus.grid(row=1,column=1)

plus=Button(root,text='+',fg='darkgreen',command=add)
plus.grid(row=1,column=3)

itemlabel=Label(root,textvariable=itemnumber)
itemlabel.grid(row=1,column=2)

addtocart=Button(root,text='Add to Cart',command=additem)
addtocart.grid(row=2,column=1,columnspan=3)

checkoutbutton=Button(root,text='Checkout',command=checkout)
checkoutbutton.grid(row=2,column=0,ipady=10)'''

'''
h=0
m=0
s=0
t=False
def timeon():
    global h,m,s,t 
    t=True
    
       
def timeoff():
    global t
    t=False
    

def reset():
    global h,m,s,t
    timevar.set('0:0:0')
    t=False
    s=0
    m=0
    h=0

    
timevar=StringVar()
timevar.set('0:0:0')

timer=Label(root,textvariable=timevar)
timer.grid(row=0,column=0,columnspan=3,sticky=EW)

startbutton=Button(root,text='Start',command=timeon)
startbutton.grid(row=1,column=0)

stopbutton=Button(root,text='Stop',command=timeoff)
stopbutton.grid(row=1,column=1)

resetbutton=Button(root,text='Reset',command=reset)
resetbutton.grid(row=1,column=2)

# can change to increments of 0.1 to make page more responsive
while True:
    if t==True:
        time.sleep(1)
        s+=1
        if s==60:
            m+=1
            s=0
        if m==60:
            h+=1
            m=0
        timevar.set(f'{h}:{m}:{s}')
    root.update()'''





'''
colorlist=['red','orange','yellow','green','blue','purple','pink','brown','black','gray']

def changecolorandword():
    ''''''if pointsvar.get()==0 and word['fg']==colorlist[6] and wordofcolor==colorlist[8]:
        if entry.get()==colorlist[6]:
            x+=1
            pointsvar.set()''''''
    if entry.get()==colorlist[1]:
        pointsvar.set(pointsvar.get()+1)
    else:
        msg=messagebox.showinfo('Incorrect','Incorrect! You lose. Points: '+str(pointsvar.get()))
    random.shuffle(colorlist)
    wordofcolor.set(colorlist[0])
    word['fg']=colorlist[1]
    print('word on screen:',colorlist[0])
    print('color of word:',colorlist[1])
    
    
    
#initial color
#colorlist[0] = word
#colorlist[1] = color of word
random.shuffle(colorlist)

pointsvar=IntVar()
wordofcolor=StringVar(value=colorlist[0])

score=Label(root,textvariable=pointsvar)
score.grid(row=0,column=0)

Label(root,text='Type the color of the word shown below').grid(row=1,column=0)

word=Label(root,textvariable=wordofcolor,fg=colorlist[1])
word.grid(row=2,column=0)

entry=Entry(root)
entry.grid(row=3,column=0)

submit=Button(root,text='Submit',command=changecolorandword)
submit.grid(row=4,column=0)

root.mainloop()
'''





'''
redvar=IntVar()
greenvar=IntVar()
bluevar=IntVar()


redscale=Scale(root,label='red',variable=redvar,from_=0,to=255,orient=VERTICAL)
redscale.grid(row=0,column=0)

greenscale=Scale(root,label='green',variable=greenvar,from_=0,to=255,orient=VERTICAL)
greenscale.grid(row=0,column=1)

bluescale=Scale(root,label='blue',variable=bluevar,from_=0,to=255,orient=VERTICAL)
bluescale.grid(row=0,column=2)

colorlabel=Label(root,text='',bg='white')
colorlabel.grid(row=1,column=0,columnspan=3,sticky=EW)

while True:
    r=redvar.get()
    g=greenvar.get()
    b=bluevar.get()
    value=webcolors.rgb_to_hex((r,g,b))
    colorlabel.configure(bg=value)
    root.update()
'''

'''
blueframe=Frame(root,width=50,height=100,bg='darkblue')
blueframe.pack(side=LEFT)

whiteframe=Frame(root,width=50,height=100,bg='white')
whiteframe.pack(side=LEFT)

redframe=Frame(root,width=50,height=100,bg='red')
redframe.pack(side=RIGHT)
ç
root.mainloop()'''

'''
def NA():
    pass

indiaframe=Frame(root,width=100,height=50)
indiaframe.grid(row=0,column=0)
indiatimezone=pytz.timezone('Asia/Calcutta')
timevar=StringVar()




Label(indiaframe,text='India').pack()
Button(indiaframe,text='',bg='orange',command=NA).pack()
Label(indiaframe,textvariable=timevar).pack()

while True:
    time.sleep(1)
    currentindia=datetime.now(indiatimezone)
    final_time=currentindia.strftime('%Y-%m-%d %l:%M:%S %p %Z')
    timevar.set(final_time)
    ##

    root.update()'''






