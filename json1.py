#!/usr/bin/env python3
import json
data ='''{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''
# If any extra comma is inserted at end of one key value pair like in dict 
# for ease of adding new pair of data, it creates problem with json.loads()
# Also only use " (double quotes since singel quotes are already in use for
# multiline string, otherwise it would result in error

info = json.loads(data)  # object returned is a python dictionary
print('Name: ', info["name"])
print('Hide: ', info["email"]["hide"])
print("Phone: ", info["phone"]["number"])
