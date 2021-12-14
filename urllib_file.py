#!/usr/bin/env python3
import urllib.request, urllib.parse, urllib.error
# Using urllib library for opening file on webserver and read from it

# Open file using methods of request class from urllib
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# Process data using file handle set in previous instruction
for line in fhand:
    print(line.decode().strip())

