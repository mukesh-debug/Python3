#!/usr/bin/env python3
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# To ignore certificate error for https requests
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Input url: ')
count = int(input('Input count: '))
pos = int(input('Input position: '))

for _ in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    refined_tags = []
    for tag in tags:
        refined_tags.append(tag.get('href', None))
    print("Retrieving : ", refined_tags[pos-1])
    url = refined_tags[pos-1]
