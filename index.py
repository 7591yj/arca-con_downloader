import os
import urllib.request
from bs4 import BeautifulSoup
from enum import Enum

hdrs = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
      'AppleWebKit/537.11 (KHTML, like Gecko) '
      'Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}

class Extension(Enum):
    IMG = 1
    VID = 2

def download(links, whatFileIsIt):
    n = 1
    for link in links:
        link_url = "https:"+link["src"]
        link_extension = link_url.split(".")[-1]    
        req = urllib.request.Request(url=link_url, headers=hdrs)
        with urllib.request.urlopen(req) as f:
            if whatFileIsIt == Extension.IMG:
                with open('./img/' + str(n)+"."+link_extension, 'wb') as h:
                    img = f.read()
                    h.write(img)
                    print("Downloaded img: "+str(n))
            elif whatFileIsIt == Extension.VID:
                with open('./video/' + str(n)+"."+link_extension, 'wb') as h:
                    vid = f.read()
                    h.write(vid)
                    print("Downloaded video: "+str(n))
        n += 1
    print("Download completed.")

def find_data(soup):
    div = soup.find("div", class_="emoticons-wrapper")
    images = div.find_all("img")
    videos = div.find_all("video")

    if images:
        download(images, whatFileIsIt=Extension.IMG)
    if videos:
        download(videos, whatFileIsIt=Extension.VID)

def init():
    print("Arca-con Downloader")
    print("Please create a folder named 'img' in the same directory before using this program.")
    url = input("Enter your URL: ")

    req = urllib.request.Request(url=url, headers=hdrs) 
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, "html.parser")
    find_data(soup)

init()

os.system('pause')
