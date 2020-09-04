from tkinter import *
from employee import emp_func_batch
from admin import cloud
from employee import users_start
import os
from admin.employee_manger import write
import time


def download_req(emp_id):
    t = time.strftime('%d/%m/%Y, %H:%M:%S', time.localtime())
    root = Tk()
    root.geometry("300x125")
    root.title("File Download")
    get_f = Button(text="Get available files",command=emp_func_batch.available_files)
    get_f.place(x=75, y=0)
    get_file_fd = Entry(root)
    get_file_fd.insert(END, "Paste the file name here")
    get_file_fd.place(width=299, height=30)
    get_file_fd.place(x=0, y=35)

    def ok():
        cloud.download(get_file_fd.get())
        write("#{/*DOWNLOAD*/" + t + "->" + get_file_fd.get() + "}",emp_id)


    def reverse():
        root.destroy()
        users_start.usr_start(emp_id)

    get = Button(text="Download",  command=ok,width=10)
    get.place(x=40,y=68)
    close= Button(text="CLOSE", command=exit,width=10)
    close.place(x=155,y=68)
    back = Button(text="<-", command=reverse)
    back.place(x=0, y=0)
    file_path = Label(text="File path")
    file_path_fd = Entry(root)
    file_path.place(x=0,y=100)
    file_path_fd.place(width=230)
    file_path_fd.place(x=65, y=100)
    file_path_fd.insert(END,os.path.expanduser("~")+"/Downloads/" )


    root.mainloop()


if __name__ == "__main__":
    download_req(1211)