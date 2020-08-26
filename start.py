from tkinter import *
from interface1 import login
           
root = Tk()
root.geometry("300x300")
root.maxsize(300,300)
root.minsize(300,300)
root.title("COLLEAGUE")


def click(event=None):
    root.destroy()
    login()


root.bind('<Return>', click)

photo = PhotoImage(file="asr.png")
label = Button(image=photo, command=click)
label.pack()
root.mainloop()
