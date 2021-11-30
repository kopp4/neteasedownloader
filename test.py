# -*- coding: utf-8 -*-
# @Time    : 2021/11/30 10:31
# @Author  : taltalasuka
# @File    : test.py
# @Software: PyCharm

import unittest
import re
import requests

HEADERS = {
    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}


class test(unittest.TestCase):
    def test_fetch_playlists(self):
        url = "https://music.163.com/#/user/home?id=350278537"
        print("If u are stuck then I am fucked up")
        r = requests.get(url, headers=HEADERS)
        contents = r.text
        playlists_name = re.search()
        print(contents)
        requests.session()
    def test_fetch_playlists2(self):
        url = "https://music.163.com/#/playlist?id=492053870"
        _id = re.search(r'id=(\d+)', url).group(1)
        url = "http://music.163.com/playlist?id={0}".format(_id)
        r = requests.get(url, headers=HEADERS)
        contents = r.text
        song_list_name = re.search(r"<title>(.+)</title>", contents).group(1)[:-13]

        print("歌单: " + song_list_name + "\n")
        pattern = r'<li><a href="/song\?id=\d+">(.+?)</a></li>'
        song_list = re.findall(pattern, contents)


if __name__ == '__main__':
    print("In main")