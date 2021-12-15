# -*- coding: utf-8 -*-
# @Time    : 2021/11/30 23:48
# @Author  : taltalasuka
# @File    : 1111.py
# @Software: PyCharm
import requests

HEADERS = {
    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

# url = 'https://spclient.wg.spotify.com/user-profile-view/v3/profile/31jpixs7tmbzy4x6b3g6qefuonxy?playlist_limit=10&artist_limit=10&market=HK'
url = "https://open.spotify.com/user/31jpixs7tmbzy4x6b3g6qefuonxy"

http_proxy = "http://127.0.0.1:7890"        # todo can't find a better way but now let's just use it
https_proxy = "http://127.0.0.1:7890"

proxyDict = {
    "http": http_proxy,
    "https": https_proxy
}

payload = {
    "username":"vivi",
    "password":"123456"
}
# login_res = requests.post(url, proxies = proxyDict)
login_res = requests.get(url, proxies = proxyDict, headers = HEADERS)

# login_res = requests.post(url,json=payload, proxies = proxyDict)

print(login_res.text)

# 从响应结果中获取token值
# token = login_res.json()["token"]
# print("token:", token)