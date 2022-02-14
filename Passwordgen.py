from random import *
from tkinter import *

#***********************************constans************************************
passwd=[]
num='0123456789'
alphanum='abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special='abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ*-/!#$%^&~'

#*******************************************************************************
'''
user=int(input("Enter length of password to generate: "))
ask=int(input("1.Numaric\n2.Alphanum\n3.Alpanum with spical characters\nEnter your Tchoice: "))
if ask==1:
    for i in range(user):
        passwd.append(Tchoice(num))
elif ask==2:
    for i in range(user):
        passwd.append(Tchoice(alphanum))
elif ask==3:
    for i in range(user):
        passwd.append(Tchoice(special))
else:
    print("Invalid command...")
box=''.join(passwd)
print(f"Your password:  {box}")'''

#**************************************GUI**************************************
def create_pass():
    Thechoice=Tchoice.get()
    if Thechoice=="":
        box.delete(0.0,END)
        box.insert(END,"\nSelect the type of password you'd like ")
    length=int(size.get())
    passwd=[]
    for i in range(length):
        passwd.append(choice(Thechoice))
    result=''.join(passwd)
    Thebox=f"Your password is: {result}"
    box.delete(0.0,END)
    box.insert(END,Thebox)



win=Tk()
win.configure(bg='gray')
win.geometry('800x450')
win.title("Password Genrator💡")
Name=Label(win,font=('Lucida Console',18,'bold'),text="Password Generator 🔒",fg='blue')
Name.grid(row=1,column=3,padx=250,pady=30)

choose=Label(win,font=('Lucida Console',16,'bold'),text=" ⚙ Choose a type among the 3 ⚙",fg='black')
choose.place(relx=.03,rely=.2)

Tchoice=StringVar()
Numchoice=Radiobutton(win,font=("Lucida Console",15,'bold'),text="Numaric ",variable=Tchoice,value=num,fg="green")
Numchoice.place(relx=.2,rely=.3)
Alphanumchoice=Radiobutton(win,font=("Lucida Console",15,'bold'),text="AlphaNumaric ",variable=Tchoice,value=alphanum,fg="green")
Alphanumchoice.place(relx=.2,rely=.4)
Specialchoice=Radiobutton(win,font=("Lucida Console",15,'bold'),text="Special ",variable=Tchoice,value=special,fg="green")
Specialchoice.place(relx=.2,rely=.5)


pass_len=Label(win,font=("Lucida Console",15,'bold'),text="Size ",fg="orange")
pass_len.place(relx=.7,rely=.35)
size=Spinbox(win,from_=8,to=100)
size.place(relx=0.7,rely=.4)
size.config(state='readonly')                   #size box can only be read

Genbutton=Button(win,font=("Lucida Console",13,'bold'),text="Generate 📂 ",fg="red",command=create_pass)
Genbutton.place(relx=.4,rely=.6)

box=Text(win,height=6,width=90)
box.place(relx=.04,rely=.7)






win.mainloop()