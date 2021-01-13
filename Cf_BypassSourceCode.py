#!/usr/bin/env python3

import cloudscraper
import re
from bs4 import BeautifulSoup
import time
links = []

def linkWriter(a,links):
    scraper = cloudscraper.create_scraper()
    trc = scraper.get(a).content
    r = BeautifulSoup(trc,"lxml")
    x = r.find_all(href=re.compile("https"))
    for link in x:
        link = link.get('href')
        links.append(link)
        print(link)                 # 
    return links


a = input("Url Giriniz: ")

links = linkWriter(a,links)           # 
print(links)

time.sleep(1)                         # 

print("--------------------------------------")
links2 = []                         # 
for i in links:
    linkWriter(i,links2)

print("-------------------------------------")
print(links2)
