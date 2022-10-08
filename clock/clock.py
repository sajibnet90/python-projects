from tkinter import *
from time import *

def update():
    time_string= strftime("%H:%M:%S")
    time_lebel.config(text=time_string)

    day_string=strftime("%A")
    day_lebel.config(text=day_string)

    date_string = strftime("%B %d,%Y")
    date_lebel.config(text=date_string)

    window.after(1000,update)#time_lebel.after(1000,update)

window= Tk()
window.title("Clock")

time_lebel = Label(window,font=("Arial",50),bg="black",fg="#00FF00")
time_lebel.pack()

day_lebel= Label(window,font=("Arial",25))
day_lebel.pack()

date_lebel= Label(window,font=('Arial',30),bg="blue")
date_lebel.pack()


update()

window.mainloop()