#!/usr/bin/env python3
from bs4 import BeautifulSoup as bs
import urllib.request as urllib



def getHtml(url):
    res  = urllib.urlopen(url)
    html = res.read()
    content = bs(html,'html.parser')
    return content

def openFromRaw():
    file = open('raw.html', 'r')
    cnt  = file.read()
    new  = bs(cnt,'html.parser')
    return new

def pretty(uglyhtml):
    return uglyhtml.prettify()


def saveTofile(content):
    file = open('raw.html','w+')
    file.write(content)
    file.close()

def getUri(num):
    return "https://www.narendramodi.in/speech/loadspeeche?page=%s&language=en" % (num)


if __name__ == "__main__":
    link_list = set()
    page_id = 0
    last_id = 0
    while page_id != last_id + 1:
        uri = getUri(page_id)
        html = getHtml(uri)
        for a in html.find_all('a'):
            if a.get('class')[0] == 'left_class':
                link_list.add(a.get('href'))
        page_id += 1
        print(page_id)

    with open('links', 'w+') as f:
        for a in link_list:
            f.write('%s\n' % (a))

