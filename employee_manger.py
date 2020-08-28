from tkinter import *
import sqlite3
from datetime import date


# delete entry employee table
def delete(a):
    db = sqlite3.connect('/home/adarshsingh/PycharmProjects/oms/admin/oms.db')
    cursor = db.cursor()
    cursor.execute("DELETE FROM employee WHERE emp_id=?", (a,))
    db.commit()
    db.close()


def update(emp_id, name, project, grade):
    db = sqlite3.connect('/home/adarshsingh/PycharmProjects/oms/admin/oms.db')
    db.execute("UPDATE employee SET emp_id=?,name=?,project=?,grade=? WHERE emp_id=?",
               (emp_id, name, project, grade, emp_id))
    db.commit()
    db.close()


def emp_table(emp_id, name, project, grade):
    join_date = date.today()
    emp_id = int(emp_id)
    project = int(project)
    grade = int(grade)
    db = sqlite3.connect('/home/adarshsingh/PycharmProjects/oms/admin/oms.db')
    db.execute("INSERT INTO employee(emp_id,name,project,grade,join_date) VALUES(?,?,?,?,?)",
               (emp_id, name, project, grade, join_date))
    db.commit()
    db.close()


def last_emp():
    i = 0
    db = sqlite3.connect('/home/adarshsingh/PycharmProjects/oms/admin/oms.db')
    cursor = db.cursor()
    cursor.execute("SELECT emp_id FROM employee ORDER BY grade DESC")
    for employee in cursor:
        for j in range(len(employee)):
            if employee[0] > i:
                i = employee[0]
    return i


# 1
# Delete employee
def delete_emp():
    root = Tk()
    root.geometry("300x100")
    root.minsize(300, 100)
    root.maxsize(300, 100)
    root.title("REMOVE EMPLOYEE")

    def delete_h(event=None):
        try:
            delete(int(delete_fd.get()))
            delete_response.config(text="successfully deleted")
            root.destroy()
            delete_emp()

        except:
            delete_response.config(text="error!!!")

    def out():
        root.destroy()

    # LAYOUT
    delete_lab = Label(text="ENTER EMP_ID")
    delete_lab.place(x=1, y=1)
    delete_fd = Entry(root)
    delete_fd.place(x=120, y=1)
    delete_bt = Button(text="Delete", command=delete_h)
    delete_bt.place(x=60, y=30)
    delete_cancel = Button(text="cancel", command=out)
    delete_cancel.place(x=150, y=30)
    delete_response = Label(text="!!Check before deleting")
    delete_response.place(x=60, y=70)
    root.bind('<Return>', delete_h)
    root.mainloop()


