#!/usr/bin/env python3
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET

# To ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Input url: ')
xml = urllib.request.urlopen(url, context=ctx).read()
#print(xml)
#print('-'*80)
#print(xml.decode()) # xml looks good for printing on stdout using decode() 
#soup = BeautifulSoup(xml, 'html.parser') 
# HTML parser makes xml bad by taking out indentation
# however indentation doesn't affect xml, but it can help in error reduction using other func
#print(soup)
tree = ET.fromstring(xml)
#print(tree)
comments_list = tree.findall('comments/comment')
sum_count, counts = 0, 0
for comment_item in comments_list:
    sum_count += int(comment_item.find('count').text)
    counts += 1
print('Count: ',counts)
print('Sum of data: ', sum_count)
