import tkinter
from tkinter import filedialog
from admin import cloud


def file_get():
    main_win = tkinter.Tk()
    main_win.geometry("500x200")
    main_win.title("SELECT FILE")
    main_win.sourceFile = ''

    def chooseFile():
        main_win.sourceFile = filedialog.askopenfilename(parent=main_win, initialdir="/home",
                                                         title='Please select a directory')

    def bye():
        try:
            cloud.upload(main_win.sourceFile)
            response.config(text="done")
        except Exception as e:
            response.config(text=e)

    def end():
        exit(0)

    b_chooseFile = tkinter.Button(main_win, text="Choose File", width=20, height=3, command=chooseFile,font=('Helvetica', 11, 'bold'))
    close = tkinter.Button(text="UPLOAD", command=bye)
    b_chooseFile.place(x=150, y=50)
    b_chooseFile.width = 100
    close.place(x=200, y=120)
    close.width = 100
    response = tkinter.Label(text= "Select the file and wait for response ")
    response.place(x=120, y=160)
    x = tkinter.Button(text='X', command=end)
    x.place(x=0, y=0)

    def on_closing():
        main_win.destroy()

    main_win.protocol("WM_DELETE_WINDOW", on_closing)
    main_win.mainloop()
    cloud.upload(main_win.sourceFile)


if __name__ == "__main__":
    file_get()

