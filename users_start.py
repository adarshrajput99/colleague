from tkinter import *
from employee import emp_func_batch
from admin import file
import time


def usr_start(emp_id):
    root = Tk()
    root.geometry("1000x400")
    root.title("User Handel")

    def file_get_upload():
        root.destroy()
        file.file_get()

    def file_get_download():
        pass

    user_id_lb = Label(text="User_id :")
    user_id = Entry(root)
    user_name_lb = Label(text="User Name :")
    user_name = Entry(root)
    user_join_lb = Label(text="Joined on :")
    user_join = Entry(root)
    grade_lb = Label(text="Grade :")
    grade = Entry(root)
    sal_lb = Label(text="Your salary will be in range: ", font=('Helvetica', 18, 'bold'))
    start_lb = Label(text="Start from  :")
    end_lb = Label(text="Upto           :")
    file_lb= Label(text="Project", font=('Helvetica', 20, 'bold'))
    feedback_lb= Label(text="Feedback:(For last submission)", font=('Helvetica', 15, 'bold') )
    start = Entry(root)
    end = Entry(root)
    feedback = Entry(root)
    upload = Button(text="UPLOAD FILES", width=20, height=3, command=file_get_upload, font=('Helvetica', 11, 'bold'), bg='black',fg='white')
    download = Button(text="DOWNLOAD FILES", width=20, height=3, command=file_get_download, font=('Helvetica', 11, 'bold'), bg='black',fg='white')
    date = Label(text='')
    note = Label(text="Always check before uploading",font=('Helvetica', 10, 'bold'))

    def clock():
        t = time.strftime('%d/%m/%Y, %H:%M:%S', time.localtime())
        if t != '':
            date.config(text=t, font=('Helvetica', 12, 'bold'))
        root.after(100, clock)

    date.place(x=840, y=38)
    root.after(100, clock)
    user_id_lb.place(x=0, y=0)
    user_id.place(x=60, y=0)
    user_name_lb.place(x=250, y=0)
    user_name.place(x=335, y=0)
    user_join_lb.place(x=520, y=0)
    user_join.place(x=590, y=0)
    grade_lb.place(x=775, y=0)
    grade.place(x=825, y=0)
    sal_lb.place(x=0, y=30)
    start_lb.place(x=0, y=70)
    end_lb.place(x=0, y=92)
    start.place(x=75, y=70)
    end.place(x=75, y=92)
    upload.place(x=400, y=70)
    download.place(x=600, y=70)
    file_lb.place(x=550, y=35)
    feedback.place(x=2, y=150)
    feedback.place(width=300, height=200)
    feedback_lb.place(x=0, y=125)
    note.place(x=490,y=140)

    user_id.insert(END, emp_id)
    user_name.insert(END, (emp_func_batch.get_name(int(emp_id))))
    user_join.insert(END, emp_func_batch.get_date(int(emp_id)))
    grade.insert(END, emp_func_batch.get_grade(int(emp_id)))
    start.insert(END, emp_func_batch.get_salary_start(int(emp_id)))
    end.insert(END, emp_func_batch.get_salary_end(int(emp_id)))
    feedback.insert(END, "No Feedback")
    feedback.config(state='readonly')
    root.mainloop()


if __name__ == "__main__":
    usr_start('1211')
