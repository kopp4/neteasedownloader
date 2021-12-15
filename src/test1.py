# -*- coding: utf-8 -*-
# @Time    : 2021/11/30 13:09
# @Author  : taltalasuka
# @File    : test1.py
# @Software: PyCharm

import re
import requests
import shutil
from bs4 import BeautifulSoup


HEADERS = {

    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

if __name__ == '__main__':
    url = "https://music.163.com/weapi/user/playlist?csrf_token="

    playlists = []
    offset = 0



    re = requests.session().post(url, headers = HEADERS)
    re = requests.get()

    file = "get.txt"

    print(re.text)

    f = open(file, "w", errors = "ignore")
    f.write(re.text)
    f.close()
