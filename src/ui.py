# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 21:23
# @Author  : taltalasuka
# @File    : Ui.py
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


class Ui:

    def __init__(self):

        # super().__init__(master)

        ''''''
        self.window0 = tkinter.Tk()
        self.window0.geometry("600x300")
        self.window0.title("taltalasuka")
        self.window0.config(bg = "#5f6467")
        # self.window0.
        # self.window0.



        self.txt = tkinter.StringVar()
        self.txt.set("Enter here...")


        # compound = "left"

        self.LABEL0 = tkinter.Label(self.window0, text = "Input your url : ", fg = "#bbbbbb", bg = "#3c3f41", bd = 10, compound = "bottom")
        self.LABEL0.pack()
        # self.LABEL0.place(x=0, y=50)
        self.LABEL1 = tkinter.Label(self.window0, text = "format : https://music.163.com/#/user/home?id=350278537", bg = "#3c3f41", fg = "#bbbbbb")
        self.LABEL1.pack(side = "bottom", fill = "both")
        self.ENTRY0 = tkinter.Entry(self.window0, font = ("Arial", 20), textvariable = self.txt, bg = "#2b2b2b", fg = "#bbbbbb")
        self.ENTRY0.pack(side = "left")
        # self.ENTRY0.place(x=80, y=50)

        self.BUTTON0 = tkinter.Button(self.window0, text = "submit", command = self.functions, compound = "left")   # todo CRITICAL!!!
        # self.BUTTON0.place(x=100, y=100)
        # self.btnquit
        BUTTONTEST = tkinter.Button(self.window0, text = "fetch demo rank", command = self.test_myrank, compound = "right")
        self.BUTTON0.pack(side = "left", expand = True)
        BUTTONTEST.pack(side = "left", expand = True)


        ''''''

        self.window0.mainloop()

    def functions(self):
        """
        Match and get the userid from input and then jump to
        the next window, make the user to decide whether to go forward
        :return:
        """
        while True:
            try:
                self.uid = re.search(regex, self.ENTRY0.get()).group(1)
                if self.uid != None:
                    break
            except AttributeError as e:

                print(e)
                print("THE FORMAT !!!")
                      #fixme
                self.uid = None
                self.ENTRY0.destroy()
                self.ENTRY0 = tkinter.Entry(self.window0, font = ("Arial", 20), textvariable = self.txt, bg = "#2b2b2b", fg = "#bbbbbb")
                self.ENTRY0.pack(side = "right")  # FIXME BRO



        if self.uid:  # Judging else print THE FORMAT!!

            self.profile_url = url.format(self.uid)

            self.fetch = src.onfetching.getNetease(self.profile_url)                # --> CALLING THE **CONSTRUCTOR** HERE <--


            """"""
            self.window0.destroy()  # from the original lib:'''Destroy this and all descendants widgets, end the application of this Tcl interpreter."'''

            self.LABEL0 = tkinter.Label(self.window0, text = "Hello, ")

            self.BUTTON0 = tkinter.Button(self.window0, text = "To download all the songs", command = self.getsongs)  # Yes, I use them repeatedly
            self.BUTTON0.pack()

            self.BUTTON1 = tkinter.Button(self.window0, text = "To show the rank graph", command = self.test_myrank())
            self.BUTTON0.pack()
            """"""


            # self.id = re.search(regex0, self.ENTRY0.get()).group(1)
            # .format(self.id)  # idkw default source have a #
            # MINDBLOWING
        else:
            print("THE FORMAT !!!")

    def getsongs(self):
        """
        Download songs from onfetching.py
        """
        self.fetch.fetch_playlists(self.uid)



    def getrank(self):
        """
        Calling the get rank function from onfetching.py
        """
        self.fetch.fetch_rank(self.uid)

    def notify(self):

        print("COMPLETE!!")

    def test_myrank(self):
        print("ID : 350278537")
        fetch = src.onfetching.getNetease(url.format("350278537"))

        fetch.fetch_rank("350278537")


    def delete(self):
        pass
