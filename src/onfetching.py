# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 21:27
# @Author  : taltalasuka
# @File    : onfetching.py
# @Software: PyCharm
import os
import re
import urllib.request

import requests
import json
from requests_html import HTMLSession
from lxml import etree

import base64, codecs
from Crypto.Cipher import AES

import src as s

# import src.encode     encode = src.encode.encode()
"""
functions related to requests
"""

HEADERS = {
    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

regex1 = r'''\"title\"\s?:\s?\"(.+)\"'''  # for getting username in user profile

# regex1 = r'<li><a href="/song\?id=\d+">(.+?)</a></li>'

regex = r"\"name\"\s?:\s?\"(.+?)\""  # Regex for filtering the playlists name in the profile

regex2 =  r"\"id\"\s?\s?\:(\d+)"  # Regex for obtain all the playlists id

playlists_post_url = "https://music.163.com/weapi/user/playlist?csrf_token="

song_post_url = "https://music.163.com/weapi/song/enhance/player/url?csrf_token="

class getNetease:

    """Path of the main folder"""
    path = "e:/Music/"

    def __init__(self, profile_url, uid):

        self.user_name = self.fetch_user(profile_url)

        print("Greetings, " + self.user_name)

        # CORE
        # CORE
        # CORE
        self.fetch_playlists(uid)       # Recursively obtain all the songs in all the playlists
        # CORE
        # CORE
        # CORE
        # CORE

    def fetch_user(self, url):
        """
        Fetch the user name according to the url given
        :param url:
        :return:
        """

        r = requests.get(url = url, headers = HEADERS, timeout = 4)  # timeout
        contents = r.text
        user_name = re.search(regex1, contents).group(1)  # EXP + 1    also, findall -> default groups
        if not user_name:
            print("fetching username error")
            # LITERALLY SO GENIUS
        else:
            return user_name

    def fetch_playlists(self, uid):
        print("Fetching playlists : " + "")

        formdata = {
            "params": self.get_params_profile(uid),
            "encSecKey": self.get_encSecKey()
        }

        response = requests.post(playlists_post_url, headers = HEADERS, data = formdata)

        content = str(response.content, encoding = "utf-8")  # Or else \x9f\xe5\xa3\xb0 blah blah

        print(re.findall(regex, content))      # Printing all playlists name in the profile

        playlists_name = re.findall(regex, content)

        playlists_id = (re.findall(regex2, content))   # Obtain all playlists id in the profile

        del playlists_id[0]     # 《登录后才可以查看》

        del playlists_name[0]

        while playlists_name:
            for i in playlists_id:

                playlists_url = "https://music.163.com/playlist?id=" + i

                self.songs = self.fetch_songs(playlists_url, playlists_name[0])

                print(playlists_name[0])

                print(self.songs)

                playlists_name.pop(0)




        # i : PID
        # playlist : Name of the playlist
        # for i, playlist in playlists_id, playlists_name:
        #
        #     playlists_url = "https://music.163.com/playlist?id=" + i
        #
        #     self.songs = self.fetch_songs(playlists_url, playlist)
        #
        #     print(self.songs)

        # return      # url of evey playlist

    def fetch_songs(self, url, playlist):
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

        if music_list:
            self.download(music_list, playlist)
            return music_list       # GENIUS
        # return

        # print(html)

    def download(self, song_list, playlist):
        """

        :param song_list: type list
        :param playlist: Name of 1 playlist
        :return:
        """
        for song in song_list:
            song_id = song['id'][0].split('=')[1]
            song_name = song['name'][0]


            formdata = {'params': self.get_params_song(song_id),        # todo add another parameter to get_params function e.g. get_params(song_id, s)||get_params(playlist_id, p) => get_params(id, key): if key else
                        'encSecKey': self.get_encSecKey()}


            response = requests.post(song_post_url, headers = HEADERS, data = formdata)
            download_url = json.loads(response.content)["data"][0]["url"]
            if download_url:
                try:

                    playlist_folder = self.path + self.user_name + "/" + playlist + "/"
                    if not os.path.exists(playlist_folder):
                        os.makedirs(playlist_folder)

                    download_path = playlist_folder + song_name + ".mp3"
                    # Seems to be the best method
                    # urllib.request.urlretrieve(download_url, self.path + self.user_name + "/" + playlist + "/" + song_name + ".mp3")
                    urllib.request.urlretrieve(download_url, download_path)

                    # os.makedirs(self.path + self.user_name + "/" + music_list + ".mp3")
                    print(song_name + "をゲットだぜ!")

                except Exception as e:
                    print("VIP SONG BRUH....")
                    print(e)


    def get_rank_profile(self, UID):

        formdata = {
            "params" : self.
            "encSecKey" : self.get_encSecKey()
        }


    def get_params_profile(self, UID):  # this is function d(d, e, f, g)

        encode = s.encode.encode()

        """
        function b(a, b)        "in another word, window.asrsea"
        a = "{\"uid\":\"350278537\",\"type\":\"-1\",\"limit\":\"1000\",\"offset\":\"0\",\"total\":\"true\",\"csrf_token\":\"\"}",
        b = "0CoJUm6Qyw8W8jud"
        """
        # a : encoded params
        # a = str({'ids': "[" + str(549321040) + "]", 'br': 128000, 'csrf_token': ""})
        a = """{\"uid\":\"""" + UID + """\",\"type\":\"-1\",\"limit\":\"1000\",\"offset\":\"0\",\"total\":\"true\",\"csrf_token\":\"\"}"""

        b = "0CoJUm6Qyw8W8jud"

        # Quotation mark sucks, so I'll just use str()
        # Edit : str() sucks

        self.i = encode.i
        # return self.encode.func_b(self.encode.func_b(a, b), self.i)       # Call encoding method in encode.py
        return encode.func_b(encode.func_b(a, b), self.i)  # Call encoding method in encode.py

    def get_params_song(self, SID):  # todo this is function d(d, e, f, g) SID
        encode = s.encode.encode()


        a = str({'ids': "[" + str(SID) + "]", 'br': 128000, 'csrf_token': ""})


        b = "0CoJUm6Qyw8W8jud"


        # Quotation mark sucks, so I'll just use str()
        # Edit : str() sucks



        self.i = encode.i
        # return self.encode.func_b(self.encode.func_b(a, b), self.i)       # Call encoding method in encode.py
        return encode.func_b(encode.func_b(a, b), self.i)  # Call encoding method in encode.py


    def get_encSecKey(self):
        # todo SecKey
        encode = s.encode.encode()

        b = "010001"

        c = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"

        # return self.func_c(self.i, b, c)
        return encode.func_c(self.i, b, c)

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
