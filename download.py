import requests
import os
from lxml import etree
from bs4 import BeautifulSoup as bs

prefix = "./htmls/"
cnt = 0

def download(filename):
    global cnt
    with open(prefix + filename, "r") as f:
        soup = bs(f.read(), features="lxml")
    src = soup.find("video").contents[0]["src"]
    src = "https:" + src
    title = soup.find("meta",{"data-react-helmet": "true", "name": "description"})["content"]
    print("[v] Downloading:  " + title)
    with open("./result/" + str(cnt) + ".mp4", "wb") as f:
        response = requests.get(src)
        f.write(response.content)
    print("[v] Done")
    print("=======================================")
    cnt += 1

if __name__ == '__main__':
    files = os.listdir(prefix)
    for filename in files:
        if ".html" in prefix + filename:
            download(filename)

