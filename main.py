import os
from tkinter import *
from tkinter import ttk


def bad_crypt(string: str):
    result = ""
    for char in range(0, len(string)):
        result += (chr(ord(string[char])+5))
    return result


def uncrypt(string: str):
    result = ""
    for char in range(0, len(string)):
        result += (chr(ord(string[char])-5))
    return result


def add_to_file(id: str, mdp: str):
    # apen file
    try:
        store_file = open('data.txt', 'x')
        store_file = open('data.txt', 'r')
    except FileExistsError:
        store_file = open('data.txt', 'r')

    # check if already in file
    word_search = id + ',' + mdp
    if (word_search in store_file.read()):
        print('Already exists')
    else:
        store_file = open('data.txt', 'a')
        store_file.write(bad_crypt(id) + ',' + bad_crypt(mdp) + "\n")

    store_file.close()


def file_to_table():
    try:
        file = open('data.txt', 'x')
        file = open('data.txt', 'r')
    except FileExistsError:
        file = open('data.txt', 'r')
    lines = file.readlines()
    list = []
    for line in lines:
        list.append(uncrypt(line.strip()))
    return list


def search_string_in_file(file_name, string_to_search):
    line_number = 0
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            line_number += 1
            if string_to_search in line:
                return line_number
        return -1


def delete_in_file(string: str):
    string = bad_crypt(string)

    # get all lines
    try:
        a_file = open('data.txt', 'x')
        a_file = open('data.txt', 'r')
    except FileExistsError:
        a_file = open('data.txt', 'r')
    lines = a_file.readlines()
    a_file.close()

    # delete useless data
    if search_string_in_file('data.txt', string) != -1:
        del lines[search_string_in_file('data.txt', string) - 1]

    # create new file without useless data
    new_file = open("data.txt", "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()


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
id_text.place(x=25, y=5)
id_entry = Entry(textvariable=id_var)
id_entry.place(x=25, y=30)

mdp_text = Label(text="Password")
mdp_text.place(x=190, y=5)
mdp_entry = Entry(textvariable=mdp_var)
mdp_entry.grid(column=1, row=1, padx=10)
mdp_entry.place(x=190, y=30)

ttk.Button(text="Add", command=OnClick).place(x=350, y=27)


root.mainloop()
