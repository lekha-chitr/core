#!/usr/bin/env python3
from bs4 import BeautifulSoup as bs
import requests


def test():
    with open('link', 'r') as f:
        for link in f.readlines():
            r = requests.get(link)
            soup = bs(r.text, 'html.parser')


if __name__ == '__main__':
    test()
