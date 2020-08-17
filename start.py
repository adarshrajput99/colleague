from tkinter import *
from interface1 import login

root = Tk()
root.geometry("400x555")
root.title("OFFICE MANAGEMENT SYSTEM")


def click(event=None):
    root.destroy()
    login()


root.bind('<Return>', click)

photo = PhotoImage(file="asr.png")
label = Button(image=photo, command=click)
label.pack()
root.mainloop()
