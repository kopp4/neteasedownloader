# -*- coding: utf-8 -*-
# @Time    : 2021/11/30 10:31
# @Author  : taltalasuka
# @File    : test.py
# @Software: PyCharm

import unittest
import re
import requests
import base64, codecs
from Crypto.Cipher import AES


HEADERS = {
    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}


    def get_params(self,id):
        encText=str({'ids': "[" + str(id) + "]", 'br': 128000, 'csrf_token': ""})
        return AES_encrypt(AES_encrypt(encText,self.g, self.iv), self.i, self.iv)

    def get_encSecKey(self):
        return RSA_encrypt(self.i, self.b, self.c)






class decode():

    def to_16(key):
        while len(key) % 16 != 0:
            key += '\0'
        return str.encode(key)
    def AES_encrypt(text, key, iv):
        bs = AES.block_size
        pad2 = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
        encryptor = AES.new(to_16(key), AES.MODE_CBC, to_16(iv))
        encrypt_aes = encryptor.encrypt(str.encode(pad2(text)))
        encrypt_text = str(base64.encodebytes(encrypt_aes), encoding = 'utf-8')
        return encrypt_text

    def RSA_encrypt(text, pubKey, modulus):
        text = text[::-1]
        rs = int(codecs.encode(text.encode('utf-8'), 'hex_codec'), 16) ** int(pubKey, 16) % int(modulus, 16)
        return format(rs, 'x').zfill(256)























# class test(unittest.TestCase):
#     def test_fetch_playlists(self):
#         url = "https://music.163.com/#/user/home?id=350278537"
#         print("If u are stuck then I am fucked up")
#         r = requests.get(url, headers=HEADERS)
#         contents = r.text
#         playlists_name = re.search()
#         print(contents)
#         requests.session()
#     def test_fetch_playlists2(self):
#         url = "https://music.163.com/#/playlist?id=492053870"
#         _id = re.search(r'id=(\d+)', url).group(1)
#         url = "http://music.163.com/playlist?id={0}".format(_id)
#         r = requests.get(url, headers=HEADERS)
#         contents = r.text
#         song_list_name = re.search(r"<title>(.+)</title>", contents).group(1)[:-13]
#
#         print("歌单: " + song_list_name + "\n")
#         pattern = r'<li><a href="/song\?id=\d+">(.+?)</a></li>'
#         song_list = re.findall(pattern, contents)
#
#
# if __name__ == '__main__':
#     print("In main")