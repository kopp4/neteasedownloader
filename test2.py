import requests
from bs4 import BeautifulSoup

http_proxy = "http://127.0.0.1:7890"        # todo can't find a better way but now let's just use it
https_proxy = "http://127.0.0.1:7890"

HEADERS = {
    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

url = 'https://open.spotify.com/user/31jpixs7tmbzy4x6b3g6qefuonxy'

proxyDict = {
    "http": http_proxy,
    "https": https_proxy
}




r = requests.get(url, proxies=proxyDict, headers = HEADERS)
content = r.text

print(content)

soup = BeautifulSoup(content, "html.parser")

print(soup.title.string)

print(soup.title.)


