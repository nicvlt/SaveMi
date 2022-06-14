import os
from functions import *
from tkinter import *
from tkinter import ttk
import sys

root = Tk()
root.title('SaveMi')
root.resizable(False, False)
root.geometry('250x160')
root.eval('tk::PlaceWindow . center')
style = ttk.Style(root)
style.theme_use("clam")


def OnClick():
    id_var_info = id_var.get()
    mdp_info = mdp_var.get()
    boolean = login_add_file(id_var_info, mdp_info)
    id_entry.delete(0, END)
    mdp_entry.delete(0, END)

    if(boolean):
        root.destroy()
        # insert at 1, 0 is the script path (or '' in REPL)
        sys.path.insert(1, 'C:/Users/nicol/Documents/pythonProject/SaveMi')
        import main


id_var = StringVar()
mdp_var = StringVar()

id_text = Label(text="Login")
id_text.place(x=105, y=8)
id_entry = Entry(textvariable=id_var)
id_entry.place(x=65, y=30)

mdp_text = Label(text="Password")
mdp_text.place(x=100, y=58)
mdp_entry = Entry(textvariable=mdp_var, show="*")
mdp_entry.grid(column=1, row=1, padx=10)
mdp_entry.place(x=65, y=80)

ttk.Button(text="Log in", command=OnClick).place(x=89, y=115)

root.mainloop()
