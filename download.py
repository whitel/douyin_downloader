import requests
import os
from lxml import etree
from bs4 import BeautifulSoup as bs
import datetime
import hashlib

prefix = "./htmls/"

def download(filename):
    # read local html contents
    with open(prefix + filename, "r") as f:
        soup = bs(f.read(), features="lxml")

    # get actual video address
    src = soup.find("video").contents[0]["src"]
    src = "https:" + src

    # get video contents
    title = soup.find("meta",{"data-react-helmet": "true", "name": "description"})["content"]
    print("[v] Downloading:  " + title)
    response = requests.get(src)
    video_content = response.content

    # write to local file
    author = soup.find("div", {"class": "account-name"}).text
    video_hash = hashlib.sha1(video_content)
    with open("./result/" + author + "-" + video_hash.hexdigest() + ".mp4", "wb") as f:
        f.write(video_content)
    print("[v] Done")
    print("====================================================")

if __name__ == '__main__':
    files = os.listdir(prefix)
    for filename in files:
        if ".html" in prefix + filename:
            download(filename)

