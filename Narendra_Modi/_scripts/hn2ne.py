#!/usr/bin/env python3
from bs4 import BeautifulSoup as bs
import requests

uri = "https://translate.google.com/#view=home&op=translate&sl=hi&tl=en&text=%E0%A4%B8%E0%A4%AD%E0%A5%80%20%E0%A4%B5%E0%A4%B0%E0%A4%BF%E0%A4%B7%E0%A5%8D"
res = requests.get(uri)

soup = bs(res.text, 'html.parser')

print(soup.prettify())

