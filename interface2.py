from admin.project_manager import *
from admin.details import details
from admin.employee_manger import *
from admin import file
from employee.download_call import download_req
from admin.employee_manger import commit_get


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

    def download():
        root.destroy()
        download_req(0)

    def get_list():
        root.destroy()
        commit_get()


    root.geometry("1000x400")
    root.title("ADMIN HANDLE")
    # LABELS
    head = Label(root, text="Menu",  font=('Helvetica', 18, 'bold'))
    head.place(x=470,y=0)
    # BUTTON
    project = Button(root, text="Project list",width=20,height=2,bg='black',fg='white',font=('Helvetica', 11, 'bold'), command=proj_list)
    project.place(x=0,y=30)
    emp = Button(root, text="Employee Performance",width=20,height=2,bg='black',fg='white',font=('Helvetica', 11, 'bold'), command=emp_perform)
    emp.place(x=0,y=75)
    add = Button(root, text="Add Employee",width=20,height=2,bg='black',fg='white',font=('Helvetica', 11, 'bold'), command=emp_add)
    add.place(x=0,y=120)
    remove = Button(root, text="Remove  Employee",width=20,height=2,bg='black',fg='white',font=('Helvetica', 11, 'bold'), command=del_emp)
    remove.place(x=0,y=165)
    assign = Button(root, text="Add Project",width=20,height=2,bg='black',fg='white',font=('Helvetica', 11, 'bold'), command=proj_add)
    assign.place(x=0,y=210)
    emp_grade = Button(root, text="Employee Ranking",width=20,height=2,bg='black',fg='white',font=('Helvetica', 11, 'bold'), command=show_emp)
    emp_grade.place(x=0,y=255)
    search = Button(root, text="Search",width=20,height=2,bg='black',fg='white',font=('Helvetica', 11, 'bold'), command=serch)
    search.place(x=0, y=300)

    def upload_i():
        root.destroy()
        file.file_get(0)

    cloud_b = Button(root, text="Upload",width=20,height=2,bg='black',fg='white',font=('Helvetica', 11, 'bold'), command=upload_i)
    cloud_b.place(x=0, y=345)
    close = Button(root, text="x",font=('Helvetica', 11, 'bold'), command=out)
    close.place(x=0, y=0)
    download_b = Button(root, text="Upload",width=20,height=2,bg='black',fg='white',font=('Helvetica', 11, 'bold'), command=download)
    download_b.place(x=810, y=30)
    commit=Button(root, text="STATUS",width=20,height=2,bg='black',fg='white',font=('Helvetica', 11, 'bold'), command=get_list)
    commit.place(x=810,y=75)

    root.mainloop()


def out():
    exit(0)


if __name__ == "__main__":
    interface2()
