# -*- coding: utf-8 -*-
# @Time    : 2021/12/16 1:26
# @Author  : taltalasuka
# @File    : encode.py
# @Software: PyCharm

import urllib.request,os,json
from lxml import etree
from requests_html import HTMLSession
import re

import execjs,requests

import base64,codecs
from Crypto.Cipher import AES

# todo wtf is this
def to_16(key):
    while len(key) % 16 != 0:
        key += '\0'
    return str.encode(key)



class encode:
# In window.asrsea :
# wtf the very first song id in my profile literally appear out of NOWHERE!!!
# Fortunately user id appear at last   <3<3<3

    def __init__(self):
        self.i = self.func_a("16")                                                          # i is supposed to be unified


    def func_a(self, a):
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


    def func_b(self, a, b):

        blockSize = AES.block_size
        pad2 = lambda s: s + (blockSize - len(s) % blockSize) * chr(blockSize - len(s) % blockSize)
        d = AES.new(to_16(b), AES.MODE_CBC, to_16("0102030405060708"))  # encryptor
        encrypt_aes = d.encrypt(str.encode(pad2(a)))
        encrypt_text = str(base64.encodebytes(encrypt_aes), encoding = 'utf-8')
        return encrypt_text

    def func_c(self, a, b, c):        # todo change
        a = a[::-1]
        rs = int(codecs.encode(a.encode('utf-8'), 'hex_codec'), 16) ** int(b, 16) % int(c, 16)
        return format(rs, 'x').zfill(256)






    # UID : User ID



