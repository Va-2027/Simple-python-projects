from tkinter import *
import random

#function to roll dice
def roll():
    number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']    #ascii value
    l1.config(text=f'{random.choice(number)}')
    l1.pack(expand=True, fill="both")


# main window create
frame=Tk()
frame.title("Dice Roller")
frame.geometry("400x400")
frame.resizable(0,0)
frame.config(bg="#befc03")

#label for dice
l1=Label(frame,text='',font=("times",300),bg="#befc03",fg="blue")

label1=Label(frame,text="Let's Roll it !!",font=("Cuckoo",40,"bold italic"),bg="#befc03",fg="black",padx=10,pady=2)
label1.pack()
#label1.pack(expand=True,fill="both",)

#button
button_roll=Button(frame,text="Click to roll !!",font=("lucida handwriting",16,"bold italic"),padx=3,pady=4,bg="orange",fg="black",command=roll)
button_roll.place(x=100,y=350)
button_roll.pack(fill="both")
frame.mainloop()