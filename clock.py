from tkinter import *
import time

#function for showing time
def show_time():
    current_time=time.strftime("%H : %M : %S")
    clock.config(text=current_time)
    clock.after(200,show_time)           #changes time for every 100 milliseconds by calling same func
    return

frame=Tk()
frame.title("Clock")
frame.config(bg="Black")
frame.geometry("600x200")
frame.resizable(0,0)
clock=Label(frame,font=("Cuckoo",84,"bold"),bg="Black",fg="cyan")
l1=Label(frame,text=" Hours              Minutes           Seconds", font=("Cuckoo",24,"bold") ,bg="Black",fg="yellow" )
clock.grid(row=2,column=2,padx=10,pady=10)
l1.grid(row=3,column=2)
show_time()


frame.mainloop()
