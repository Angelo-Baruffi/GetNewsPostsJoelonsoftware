# -*- coding: utf-8 -*-
"""
Created on Thu Feb 08 22:06:48 2018

@author: Angelo Baruffi Nogueira
"""

import pip
from datetime import datetime

def install(package):
    pip.main(['install', package])



try:
    import requests
except ImportError, e:
    install('requests')
    import requests

try:
    from bs4 import BeautifulSoup
except ImportError, e:
    install('bs4')
    from bs4 import BeautifulSoup


page = requests.get("https://www.joelonsoftware.com/")

soup = BeautifulSoup(page.content, 'html.parser')

divs = soup.findAll("div", {"class": "entry-date"})

day = divs[0].time['datetime']

day = day[:10]

datetime_obj = datetime.strptime(day, '%Y-%M-%d')

with open('data.txt') as f:
    content = f.readlines()

datetime_lest = datetime.strptime(content[0], '%Y-%M-%d')

if(datetime_obj > datetime_lest):
    
    with open("data.txt", "w") as f:
        f.write(datetime_obj.strftime('%Y-%M-%d'))    
 
    print("Tem um novo Post no Blog do JOEL ON SOFTWARE !!!!!!!!!!")
    input()