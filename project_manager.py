from tkinter import *
import sqlite3


# ADDING PROJECT

def update_project(project, emp_id):
    db = sqlite3.connect('/home/adarshsingh/PycharmProjects/oms/admin/oms.db')
    db.execute("UPDATE employee SET project=? WHERE emp_id=?",
               (project + 1, emp_id))
    db.commit()
    db.close()


def get_proj(emp_id):
    db = sqlite3.connect('/home/adarshsingh/PycharmProjects/oms/admin/oms.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employee WHERE emp_id=?", (emp_id,))
    records = cursor.fetchall()
    for row in records:
        return row[2]
    db.close()


# *****************************( SEARCH SECTION )*************************************************** #
def search(emp_id):
    db = sqlite3.connect('/home/adarshsingh/PycharmProjects/oms/admin/oms.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employee Where emp_id=?", (emp_id,))
    for row in cursor.fetchall():
        return True
    else:
        return False


def search_name(name):
    db = sqlite3.connect('/home/adarshsingh/PycharmProjects/oms/admin/oms.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employee Where name=?", (name,))
    for row in cursor.fetchall():
        return True
    else:
        return False


def search_proj(proj_id):
    db = sqlite3.connect('/home/adarshsingh/PycharmProjects/oms/admin/oms.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM project Where proj_id=?", (proj_id,))
    for row in cursor.fetchall():
        return True
    else:
        return False


def search_proj_name(name):
    db = sqlite3.connect('/home/adarshsingh/PycharmProjects/oms/admin/oms.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM project Where proj_name=?", (name,))
    for row in cursor.fetchall():
        return True
    else:
        return False
# *****************************************( SEARCH END )*************************************** #


# Entry of proj
def proj_table(proj_id, proj_name, assign=None, date=None):
    if assign is not None:
        db = sqlite3.connect('/home/adarshsingh/PycharmProjects/oms/admin/oms.db')
        cursor = db.cursor()
        x = None
        cursor.execute("SELECT * FROM employee WHERE emp_id=?", (assign,))
        for row in cursor.fetchall():
            x = row

        if x is not None:
            if assign is not None or date is not None:
                db.execute("INSERT INTO project(proj_id, proj_name, assign,due ) VALUES(?,?,?,?)",
                           (proj_id, proj_name, assign, date))
                db.commit()
                db.close()
                return 1
            else:
                return 0
        else:
            return 3


# 1
# Show project progress
def proj_list():
    root = Tk()
    root.geometry("430x310")
    root.title("emp info")

    db = sqlite3.connect("/home/adarshsingh/PycharmProjects/oms/admin/oms.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM project ORDER BY proj_id ASC")
    i = 0
    f = Entry(root, width=10, fg='white', bg='black')
    f.grid(row=0, column=0)
    g = Entry(root, width=10, fg='white', bg='black')
    g.grid(row=0, column=1)
    h = Entry(root, width=10, fg='white', bg='black')
    h.grid(row=0, column=2)
    k = Entry(root, width=10, fg='white', bg='black')
    k.grid(row=0, column=3)
    l = Entry(root, width=10, fg='white', bg='black')
    l.grid(row=0, column=4)
    f.insert(END, "proj_id")
    g.insert(END, "proj_Name")
    h.insert(END, "assign_emp_id")
    k.insert(END, "End date")
    l.insert(END, "Status")
    for project in cursor:
        for j in range(len(project)):
            e = Entry(root, width=10, fg='blue')
            e.grid(row=i + 10, column=j)
            e.insert(END, project[j])
        i = i + 1

    root.mainloop()


# 2
# Add new projects
def add_proj():
    root = Tk()
    root.geometry("350x170")
    root.minsize(350, 170)
    root.maxsize(350, 170)
    root.title("ASSIGN PROJECT/PROJECT ADD")

    # LAYOUT
    proj_id_lb = Label(root, text="Project id *")
    proj_id_lb.place(x=1, y=1)
    proj_id = Entry(root)
    proj_id.place(x=150, y=1)
    proj_name = Label(root, text="Project Name *")
    proj_name.place(x=1, y=30)
    proj_name_fd = Entry(root)
    proj_name_fd.place(x=150, y=30)
    proj_assign = Label(root, text="Assign emp_id *")
    proj_assign.place(x=1, y=60)
    proj_assign_fd = Entry(root)
    proj_assign_fd.place(x=150, y=60)
    proj_date = Label(root, text="Project due Date")
    proj_date.place(x=1, y=90)
    proj_date_fd = Entry(root)
    proj_date_fd.place(x=150, y=90)
    proj_assign_fd.insert(0, "None")
    proj_date_fd.insert(0, "00-00-00")
    response = Label(root)
    response.place(x=100, y=150)

    def out():
        root.destroy()

    # ok function
    def ok(event=None):
        if search(int(proj_assign_fd.get())):
            try:
                update_project(get_proj(int(proj_assign_fd.get())), int(proj_assign_fd.get()))
                proj_table(int(proj_id.get()), proj_name_fd.get(), int(proj_assign_fd.get()),
                           proj_date_fd.get())
                response.config(text="Entry Successful")
            except:
                response.config(text="Entry failed!!!!!")
        else:
            response.config(text="emp_id not Available")
        root.destroy()
        add_proj()

    root.bind('<Return>', ok)
    b1 = Button(root, text="ok", command=ok)
    b1.place(x=100, y=120)
    b2 = Button(root, text="Close", command=out)
    b2.place(x=200, y=120)
    root.mainloop()
