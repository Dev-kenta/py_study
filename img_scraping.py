# coding: UTF-8
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import uuid
import time

# 画像を保存する関数
def download_image(url, dst_path, headers):
    try:
        request = urllib.request.Request(url=url, headers=headers)
        data = urllib.request.urlopen(request).read()
        with open(dst_path, mode="wb") as f:
            f.write(data)
    except urllib.error.URLError as e:
        print(e)

# アクセスするURL
url = "http://blog.livedoor.jp/pururungazou/archives/9382971.html"
# ユーザーエージェントをfirefoxに偽装
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
request = urllib.request.Request(url=url, headers=headers)
html = urllib.request.urlopen(request)

# 画像を取得
soup = BeautifulSoup(html, "html.parser")

# imgタグを全部取得
img = soup.select(".article-body-more a")

# 画像を格納する配列
img_list = []

# forで回す
for tag in img:
   try:
        # print(tag)
        # path = 'http://i4.ertk.net' + tag.get('data-src')
        # path = 'http://ertk.net' + tag.get('href')
        # path = tag.get('src')
        path = tag.get('href')
        img_list.append(path)
   except:
        pass

# 画像を保存する処理
download_dir = 'images'
sleep_time_sec = 1

count = 0
total = len(img_list)
for url in img_list:
    dst_path = str('/Users/kenta/Desktop/寺本莉緒/')+str(uuid.uuid4())+str('.jpeg')
    time.sleep(sleep_time_sec)
    count += 1
    print('%s/%s' % (count,total))
    # print(url, dst_path)
    download_image(url, dst_path, headers)
