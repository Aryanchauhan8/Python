import tkinter as tk
from tkinter import *

#global variable for main expression
expression=""

#input function
def inputfield(value):
    global expression
    expression += str(value)
    entry.delete(1.0, tk.END)
    entry.insert(1.0, expression)

#expression operation
def operation():
    global expression
    try:
        #eval() is function to evaluate main expression
        expression = str(eval(expression))
        entry.delete(1.0, tk.END)
        entry.insert(1.0, expression)
    except Exception as e:
        clear()
        entry.insert(1.0, "Error")

#clear operation expression
def clear():
    global expression
    expression=""
    entry.delete(1.0, tk.END)


root=tk.Tk()

#main frame
root.geometry('500x438+500+150')           #  height x  width  +xaxis  + yaxis
root.title('CALCULATOR')
root.config(bg='grey')
root.resizable(False,False)

#text field
entry=tk.Text(root,bd=5,relief=SUNKEN, height=3 , width=27, font=("Helvetica", 24))
entry.grid(columnspan=5)

#button frame
buttonframe=Frame(root,bd=10,relief=RIDGE)
buttonframe.grid(columnspan=5)

#buttons
bt1=tk.Button(buttonframe,text='1',bd=1,relief=RAISED,command=lambda:inputfield(1),width=10,height=2,font=("Helvetica", 14),activebackground='grey')
bt1.grid(row=2,column=1)

bt2=tk.Button(buttonframe,text='2',bd=1,relief=RAISED,command=lambda:inputfield(2),width=10,height=2,font=("Helvetica", 14),activebackground='grey')
bt2.grid(row=2,column=2)

bt3=tk.Button(buttonframe,text='3',bd=1,relief=RAISED,command=lambda:inputfield(3),width=10,height=2,font=("Helvetica", 14),activebackground='grey')
bt3.grid(row=2,column=3)

btd=tk.Button(buttonframe,text='/',bd=1,relief=RAISED,command=lambda:inputfield("/"),width=10,height=2,font=("Helvetica", 14),activebackground='grey')
btd.grid(row=2,column=4)

bt4=tk.Button(buttonframe,text='4',bd=1,relief=RAISED,command=lambda:inputfield(4),width=10,height=2,font=("Helvetica", 14),activebackground='grey')
bt4.grid(row=3,column=1)

bt5=tk.Button(buttonframe,text='5',bd=1,relief=RAISED,command=lambda:inputfield(5),width=10,height=2,font=("Helvetica", 14),activebackground='grey')
bt5.grid(row=3,column=2)

bt6=tk.Button(buttonframe,text='6',bd=1,relief=RAISED,command=lambda:inputfield(6),width=10,height=2,font=("Helvetica", 14),activebackground='grey')
bt6.grid(row=3,column=3)

btm=tk.Button(buttonframe,text='x',bd=1,relief=RAISED,command=lambda:inputfield("*"),width=10,height=2,font=("Helvetica", 14),activebackground='grey')
btm.grid(row=3,column=4)

bt7=tk.Button(buttonframe,text='7',bd=1,relief=RAISED,command=lambda:inputfield(7),width=10,height=2,font=("Helvetica", 14),activebackground='grey')
bt7.grid(row=4,column=1)

bt8=tk.Button(buttonframe,text='8',bd=1,relief=RAISED,command=lambda:inputfield(8),width=10,height=2,font=("Helvetica", 14),activebackground='grey')
bt8.grid(row=4,column=2)

bt9=tk.Button(buttonframe,text='9',bd=1,relief=RAISED,command=lambda:inputfield(9),width=10,height=2,font=("Helvetica", 14),activebackground='grey')
bt9.grid(row=4,column=3)

btmi=tk.Button(buttonframe,text='-',bd=1,relief=RAISED,command=lambda:inputfield("-"),width=10,height=2,font=("Helvetica", 14),activebackground='grey')
btmi.grid(row=4,column=4)

bt0=tk.Button(buttonframe,text='0',bd=1,relief=RAISED,command=lambda:inputfield(0),width=10,height=2,font=("Helvetica", 14),activebackground='grey')
bt0.grid(row=5,column=1)

btde=tk.Button(buttonframe,text='.',bd=1,relief=RAISED,command=lambda:inputfield("."),width=10,height=2,font=("Helvetica", 14),activebackground='grey')
btde.grid(row=5,column=2)

bte=tk.Button(buttonframe,text='=',bd=1,relief=RAISED,command=operation,width=10,height=2,font=("Helvetica", 14),activebackground='grey')
bte.grid(row=5,column=3)

btp=tk.Button(buttonframe,text='+',bd=1,relief=RAISED,command=lambda:inputfield("+"),width=10,height=2,font=("Helvetica", 14),activebackground='grey')
btp.grid(row=5,column=4)

btc=tk.Button(buttonframe,text='Clear',bd=1,relief=RAISED,command=clear,width=15,height=2,font=("Helvetica", 14),activebackground='grey')
btc.grid(row=6,column=2,columnspan=2)

btp1=tk.Button(buttonframe,text='(',bd=1,relief=RAISED,command=lambda:inputfield("("),width=10,height=2,font=("Helvetica", 14),activebackground='grey')
btp1.grid(row=6,column=1)

btp2=tk.Button(buttonframe,text=')',bd=1,relief=RAISED,command=lambda:inputfield(")"),width=10,height=2,font=("Helvetica", 14),activebackground='grey')
btp2.grid(row=6,column=4)


root.mainloop()