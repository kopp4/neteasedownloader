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

from enum import Enum

import base64, codecs
from Crypto.Cipher import AES

import src as s

# import src.encode     encode = src.encode.encode()
"""
functions related to post
"""

HEADERS = {
    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

regex = r"\"name\"\s?:\s?\"(.+?)\""                                 # Regex for filtering the playlists name in the profile

regex1 = r'''\"title\"\s?:\s?\"(.+)\"'''                                            # for getting username in user profile

regex2 =  r"\"id\"\s?\s?\:(\d+)"                                                    # Regex for obtain all the playlists id

regex3 = r"\"score\":(\d+?),\"song\":{\"name\":\"(.+?)\""       # Regex for obtaining song score in user's ranking

# regex4 = r"\"song\":{\"name\":\"(.+?)\""       # Regex for obtaining song name in user's ranking

playlists_post_url = "https://music.163.com/weapi/user/playlist?csrf_token="

song_post_url = "https://music.163.com/weapi/song/enhance/player/url?csrf_token="

rank_post_url = "https://music.163.com/weapi/v1/play/record?csrf_token="

path = "e:/Music/"

class getNetease:

    """Path of the main folder"""

    def __init__(self, profile_url):

        self.user_name = self.fetch_user(profile_url)

        print("Greetings, " + self.user_name)

        # CORE
        # CORE
        # CORE
        # self.fetch_playlists(uid)       # Recursively obtain all the songs in all the playlists
        # CORE
        # CORE
        # CORE
        # CORE


    def _get_params(self, ID, key):                                                      # this is function d(d, e, f, g)
        """
        :key :  "profile", "song"
        """
        encode = s.encode.encode()

        """
        function b(a, b)        "in another word, window.asrsea"
        a = "{\"uid\":\"350278537\",\"type\":\"-1\",\"limit\":\"1000\",\"offset\":\"0\",\"total\":\"true\",\"csrf_token\":\"\"}",
        b = "0CoJUm6Qyw8W8jud"
        """
        # a : encoded params
        if key == "profile":
            a = """{\"uid\":\"""" + ID + """\",\"type\":\"-1\",\"limit\":\"1000\",\"offset\":\"0\",\"total\":\"true\",\"csrf_token\":\"\"}"""   # str() is way better
        elif key == "song":
            a = str({'ids': "[" + str(ID) + "]", 'br': 128000, 'csrf_token': ""})                            # todo str() yes
            # Quotation mark sucks, so I'll just use str()
        else:
            print("Error : Params are Wrong!!!")

        b = "0CoJUm6Qyw8W8jud"

        self.i = encode.i                                               # i is supposed to be unified

        return encode.func_b(encode.func_b(a, b), self.i)               # Call encoding method in encode.py

    def _get_encSecKey(self):
        # todo SecKey
        encode = s.encode.encode()

        b = "010001"

        c = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"

        # return self.func_c(self.i, b, c)

        return encode.func_c(self.i, b, c)

    def _download(self, song_list, playlist):
        """

        :param song_list: type list
        :param playlist: Name of 1 playlist
        :return:
        """
        for song in song_list:
            song_id = song['id'][0].split('=')[1]
            song_name = song['name'][0]

            response = requests.post(song_post_url, headers = HEADERS, data = self.get_modify_formdata(song_id, "song"))
            download_url = json.loads(response.content)["data"][0]["url"]
            if download_url:
                try:

                    playlist_folder = path + self.user_name + "/" + playlist + "/"
                    if not os.path.exists(playlist_folder):
                        os.makedirs(playlist_folder)

                    download_path = playlist_folder + song_name + ".mp3"
                    # Seems to be the best method
                    # urllib.request.urlretrieve(download_url, path + self.user_name + "/" + playlist + "/" + song_name + ".mp3")
                    urllib.request.urlretrieve(download_url, download_path)

                    # os.makedirs(path + self.user_name + "/" + music_list + ".mp3")
                    print(song_name + "をゲットだぜ!")

                except Exception as e:
                    print("VIP SONG BRUH....")
                    print(e)

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

    # Default : calling fetch_songs func
    def fetch_playlists(self, uid):

        response = requests.post(playlists_post_url, headers = HEADERS, data = self.get_modify_formdata(uid, "profile"))

        content = str(response.content, encoding = "utf-8")  # Or else \x9f\xe5\xa3\xb0 blah blah

        print(re.findall(regex, content))      # Printing all playlists name in the profile

        playlists_name = re.findall(regex, content)

        playlists_id = re.findall(regex2, content)   # Obtain all playlists id in the profile

        print(self.user_name)

        print("Fetching playlists of " + self.user_name + "'s")

        del playlists_id[0]     # 《登录后才可以查看》

        del playlists_name[0]      # 《登录后才可以查看》

        while playlists_name:
            for i in playlists_id:

                playlists_url = "https://music.163.com/playlist?id=" + i

                songs = self.fetch_songs(playlists_url, playlists_name[0])          # Default : calling fetch_songs func

                print(playlists_name[0])

                print(songs)

                playlists_name.pop(0)

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
            self._download(music_list, playlist)
            return music_list       # GENIUS
        # return

        # print(html)

    def fetch_rank(self, uid):

        print("Fetching ranking of " + self.user_name + "'s")

        response = requests.post(rank_post_url, headers = HEADERS, data = self.get_modify_formdata(uid, "profile"))

        content = response.text

        print(content)

        score = re.findall(regex3, content)

        # song = re.findall(regex4, content)

        print(score)


        return



    def get_modify_formdata(self, ID, key):         # **ID** : song or profile id, **key** : key to judge the posting params

        formdata = {
            "params": self._get_params(ID, key),
            "encSecKey": self._get_encSecKey()
        }
        return formdata




    # def get_rank_profile(self, UID):
    #
    #     formdata = {
    #         "params" : self.
    #         "encSecKey" : self.get_encSecKey()
    #     }






# todo     '''Storing playlists & Songs from specified UID'''
#
#     def store_P(self):
#         store.playlists()
#     def store_S(self):
#         store.songs()
#         print("this is cursed")
