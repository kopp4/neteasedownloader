# -*- coding: utf-8 -*-
# @Time    : 12/16/2021 10:39 PM
# @Author  : taltalasuka
# @File    : test.py
# @Software: PyCharm
from tkinter import *

root = Tk()
root.geometry("300x300")
s = StringVar()
a = Entry(root,textvariable=s)
a.pack()
i = 0
s.set(i)

def refresh_data():
    global i
    a.delete(0, END)
    s.set(i)
    i = i + 1
    a.update()
    root.after(1000, refresh_data)

root.after(1000, refresh_data)
mainloop()
