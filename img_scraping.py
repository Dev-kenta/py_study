# coding: UTF-8
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import uuid
import time
import sys
import re

# 画像を保存する関数
def download_image(url, dst_path, headers):
    try:
        request = urllib.request.Request(url=url, headers=headers)
        data = urllib.request.urlopen(request).read()
        with open(dst_path, mode="wb") as f:
            f.write(data)
    except urllib.error.URLError as e:
        print(e)

# 引数出力
args = sys.argv
# print(args[1])

# アクセスするURL
url = args[1]

# ユーザーエージェントをfirefoxに偽装
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
request = urllib.request.Request(url=url, headers=headers)
html = urllib.request.urlopen(request)

# 画像を取得
soup = BeautifulSoup(html, "html.parser")

# imgタグの取得domリスト
tag_doms = {
    'pururun': {'dom': '.pict', 'tag': 'src'},
    'ertk': {'dom': '.img_frame a', 'tag': 'href'},
    'mink': {'dom': '.pict', 'tag': 'src'},
    'bakufu': {'dom': '.entry-content img', 'tag': 'src'},
}

# imgタグを全部取得
try:
    img = soup.select(tag_doms[args[3]]['dom'])
except Exception as e:
    print(e)

# 画像を格納する配列
img_list = []

# forで回す
for tag in img:
   try:
        # print(tag)
        # path = 'http://i4.ertk.net' + tag.get('data-src')
        # path = 'http://ertk.net' + tag.get('href')
        if args[3] == 'ertk':
            path = 'http://ertk.net' + tag.get(tag_doms[args[3]]['tag'])
        elif args[3] == 'mink':
            path = 'https:' + tag.get(tag_doms[args[3]]['tag'])
        else:
            path = tag.get(tag_doms[args[3]]['tag'])
        # path = tag.get('href')
        # path = 'https:' + tag.get('href')
        img_list.append(path)
   except Exception as e:
       print(e)

# 画像を保存する処理
download_dir = 'images'
sleep_time_sec = 1

count = 0
total = len(img_list)
for url in img_list:
    dst_path = str('/Users/kataokakenta/Desktop/')+args[2]+'/'+str(uuid.uuid4())+str('.jpeg')
    time.sleep(sleep_time_sec)
    count += 1
    print('%s/%s' % (count,total))
    # print(url, dst_path)
    download_image(url, dst_path, headers)
