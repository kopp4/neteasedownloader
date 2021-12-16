# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 21:23
# @Author  : taltalasuka
# @File    : ui.py
# @Software: PyCharm

import tkinter
import re

import src.onfetching

'''
GUI for my menu
'''

"""regex for filtering the format"""
regex = r".+id=(\d+)"

"""regex for matching self.id"""
regex0 = r"id\s?=\s?(\d+)"

"""Default url format that we are fetching"""
url = "https://music.163.com/user/home?id={0}"


class ui:
    window = tkinter.Tk()

    def __init__(self):

        ''''''
        self.LABEL1 = tkinter.Label(self.window, text = "Input your url : ")
        # self.LABEL1.place(x=0, y=50)
        self.LABEL1.pack()
        self.LABEL2 = tkinter.Label(self.window, text = "format : https://music.163.com/#/user/home?id=350278537")
        self.LABEL2.pack()
        self.ENTRY1 = tkinter.Entry(self.window, font = ("Arial", 10))
        # self.ENTRY1.place(x=80, y=50)
        self.ENTRY1.pack()
        self.BUTTON = tkinter.Button(self.window, text = "submit", command = self.geturl)   # todo CRITICAL!!!
        # self.BUTTON.place(x=100, y=100)
        self.BUTTON.pack()
        ''''''

        self.window.mainloop()

    def geturl(self):
        """
        Match and get the userid from input and then jump to
        the next window
        :return:
        """

        self.uid = re.search(regex, self.ENTRY1.get()).group(1)

        self.profile_url = url.format(self.uid)

        if self.uid:        # Judging else print THE FORMAT!!

            src.onfetching.getNetease(self.profile_url, self.uid)     # --> CALLING THE **CONSTRUCTOR** HERE <--

            # self.id = re.search(regex0, self.ENTRY1.get()).group(1)
            # .format(self.id)  # idkw default source have a #
            # MINDBLOWING

            # self.playlists_name = fetch.fetch_playlists(self.id)  # Playlists in the profile show here

            # Print all the playlists in the profile

            self.window.destroy()  # from the original lib:'''Destroy this and all descendants widgets, end the application of this Tcl interpreter."'''
            self.window = tkinter.Tk()

        else:

            print("THE FORMAT !!!")

    def notify(self):

        print("COMPLETE!!")

    # def delete(self):
