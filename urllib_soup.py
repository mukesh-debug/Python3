#!/usr/bin/env python3

import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup

url = input('Enter url - ')
print('Input url is of length ', len(url), ', taking default url',
        "'http://www.dr-chuck.com/page1.htm'")
if not len(url):
    url = 'http://www.dr-chuck.com/page1.htm'

html = urllib.request.urlopen(url).read()  # Reads byte string 
# To parse or make sense of read byte string with errors use BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')  # To parse zibberish to get meaning

# Retrieving all the anchor tags, marked by <a>
tags = soup('a')  # search 'soup' object

for tag in tags:
    print(tag.get('href', None))  # get method of string check for key as first agr
