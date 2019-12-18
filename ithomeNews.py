#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Author : GordonWei
#Date : Aug/06/19
#comment : Scrapying ITHome Today's News 

import requests, re, time, lineTool
from bs4 import BeautifulSoup

today = time.strftime('%Y-%m-%d')
lineToken = 'Your Line Notify Token'
ithome_site = 'https://www.ithome.com.tw/news'
indexRes = requests.get(ithome_site)
indexSoup = BeautifulSoup(indexRes.text, 'html.parser')
pages = indexSoup.find_all('span', class_ = 'views-field')

for n in pages:
        if n.find('p', text = re.compile(today)):
                if n.find('div'):
                        title = n.find('p', class_ = 'title').text
                        href = n.find('a')['href']
                botText = (today, title, 'https://www.ithome.com.tw' + href)
                lineTool.lineNotify(lineToken, botText)
