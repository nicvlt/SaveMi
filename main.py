import os
from turtle import bgcolor
from functions import *
from tkinter import *
from tkinter import ttk


def refresh_treeview():
    data_list = file_to_table()
    for data in data_list:
        temp_data = data.split("'")
        tv.insert("", 'end', values=(temp_data[0], temp_data[1]))


def delete_all_treeview(tv):
    for row in tv.get_children():
        tv.delete(row)


def OnClick():
    id_var_info = id_var.get()
    mdp_info = mdp_var.get()
    add_to_file(id_var_info, mdp_info)
    id_entry.delete(0, END)
    mdp_entry.delete(0, END)

    delete_all_treeview(tv)
    refresh_treeview()


def delete_selected():
    data_to_delete = str(tv.item(tv.focus()).get('values')[0])
    delete_in_file(data_to_delete)
    tv.delete(tv.selection()[0])


root = Tk()
root.title('SaveMi')
root.resizable(False, False)
root.geometry('450x260')
root.eval('tk::PlaceWindow . center')
style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview.Heading", background="light-grey")


#Table & Data
tv = ttk.Treeview(columns=(1, 2), show="headings", height="5")
tv.place(x=25, y=72)
tv.heading(1, text='ID')
tv.heading(2, text='Passwords')
ttk.Button(text="Delete", command=delete_selected).place(x=190, y=215)
refresh_treeview()


#Entries & Button
id_var = StringVar()
mdp_var = StringVar()

id_text = Label(text="Identification")
id_text.place(x=45, y=5)
id_entry = Entry(textvariable=id_var)
id_entry.place(x=45, y=30)

mdp_text = Label(text="Password")
mdp_text.place(x=185, y=5)
mdp_entry = Entry(textvariable=mdp_var)
mdp_entry.grid(column=1, row=1, padx=10)
mdp_entry.place(x=185, y=30)

ttk.Button(text="Add", command=OnClick).place(x=325, y=24)


root.mainloop()
