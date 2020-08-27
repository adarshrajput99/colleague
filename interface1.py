from admin.interface2 import *
from employee import users_start
from admin import project_manager
from employee import emp_func_batch
call_id = 0


def login():
    root = Tk()

# OK FUNCTION DEFINITION WHICH IS USED IN LAYOUT
    def ok(event=None):
        if user_val.get() == "asr":
            if pass_val.get() == "asr":
                response.config(text="access granted")
                root.destroy()
                interface2()
            else:
                response.config(text="access denied!!!")
        else:
            if project_manager.search(int(user_val.get())):
                call_id = int(user_val.get())
                if pass_val.get() == emp_func_batch.get_date(call_id):
                    root.destroy()
                    users_start.usr_start(call_id)
            else:
                response.config(text="access denied!!!")

    root.title("SIGN IN")
    root.geometry("250x150")
    root.bind('<Return>', ok)

    # LABELS
    user = Label(root, text="user    ")
    password = Label(root, text="password")

    response = Label(root, text="* denotes mandatory")
    response.grid(row=3, column=1)
    user.grid(row=0, column=0)
    password.grid(row=1, column=0)
    user_val = StringVar()
    pass_val = StringVar()

    #   TEXT FIELD
    user_e = Entry(root, textvariable=user_val)
    password_e = Entry(root, textvariable=pass_val)
    user_e.grid(row=0, column=1)
    password_e.grid(row=1, column=1)

    # BUTTON
    b1 = Button(root, text="ok", command=ok)
    b1.grid(row=2, column=1)

    root.mainloop()


if __name__ == "__main__":
    login()
