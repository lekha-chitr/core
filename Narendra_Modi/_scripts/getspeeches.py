#!/usr/bin/env python3
from bs4 import BeautifulSoup as bs
import requests


# helper
def pretty(uglyhtml):
    return uglyhtml.prettify()

def getArtical(url):
    html = requests.get(url)
    html = html.text
    content = bs(html,'html.parser')
    return article.get_text()

def save(link, name):
    text = getArtical(link)
    file = open('data/'+name+'.txt', 'w+')
    file.write(text)
    print('Written '+ name)
    file.close()


def init():
    with open('links', 'r') as f:
        link = f.readlines()
        for i in range(630, len(link)):
            s = link[i]
            name = s[s.rfind('/') + 1 :]
            save(s.strip(), name.strip())


if __name__ == '__main__':
    init()
