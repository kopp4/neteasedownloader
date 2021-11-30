# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 21:27
# @Author  : taltalasuka
# @File    : onfetching.py
# @Software: PyCharm

import src

import re
import requests

"""
functions related to requests
"""

HEADERS = {
    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

proxies = {
"http:" : "http://jp01-vm5.entry.ikuuu.casa:448",
"https:" : "http://jp01-vm5.entry.ikuuu.casa:448",
}

regex1 = r'''\"title\"\s?:\s?\"(.+)\"'''    # for getting username in user profile
# regex1 = r'<li><a href="/song\?id=\d+">(.+?)</a></li>'



class getNetease:
#     def __init__(self):
#        # todo
#
#
    def fetch_user(self, url):
        r = requests.get(url, headers = HEADERS, timeout = 4, proxies = proxies)   # timeout
        contents = r.text
        user_name = re.search(regex1, contents).group(1)   # EXP + 1    also, findall -> default groups
        if not user_name:
            print("fetching username error")
            # LITERALLY SO GENIUS
        else:
            print("Hello, " + user_name)

    def fetch_playlists(self):
        print("Fetching playlists : ")


        # print(contents)

# def validate(self, url):      # done


#     def get_SUID(self):
#
#     def get_PUID(self):
#
#     # def download(self):
#
#     '''Storing playlists & Songs from specified UID'''
#
#     def store_P(self):
#         store.playlists()
#     def store_S(self):
#         store.songs()
#         print("this is cursed")

# print(dir(requests.get("https://music.163.com/#/user/home?id=350278537")))