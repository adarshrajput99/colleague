import sqlite3
import dropbox
import tkinter

def grade_conv(temp):
    grade = 0
    if 11 > temp > 0:
        grade = 1
    elif 10 < temp < 21:
        grade = 2
    elif 20 < temp < 31:
        grade = 3
    elif 30 < temp < 41:
        grade = 4
    elif 40 < temp < 51:
        grade = 5
    elif 50 < temp < 61:
        grade = 6
    return grade


# return name by emp_id
def get_name(emp_id):
    db = sqlite3.connect('/home/adarshsingh/PycharmProjects/oms/admin/oms.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employee WHERE emp_id=?", (emp_id,))
    records = cursor.fetchall()
    for row in records:
        return row[1]
    db.close()


# return grade by emp_id
def get_grade(emp_id):
    db = sqlite3.connect('/home/adarshsingh/PycharmProjects/oms/admin/oms.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employee WHERE emp_id=?", (emp_id,))
    records = cursor.fetchall()
    for row in records:
        return row[3]
    db.close()


# return join date of employee
def get_date(emp_id):
    db = sqlite3.connect('/home/adarshsingh/PycharmProjects/oms/admin/oms.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employee WHERE emp_id=?", (emp_id,))
    records = cursor.fetchall()
    for row in records:
        return row[4]
    db.close()


def get_salary_start(emp_id):
    grade = grade_conv(get_grade(emp_id))

    db = sqlite3.connect('/home/adarshsingh/PycharmProjects/oms/admin/oms.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM salary WHERE grade=?", (grade,))
    records = cursor.fetchall()
    for row in records:
        return row[1]
    db.close()


def get_salary_end(emp_id):
    grade = grade_conv(get_grade(emp_id))

    db = sqlite3.connect('/home/adarshsingh/PycharmProjects/oms/admin/oms.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM salary WHERE grade=?", (grade,))
    records = cursor.fetchall()
    for row in records:
        return row[2]
    db.close()


def date_time_get():
    from datetime import datetime
    now = datetime.now()  # current date and time
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    return date_time


def search():
    x=[]
    dbx = dropbox.Dropbox('eM8QnMm92mUAAAAAAAAAAd7WgRgIsLb2tDIoCi4k9dbhejOSuobCUEC8m3k_AiAz')
    result = dbx.files_list_folder("", recursive=True)
    file_list = []

    def process_entries(entries):
        for entry in entries:
            file_list.append([entry.name])

    process_entries(result.entries)
    while result.has_more:
        result = dbx.files_list_folder_continue(result.cursor)

        process_entries(result.entries)
    check = False

    for i in file_list:
        for y in i:
            x.append(y)

    return x


def available_files():
    root = tkinter.Tk()
    root.geometry("400x500")
    root.title("File Download")
    list= search()
    for i in range(len(list)):
        e = tkinter.Entry(root, width=50, fg='blue')
        e.grid(row=i, column=0)
        e.insert(tkinter.END, list[i])
    root.mainloop()

