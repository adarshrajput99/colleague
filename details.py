import project_manager
import sqlite3
from tkinter import *


def details():
    root = Tk()
    root.geometry("330x400")
    root.minsize(330, 400)
    root.maxsize(330, 400)
    root.title(" Complete Database access")

    # LAYOUT
    emp_id_lb = Label(root, text="Employee id *")
    emp_id_lb.place(x=1, y=1)
    emp_id_fd = Entry(root)
    emp_id_fd.place(x=150, y=1)
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
    proj_id_lb = Label(root, text="Project id *")
    proj_id_lb.place(x=1, y=120)
    proj_id_fd = Entry(root)
    proj_id_fd.place(x=150, y=120)
    emp_grade_fd.place(x=150, y=90)
    proj_Name_lb = Label(root, text="Project Name *")
    proj_Name_lb.place(x=1, y=150)
    proj_Name_fd = Entry(root)
    proj_Name_fd.place(x=150, y=150)
    proj_date_lb = Label(root, text="Project End date ")
    proj_status_lb = Label(root, text="Project Status ")
    proj_date_lb.place(x=1, y=180)
    proj_status_lb.place(x=1, y=210)
    proj_date_fd = Entry(root)
    proj_status_fd = Entry(root)
    proj_date_fd.place(x=150, y=180)
    proj_status_fd.place(x=150, y=210)
    response = Label(root, text="* DENOTES FILL ONE OF THESE FIELD TO SEARCH")
    response.place(x=1, y=320)
    emp_join_date = Label(root, text="Emp join date")
    emp_join_date.place(x=1, y=240)
    emp_join_date_fd = Entry(root)
    emp_join_date_fd.place(x=150, y=240)

    def single_proj(emp):
        db = sqlite3.connect('oms.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM project WHERE assign=?", (emp,))
        records = cursor.fetchall()
        for row in records:
            proj_id_fd.insert(END, row[0])
            proj_Name_fd.insert(END, row[1])
            proj_date_fd.insert(END, row[3])
            proj_status_fd.insert(END, row[4])
        db.close()

    def single_proj_id(proj_id):
        db = sqlite3.connect('oms.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM project WHERE proj_id=?", (proj_id,))
        records = cursor.fetchall()
        for row in records:
            proj_Name_fd.insert(END, row[1])
            emp_id_fd.insert(END, row[2])
            proj_date_fd.insert(END, row[3])
            proj_status_fd.insert(END, row[4])
            return row[2]
        db.close()

    def single_proj_name(name):
        db = sqlite3.connect('oms.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM project WHERE proj_name=?", (name,))
        records = cursor.fetchall()
        for row in records:
            proj_id_fd.insert(END, row[0])
            emp_id_fd.insert(END, row[2])
            proj_date_fd.insert(END, row[3])
            proj_status_fd.insert(END, row[4])
            return row[2]
        db.close()

    def single_emp(emp):
        db = sqlite3.connect('oms.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM employee WHERE emp_id=?", (emp,))
        records = cursor.fetchall()
        for row in records:
            emp_name_fd.insert(END, row[1])
            emp_project_fd.insert(END, row[2])
            emp_grade_fd.insert(END, row[3])
            emp_join_date_fd.insert(END, row[4])
        db.close()

    def get_det_emp_name(name):
        db = sqlite3.connect('oms.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM employee WHERE name=?", (name,))
        records = cursor.fetchall()
        for row in records:
            emp_id_fd.insert(END, row[0])
            emp_project_fd.insert(END, row[2])
            emp_grade_fd.insert(END, row[3])
            return row[0]
        db.close()

    def fill(emp_id_a, emp_name_a, proj_id, proj_name):

        if emp_id_a != "":
            if project_manager.search(int(emp_id_fd.get())):

                single_emp(int(emp_id_fd.get()))
                single_proj(int(emp_id_fd.get()))

            else:
                response.config(text="Id not found")
        elif emp_name_a != "":
            if project_manager.search_name(emp_name_a):
                single_proj(get_det_emp_name(emp_name_a))
            else:
                response.config(text="name not found")
        elif proj_id != "":
            if project_manager.search_proj(int(proj_id)):
                single_emp(single_proj_id(int(proj_id)))
            else:
                response.config(text="id not found")
        elif proj_name != "":
            if project_manager.search_proj_name(proj_name):
                single_emp(single_proj_name(proj_name))

        else:
            response.config(text="*********( Operational error )************ ")

    def get(event=None):
        fill(emp_id_fd.get(), emp_name_fd.get(), proj_id_fd.get(),
             proj_Name_fd.get())

    b1 = Button(root, text="   SEARCH   ", command=get)
    b1.place(x=100, y=280)
    root.bind('<Return>', get)

    root.mainloop()


if __name__ == '__main__':
    details()
