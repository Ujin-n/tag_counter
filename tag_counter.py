import urllib.request
from bs4 import BeautifulSoup
import tkinter as tk

url = 'https://yandex.ru'
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')
tags = soup.find_all()

tag_dict = {}

for tag in tags:
    tag_dict[tag.name] = tag_dict.get(tag.name, 0) + 1
