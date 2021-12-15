# -*- coding: utf-8 -*-
# @Time    : 2021/12/16 1:26
# @Author  : taltalasuka
# @File    : encode.py
# @Software: PyCharm

import urllib.request,os,json
from lxml import etree
from requests_html import HTMLSession

import execjs,requests

import base64,codecs
from Crypto.Cipher import AES

HEADERS = {
    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

def func_a(a):
    # Decode of function a(a)
    js = execjs.compile(

        r"""
        function a(a) {
            var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
            for (d = 0; a > d; d += 1)
                e = Math.random() * b.length,
                e = Math.floor(e),
                c += b.charAt(e);
            return c
        }
        """

    )
    return js.call("a", a)


def func_b(a, b):

    blockSize = AES.block_size
    pad2 = lambda s: s + (blockSize - len(s) % blockSize) * chr(blockSize - len(s) % blockSize)
    d = AES.new(to_16(b), AES.MODE_CBC, to_16("0102030405060708"))  # encryptor
    encrypt_aes = d.encrypt(str.encode(pad2(a)))
    encrypt_text = str(base64.encodebytes(encrypt_aes), encoding = 'utf-8')
    return encrypt_text

def func_c(a, b, c):        # todo change
    a = a[::-1]
    rs = int(codecs.encode(a.encode('utf-8'), 'hex_codec'), 16) ** int(b, 16) % int(c, 16)
    return format(rs, 'x').zfill(256)

# todo wtf is this
def to_16(key):
    while len(key) % 16 != 0:
        key += '\0'
    return str.encode(key)


class encode:
# In window.asrsea :
# wtf the very first song id in my profile literally appear out of NOWHERE!!!
# Fortunately user id appear at last   <3<3<3


    i = func_a(16)


    # UID : User ID
    def get_params(self):      # todo this is function d(d, e, f, g) UID

        b = "0CoJUm6Qyw8W8jud"

        """
        function b(a, b)        "in another word, window.asrsea"
        a = "{\"uid\":\"350278537\",\"type\":\"-1\",\"limit\":\"1000\",\"offset\":\"0\",\"total\":\"true\",\"csrf_token\":\"\"}",
        b = "0CoJUm6Qyw8W8jud"
        """
        # a : encoded params
        a = """{\"uid\":\"350278537\",\"type\":\"-1\",\"limit\":\"1000\",\"offset\":\"0\",\"total\":\"true\",\"csrf_token\":\"\"}"""
        # a = """{\"userId\":\"350278537\",\"csrf_token\":\"\"}"""


        # a = str({'ids': "[" + str(549321040) + "]", 'br': 128000, 'csrf_token': ""})

        # todo modify uid here
        # Quotation mark sucks, so I'll just use str()
        # Edit : str() sucks

        # todo param2 I suppose

        return func_b(func_b(a, b), self.i)



    def get_encSecKey(self):
        # todo SecKey

        b = "010001"

        c = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"

        return func_c(self.i, b, c)

    def on_fetching(self):
        formdata = {
            "params" : self.get_params(),    # todo url
            "encSecKey" : self.get_encSecKey()
        }
        profile_url = "https://music.163.com/user/home?id=350278537"
        playlists_url = "https://music.163.com/weapi/user/playlist?csrf_token="
        song_url = "https://music.163.com/weapi/song/enhance/player/url?csrf_token="

        response = requests.post(playlists_url, headers = HEADERS, data = formdata)
        # print(response.content)
        print(response.text)

if __name__ == '__main__':
    encode = encode()
    encode.on_fetching()


