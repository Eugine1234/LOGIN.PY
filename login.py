from tkinter import*
from tkinter import messagebox


def login():
    username=entry1.get()
    password='entry2'.get()

    if (username=="" and password==""):
        messagebox.showinfo("Blank Not Allowed")

    elif (username=="Eugine12" and password=="@hitman12"):
        messagebox.showinfo("",'login successful')

    else:
        messagebox.showinfo("","incorrect username and password")

root=Tk()
root.configure(bg="cyan4")
root.title("login")
root.geometry("300*200")


global entry1
global enrty2


Label(root,text="Username"). place(p=20,y=20)
Label(root,text="password").place(p=20,y=70)


entry1=Entry(root,bd=5)
entry1.place(p=140,y=70)
Button(root,text="Login",command='Login',height=3,width=13,bd=6).place(p=100,y=120)

root.mainloop()