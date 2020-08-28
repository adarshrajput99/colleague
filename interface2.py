from admin.project_manager import *
from admin.details import details
from admin.employee_manger import *
from admin import file


def interface2():
    root = Tk()

    def emp_add():
        add_emp()

    def del_emp():
        root.destroy()
        delete_emp()

    def emp_perform():
        emp_p()

    def proj_add():
        root.destroy()
        add_proj()


    def serch():
        details()

    root.geometry("200x300")
    root.minsize(200, 300)
    root.maxsize(200, 300)
    root.title("emp info")
    # LABELS
    head = Label(root, text="Menu", font="bold")
    head.pack(anchor="center")
    # BUTTON
    project = Button(root, text="            Project list              ", command=proj_list)
    project.pack(anchor="w")
    emp = Button(root, text="  Employee Performance   ", command=emp_perform)
    emp.pack(anchor="w")
    add = Button(root, text="           Add Employee\t ", command=emp_add)
    add.pack(anchor="w")
    remove = Button(root, text="      Remove  Employee      ", command=del_emp)
    remove.pack(anchor="w")
    assign = Button(root, text="               Add Project  \t", command=proj_add)
    assign.pack(anchor="w")
    emp_grade = Button(root, text="       Employee Ranking\t", anchor="w", command=show_emp)
    emp_grade.pack()
    search = Button(root, text="                SEARCH       \t", anchor="w", command=serch)
    search.pack()

    def upload_i():
        root.destroy()
        file.file_get()

    cloud_b = Button(root, text="\t  UPLOAD\t\t", command=upload_i)
    cloud_b.pack()
    close = Button(root, text="close", command=out)
    close.pack()
    root.mainloop()


def out():
    exit(0)


if __name__ == "__main__":
    interface2()
