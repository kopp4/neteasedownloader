# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 21:22
# @Author  : taltalasuka
# @File    : store.py
# @Software: PyCharm


import pymysql

class store:

    '''

    ----------
    User
    UUID
    Playlists
    PUID        --p
    ----------
    Playlists
    PUID        --p
    Song
    SUID
    ----------

    '''

    sqlp = "select * from playlists"  # sql for playlists()

    sqls = "select * from songs"  # sql for songs()
    # def __init__(self):


    def playlists(self, data):

        db = pymysql.connect(
            host="localhost",
            user="root",
            password="123456",
            database="netease", )
        cur = db.cursor()

        try:
            cur.execute(self.sqlp)

            data = cur.fetchall()

            print(data)

            db.commit()
        except:
            print("Error : unable to fetch data")

            db.rollback()
        finally:
            db.close()


    def songs(self, data):

        db = pymysql.connect(
            host="localhost",
            user="root",
            password="123456",
            database="netease", )

        cur = db.cursor()

        try:
            cur.execute(self.sqls)

            data = cur.fetchall()

            print(data)

            db.commit()
        except:
            print("Error : unable to fetch data")

            db.rollback()
        finally:
            db.close()