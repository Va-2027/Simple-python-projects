from tkinter import *
#functions for each button
def button_click(number):
    current_num=e.get()
    e.delete(0,END)
    e.insert(0,str(current_num)+str(number))
    return
def button_dot(string):
    current_num=e.get()
    e.delete(0,END)
    e.insert(0,str(current_num)+str(string))
    return
def button_clear():
    e.delete(0,END)
    return
def button_add():
    first_number=e.get()      #first_number = present number
    global expression               #expression is global cuz to add operator and num in form of string
    expression=(str(first_number)+"+")
    e.delete(0,END)
    return
def button_subtract():
    first_number = e.get()
    global expression                      #
    expression = (str(first_number) + "-")
    e.delete(0, END)
    return
def button_multiply():
    first_number = e.get()
    global expression   #
    expression = (str(first_number) + "*")
    e.delete(0, END)
    return
def button_divide():
    first_number = e.get()
    global expression  #
    expression = (str(first_number) + "/")
    e.delete(0, END)
    return
def button_equal():
    second_number=e.get()
    end_value=(str(expression)+str(second_number))
    e.delete(0,END)
    try :
         e.insert(0, eval(end_value))
    except:
          e.insert(0,"Error!!")
    return



#end of functions for each buttons

root=Tk()
root.title("Simple calculator")
root.geometry("420x440")     #geometry
root.resizable(0,0)          #disabling resize of the main window

e=Entry(root,width=45,fg="blue",bg="#fcf9ed",borderwidth=4,font=("Cuckoo",12,"bold"))
e.grid(row=0,column=0,columnspan=4,ipadx=2,ipady=15)

# creating number buttons
mybutton_1=Button(root,text='1',font=("Cuckoo",14,"bold"),bg="#DFC98A",padx=40,pady=20,command=lambda:button_click(1))
mybutton_2=Button(root,text='2',font=("Cuckoo",14,"bold"),bg="#DFC98A",padx=40,pady=20,command=lambda:button_click(2))
mybutton_3=Button(root,text='3',font=("Cuckoo",14,"bold"),bg="#DFC98A",padx=40,pady=20,command=lambda:button_click(3))
mybutton_4=Button(root,text='4',font=("Cuckoo",14,"bold"),bg="#DFC98A",padx=40,pady=20,command=lambda:button_click(4))
mybutton_5=Button(root,text='5',font=("Cuckoo",14,"bold"),bg="#DFC98A",padx=40,pady=20,command=lambda:button_click(5))
mybutton_6=Button(root,text='6',font=("Cuckoo",14,"bold"),bg="#DFC98A",padx=40,pady=20,command=lambda:button_click(6))
mybutton_7=Button(root,text='7',font=("Cuckoo",14,"bold"),bg="#DFC98A",padx=40,pady=20,command=lambda:button_click(7))
mybutton_8=Button(root,text='8',font=("Cuckoo",14,"bold"),bg="#DFC98A",padx=40,pady=20,command=lambda:button_click(8))
mybutton_9=Button(root,text='9',font=("Cuckoo",14,"bold"),bg="#DFC98A",padx=40,pady=20,command=lambda:button_click(9))
mybutton_0=Button(root,text='0',font=("Cuckoo",14,"bold"),bg="#DFC98A",padx=40,pady=20,command=lambda:button_click(0))

#creating operation buttons
mybutton_add=Button(root,text='+',font=("Cuckoo",14,"bold"),bg="cyan",padx=40,pady=20,command=button_add)
mybutton_subtract=Button(root,text='-',font=("Cuckoo",14,"bold"),bg="cyan",padx=40,pady=20,command=button_subtract)
mybutton_multiply=Button(root,text='*',font=("Cuckoo",14,"bold"),bg="cyan",padx=39,pady=20,command=button_multiply)
mybutton_divide=Button(root,text='/',font=("Cuckoo",14,"bold"),bg="cyan",padx=41,pady=20,command=button_divide)

#equals and clear
mybutton_equal=Button(root,text='=',font=("Cuckoo",14,"bold"),bg="cyan",padx=37,pady=20,command=button_equal)
mybutton_clear=Button(root,text='Clear',font=("Cuckoo",14,"bold"),bg="#FE8484",padx=17,pady=20,command=button_clear)
mybutton_dot=Button(root,text='.',font=("Cuckoo",14,"bold"),bg="cyan",padx=41,pady=20,command=lambda:button_dot('.'))

#arranging buttons

mybutton_clear.grid(row=1,column=3)

mybutton_7.grid(row=2,column=0)
mybutton_8.grid(row=2,column=1)
mybutton_9.grid(row=2,column=2)
mybutton_divide.grid(row=2,column=3)

mybutton_4.grid(row=3,column=0)
mybutton_5.grid(row=3,column=1)
mybutton_6.grid(row=3,column=2)
mybutton_multiply.grid(row=3,column=3)

mybutton_1.grid(row=4,column=0)
mybutton_2.grid(row=4,column=1)
mybutton_3.grid(row=4,column=2)
mybutton_subtract.grid(row=4,column=3)

mybutton_0.grid(row=5,column=0)
mybutton_dot.grid(row=5,column=1)
mybutton_add.grid(row=5,column=2)
mybutton_equal.grid(row=5,column=3)

root.mainloop()