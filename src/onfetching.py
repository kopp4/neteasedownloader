# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 21:27
# @Author  : taltalasuka
# @File    : onfetching.py
# @Software: PyCharm

import src

import re
import requests
from requests_html import HTMLSession
from lxml import etree

import base64,codecs
from Crypto.Cipher import AES

"""
functions related to requests
"""

HEADERS = {
    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

regex1 = r'''\"title\"\s?:\s?\"(.+)\"'''    # for getting username in user profile
# regex1 = r'<li><a href="/song\?id=\d+">(.+?)</a></li>'



class getNetease:
#     def __init__(self):
#        # todo



    def fetch_user(self, url):
        """

        :param url: url which is fetching pending
        :return:
        """

        r = requests.get(url = url, headers = HEADERS, timeout = 4)  # timeout
        contents = r.text
        user_name = re.search(regex1, contents).group(1)   # EXP + 1    also, findall -> default groups
        if not user_name:
            print("fetching username error")
            # LITERALLY SO GENIUS
        else:
            print(contents)
            return user_name


    def fetch_playlists(self, url):
        print("Fetching playlists : " + getNetease.fetch_user)


    def fetch_songs(self, url):
        # todo fori
        # todo print("Fetching songs in " + + )


        session = HTMLSession()
        response = session.get(url)  # url should be a profile url which fetches playlists recursively
        html = etree.HTML(response.content.decode())

        song_list = html.xpath("//ul[@class='f-hide']/li/a")
        '''  
        [
        "Repeat",
        "Moonlight",
        "Sick Of Being Told",
        "Burned",
        "Just A Crush",
        "So Much More Than This",
        "Escape My Mind",
        "Talk Good",
        "Florets",
        "Insane Sometimes"
        ]
        '''

        music_list = []
        for song in song_list:
            music_id = song.xpath('.//@href')
            music_name = song.xpath('.//text()')
            music_list.append({'id': music_id, 'name': music_name})
        return music_list
        # print(html)

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