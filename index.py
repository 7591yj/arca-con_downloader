import os
import urllib.request
from bs4 import BeautifulSoup

print("Arca-con Downloader")
print("Please create a folder named 'img' in the same directory before using this program.")
url = input("Enter your URL: ")
hdrs = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
      'AppleWebKit/537.11 (KHTML, like Gecko) '
      'Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}

req = urllib.request.Request(url=url, headers=hdrs) 
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, "html.parser")

div = soup.find("div", class_="emoticons-wrapper")
images = div.find_all("img")
videos = div.find_all("video")

n = 1
for image in images:
    image_url = "https:"+image["src"]
    image_extension = image_url.split(".")[-1]    
    req = urllib.request.Request(url=image_url, headers=hdrs)
    with urllib.request.urlopen(req) as f:
        with open('./img/' + str(n)+"."+image_extension, 'wb') as h:
            img = f.read()
            h.write(img)
            print("Downloaded img: "+str(n))
    n += 1

m = 1
for video in videos:
    video_url = "https:"+video["src"]
    video_extension = video_url.split(".")[-1]    
    req = urllib.request.Request(url=video_url, headers=hdrs)
    with urllib.request.urlopen(req) as f:
        with open('./video/' + str(m)+"."+video_extension, 'wb') as h:
            img = f.read()
            h.write(img)
            print("Downloaded video: "+str(m))
    m += 1

print("Download completed.")
os.system('pause')