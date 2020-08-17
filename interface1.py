from interface2 import *


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
            response.config(text="access denied!!!")

    root.title("OMS GOD ACCESS")
    root.geometry("250x150")
    root.bind('<Return>',ok)

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