# 2
# emp performance set
def emp_p():
    root = Tk()
    root.geometry("350x170")
    root.minsize(350, 170)
    root.maxsize(350, 170)
    root.title(" EMPLOYEE PERFORMANCE SET")

    def get(event=None):
        x = int(emp_id.get())
        single_emp(x)

    def ok():
        if emp_name_fd.get() == "":
            response.config(text="Name field could not be empty")
        else:
            try:
                update(int(emp_id.get()), emp_name_fd.get(), int(emp_project_fd.get()), int(emp_grade_fd.get()))
                response.config(text="operation Successful ")
            except:
                response.config(text="error!!!!!")

    def out():
        root.destroy()

    # LAYOUT
    emp_id_lb = Label(root, text="Employee id *")
    emp_id_lb.place(x=1, y=1)
    emp_id = Entry(root)
    emp_id.place(x=150, y=1)
    emp_name = Label(root, text="Employee Name *")
    emp_name.place(x=1, y=30)
    emp_name_fd = Entry(root)
    emp_name_fd.place(x=150, y=30)
    emp_project = Label(root, text="Employee Project")
    emp_project.place(x=1, y=60)
    emp_project_fd = Entry(root)
    emp_project_fd.place(x=150, y=60)
    emp_grade = Label(root, text="Employee Grade ")
    emp_grade.place(x=1, y=90)
    emp_grade_fd = Entry(root)
    emp_grade_fd.place(x=150, y=90)
    emp_project_fd.insert(0, "0")
    emp_grade_fd.insert(0, "0")
    response = Label(root)
    response.place(x=100, y=150)
    b1 = Button(root, text="Get", command=get)
    b1.place(x=100, y=120)
    b2 = Button(root, text="Close", command=out)
    b2.place(x=200, y=120)
    b3 = Button(root, text="ok", command=ok)
    b3.place(x=30, y=120)
    root.bind('<Return>', get)

    def single_emp(emp):
        db = sqlite3.connect('/home/adarshsingh/PycharmProjects/oms/admin/oms.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM employee WHERE emp_id=?", (emp,))
        records = cursor.fetchall()
        for row in records:
            emp_name_fd.insert(END, row[1])
            emp_project_fd.insert(END, row[2])
            emp_grade_fd.insert(END, row[3])
        db.close()

    root.mainloop()


# 3
# Show employee
def show_emp():
    root = Tk()
    root.geometry("430x400")
    root.title("emp info")

    db = sqlite3.connect("/home/adarshsingh/PycharmProjects/oms/admin/oms.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employee ORDER BY grade DESC")
    i = 0
    f = Entry(root, width=10, fg='white', bg='black')
    f.grid(row=0, column=0)
    g = Entry(root, width=10, fg='white', bg='black')
    g.grid(row=0, column=1)
    h = Entry(root, width=10, fg='white', bg='black')
    h.grid(row=0, column=2)
    k = Entry(root, width=10, fg='white', bg='black')
    l = Entry(root, width=10, fg='white', bg='black')
    l.grid(row=0, column=4)
    k.grid(row=0, column=3)
    f.insert(END, "EMP-ID")
    g.insert(END, "Name")
    h.insert(END, "Projects")
    k.insert(END, "Grade")
    l.insert(END, "Join_Date")
    for employee in cursor:
        for j in range(len(employee)):
            e = Entry(root, width=10, fg='blue')
            e.grid(row=i + 10, column=j)
            e.insert(END, employee[j])
        i = i + 1

    root.mainloop()


# 4
# Add emp
def add_emp():
    root = Tk()
    root.geometry("350x170")
    root.minsize(350, 170)
    root.maxsize(350, 170)
    root.title("ADD EMPLOYEE")

    # LAYOUT
    emp_id_lb = Label(root, text="Employee id *")
    emp_id_lb.place(x=1, y=1)
    emp_id = Entry(root)
    emp_id.place(x=150, y=1)
    emp_name = Label(root, text="Employee Name *")
    emp_name.place(x=1, y=30)
    emp_name_fd = Entry(root)
    emp_name_fd.place(x=150, y=30)
    emp_project = Label(root, text="Employee Project")
    emp_project.place(x=1, y=60)
    emp_project_fd = Entry(root)
    emp_project_fd.place(x=150, y=60)
    emp_grade = Label(root, text="Employee Grade ")
    emp_grade.place(x=1, y=90)
    emp_grade_fd = Entry(root)
    emp_grade_fd.place(x=150, y=90)
    emp_project_fd.insert(0, "0")
    emp_grade_fd.insert(0, "0")
    response = Label(root)
    response.place(x=100, y=150)
    emp_id.insert(END, last_emp() + 1)
    emp_id.config(state='readonly')
    emp_project_fd.config(state='readonly')

    # ok function
    def ok(event=None):
        emp_table(emp_id.get(), emp_name_fd.get(), emp_project_fd.get(), emp_grade_fd.get())
        response.config(text="Entry Successful")
        root.destroy()
        add_emp()

    def close():
        root.destroy()

    root.bind('<Return>', ok)
    b1 = Button(root, text="ok", command=ok)
    b1.place(x=100, y=120)
    b2 = Button(root, text="Close", command=close)
    b2.place(x=200, y=120)

    root.mainloop()
