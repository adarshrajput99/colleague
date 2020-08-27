import sqlite3


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