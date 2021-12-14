#!/usr/bin/env python3
import urllib.request, urllib.parse, urllib.error
import json

url = input("Input url: ")
data = urllib.request.urlopen(url).read()
js = json.loads(data)
#print(js) # Non formatted object print
print(json.dumps(js, indent=4)) # Formatted output of json data as python data type
print('-'*80)

comments_list = js["comments"]
sum_text = 0
for comment in comments_list:
    sum_text += int(comment["count"])
print('Sum: ', sum_text)
