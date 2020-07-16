from e import email
import tkinter
from tkinter import *
from tkinter import messagebox

root=tkinter.Tk()
root.geometry("200x300")
root.resizable(0,0)
root.title("Email Program")
objects=[]
def  check():
    if len(objects)==2:
        m=objects[0]
        b1.configure(text=m)
        b1.configure(command=lambda: AAU(1))
    if len(objects)==4:
        m=objects[2]
        b2.configure(text=m)
        b2.configure(command=lambda: AAU(2))
    if len(objects)==6:
        m=objects[4]
        b3.configure(text=m)
        b3.configure(command=lambda: AAU(3))
    if len(objects)==8:
        m=objects[6]
        b4.configure(text=m)
        b4.configure(command=lambda: AAU(4))
    else:
        pass
def decoder(n):
    dencryptedN=""
    for letter in n:
            if letter == ' ':
                dencryptedN += ' '
            else:
                dencryptedN += chr(ord(letter) - 5)
    return dencryptedN
def readfile():
    f = open(r"C:\Users\varun sharma\Desktop\personal\email program\user.txt", 'r')
    for line in f:
        entityList = line.split(',')
        m=decoder(entityList[0])
        objects.append(m)
    f.close()
readfile()
def AU():
    root1=tkinter.Tk()
    root1.geometry('250x180')
    root1.resizable(0,0)
    root1.title("Creat user")
    def addup():
        u=e.get()
        p=e1.get()
        objects.append(u)
        objects.append(p)
        check()
        encryptedN=""
        encryptedP=""
        f=open(r"C:\Users\varun sharma\Desktop\personal\email program\user.txt","a")
        for letter in u:
            if letter == ' ':
                encryptedN+= ' '
            else:
                encryptedN+= chr(ord(letter) + 5)
        for letter in p:
                if letter==' ':
                    encryptedP+=' '
                else:
                    encryptedP+=chr(ord(letter)+5)
        f.write(encryptedN+',\n'+ encryptedP+',\n')
        f.close()
        messagebox.showinfo("Sucessful","User added sucess fully")
        root1.destroy()

    l = Label(root1, text=" user name ", font=('Courier', 14), justify=CENTER)
    l.pack()
    e= Entry(root1, show='*', width=30)
    e.pack(pady=7)
    l1= Label(root1, text=" Password: ", font=('Courier', 14), justify=CENTER)
    l1.pack()
    e1= Entry(root1, show='*', width=30)
    e1.pack(pady=7)
    b= Button(root1, text='Submit', command=addup, font=('Courier', 14))
    b.pack()
def AAU(b):
    if b==1:
        root.destroy()
        x=objects[0]
        y=objects[1]
        email(x,y)
    if b==2:
        root.destroy()
        x=objects[2]
        y=objects[3]
        email(x,y)
    if b==3:
        root.destroy()
        x=objects[4]
        y=objects[5]
        email(x,y)
    if b==4:
        root.destroy()
        x=objects[6]
        y=objects[7]
        email(x,y)

l1=Label(root)
l1.pack(expand=True,fill="both")
l2=Label(root)
l2.pack(expand=True,fill="both")
l3=Label(root)
l3.pack(expand=True,fill="both")
l4=Label(root)
l4.pack(expand=True,fill="both")
b1=Button(l1,text="+ ADD User",font=("Freestyle Script", 20),command=AU)
b1.pack(expand=True,fill="both")
b2=Button(l2,text="+ ADD User",font=("Freestyle Script", 20),command=AU)
b2.pack(expand=True,fill="both")
b3=Button(l3,text="+ ADD User",font=("Freestyle Script", 20),command=AU)
b3.pack(expand=True,fill="both")
b4=Button(l4,text="+ ADD User",font=("Freestyle Script", 20),command=AU)
b4.pack(expand=True,fill="both")
check()
root.mainloop()