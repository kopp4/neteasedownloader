# -*- coding: utf-8 -*-
# @Time    : 2021/11/30 20:53
# @Author  : taltalasuka
# @File    : test2.py
# @Software: PyCharm

import requests
import re
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

IP = "hk05-vm5.entry.ikuuu.casa:11200"

proxies = {
    "https:": "http://" + IP,
    "http" : "http://" + IP,
}

"""        http://icanhazip.com/        """

url = "http://icanhazip.com/"
def on_fetching():
   try:
        re = requests.get(url, headers = HEADERS, proxies = proxies)

        print(re.text)
   except requests.exceptions.ConnectionError as e:     #todo CURSE YOU!!!
        print('Error', e.args)

def get_ip_pool():
    file = "ip.txt"
    regex = r"server:\s?(.+),\s?port:\s?(\d+)"
    with open(file, "r", encoding = "utf-8") as f:
        contents = f.read()
        ips = re.findall(regex, contents)

        for i, x in ips:
            print('''"http:" : "http://{0}:{1}"'''.format(i, x), end = ",\n")
            print('''"https:" : "http://{0}:{1}"'''.format(i, x), end = ",\n")

def validate(proxies):
    https_url = 'https://ip.cn'
    http_url = 'http://ip111.cn/'
    headers = {'User-Agent': 'curl/7.29.0'}
    https_r = requests.get(https_url, headers=headers, proxies=proxies, timeout=10)
    http_r = requests.get(http_url, headers=headers, proxies=proxies, timeout=10)
    soup = BeautifulSoup(http_r.content, 'html.parser')
    # result = soup.find(class_='card-body').get_text().strip().split('''\n''')[0]

    print(f"当前使用代理：{proxies.values()}")
    print(f"访问https网站使用代理：{https_r.json()}")
    # print(f"访问http网站使用代理：{result}")

if __name__ == '__main__':
    # get_ip_pool()
    print(proxies)
    validate(proxies)
    # on_fetching()