import hashlib
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter


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
        store_file = open(
            'C:/Users/nicol/Documents/pythonProject/SaveMi/data.txt', 'x')
        store_file = open(
            'C:/Users/nicol/Documents/pythonProject/SaveMi/data.txt', 'r')
    except FileExistsError:
        store_file = open(
            'C:/Users/nicol/Documents/pythonProject/SaveMi/data.txt', 'r')

    # check if already in file
    word_search = bad_crypt(id) + ',' + bad_crypt(mdp)
    if (word_search in store_file.read()):
        tkinter.messagebox.showerror(
            title='SaveMi', message='The password & ID are already saved in')

    else:
        store_file = open(
            'C:/Users/nicol/Documents/pythonProject/SaveMi/data.txt', 'a')
        store_file.write(bad_crypt(id) + ',' + bad_crypt(mdp) + "\n")

    store_file.close()


def file_to_table():
    try:
        file = open(
            'C:/Users/nicol/Documents/pythonProject/SaveMi/data.txt', 'x')
        file = open(
            'C:/Users/nicol/Documents/pythonProject/SaveMi/data.txt', 'r')
    except FileExistsError:
        file = open(
            'C:/Users/nicol/Documents/pythonProject/SaveMi/data.txt', 'r')
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
        a_file = open(
            'C:/Users/nicol/Documents/pythonProject/SaveMi/data.txt', 'x')
        a_file = open(
            'C:/Users/nicol/Documents/pythonProject/SaveMi/data.txt', 'r')
    except FileExistsError:
        a_file = open(
            'C:/Users/nicol/Documents/pythonProject/SaveMi/data.txt', 'r')
    lines = a_file.readlines()
    a_file.close()

    # delete useless data
    if search_string_in_file('C:/Users/nicol/Documents/pythonProject/SaveMi/data.txt', string) != -1:
        del lines[search_string_in_file(
            'C:/Users/nicol/Documents/pythonProject/SaveMi/data.txt', string) - 1]

    # create new file without useless data
    new_file = open(
        "C:/Users/nicol/Documents/pythonProject/SaveMi/data.txt", "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()


def encode_sha256(string: str):
    string = string.encode()
    string_hash = hashlib.sha256(string)
    return string_hash.hexdigest()


def login_add_file(id: str, mdp: str):
    # hash everything
    hash_id = encode_sha256(id)
    hash_mdp = encode_sha256(mdp)

    # apen file
    try:
        store_file = open(
            'C:/Users/nicol/Documents/pythonProject/SaveMi/login.txt', 'x')
        store_file = open(
            'C:/Users/nicol/Documents/pythonProject/SaveMi/login.txt', 'r')
    except FileExistsError:
        store_file = open(
            'C:/Users/nicol/Documents/pythonProject/SaveMi/login.txt', 'r')

    # check if already in file
    word_search = hash_id + ',' + hash_mdp
    if (word_search in store_file.read()):
        tkinter.messagebox.showinfo(
            title='Login', message='Logged in successfully')
        store_file.close()

        return True
    else:
        tkinter.messagebox.showerror(
            title='Login', message='Wrong combination')
        store_file.close()

        return False
