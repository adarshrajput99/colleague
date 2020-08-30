from tkinter import *
from employee import emp_func_batch
from admin import cloud
from employee import users_start

def download_req(emp_id):
    root = Tk()
    root.geometry("300x300")
    root.title("File Download")
    get_f = Button(text="Get available files",command=emp_func_batch.available_files)
    get_f.place(x=75, y=0)
    get_file_fd = Entry(root)
    get_file_fd.insert(END, "Paste the file name here")
    get_file_fd.place(width=299, height=30)
    get_file_fd.place(x=0,y=35)

    def ok():
        cloud.download(get_file_fd.get())

    def reverse():
        root.destroy()
        users_start.usr_start(emp_id)

    get = Button(text="Download",command=ok,width=10)
    get.place(x=40,y=68)
    close= Button(text="CLOSE", command=exit,width=10)
    close.place(x=155,y=68)
    back = Button(text="<-",command=reverse)
    back.place(x=0,y=0)

    root.mainloop()


if __name__ == "__main__":
    download_req(1211)