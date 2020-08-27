from tkinter import *
from employee import emp_func_batch


def usr_start(emp_id):
    root = Tk()
    root.geometry("1000x400")
    root.title("User Handel")

    user_id_lb = Label(text="User_id :")
    user_id = Entry(root)
    user_name_lb = Label(text="User Name :")
    user_name = Entry(root)
    user_join_lb = Label(text="Joined on :")
    user_join = Entry(root)
    grade_lb = Label(text="Grade :")
    grade = Entry(root)
    sal_lb = Label(text="your salary will be in range: ",font=('Helvetica',18,'bold'))
    start_lb = Label(text="Start from  :")
    end_lb = Label(text="Upto           :")
    start = Entry(root)
    end = Entry(root)

    user_id_lb.place(x=0, y=0)
    user_id.place(x=60, y=0)
    user_name_lb.place(x=250, y=0)
    user_name.place(x=335, y=0)
    user_join_lb.place(x=520, y=0)
    user_join.place(x=590, y=0)
    grade_lb.place(x=775, y=0)
    grade.place(x=825, y=0)
    sal_lb.place(x=0,y=30)
    start_lb.place(x=0,y=70)
    end_lb.place(x=0,y=92)
    start.place(x=75,y=70)
    end.place(x=75,y=92)

    user_id.insert(END, emp_id)
    print(type(emp_id))
    user_name.insert(END,(emp_func_batch.get_name(int(emp_id))))
    user_join.insert(END,emp_func_batch.get_date(int(emp_id)))
    grade.insert(END,emp_func_batch.get_grade(int(emp_id)))
    start.insert(END,emp_func_batch.get_salary_start(int(emp_id)))
    end.insert(END,emp_func_batch.get_salary_end(int(emp_id)))

    root.mainloop()


if __name__=="__main__":
    usr_start('1211')
