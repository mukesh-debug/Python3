#!/usr/bin/env python3

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# To ignore ssl errore while opening https sites
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Input - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# To retrieve all the anchor tags from the parsed url
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))  # Prints only anchor tags containing 'href'
