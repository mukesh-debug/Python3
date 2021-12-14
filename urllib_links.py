#!/usr/bin/env python3
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# To ignore ssl errors while opening https files
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Input url - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
sum_data, count = 0, 0
for tag in tags:
    sum_data += int(tag.contents[0])
    count += 1

print('Count ', count)
print('Sum ', sum_data)
