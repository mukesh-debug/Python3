#!/usr/bin/env python3
import urllib.request
import urllib.parse
import urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = {}
for line in fhand:
    words = line.decode().split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
# print(counts)
for k, v  in counts.items():
    print(k, ": ", v)
