#!/usr/bin/env python3
import json
data =''' [
        {
            "id" : "001",
            "x" : "2",
            "name" : "Mukesh"
        },
        {
            "id" : "009",
            "x" : "7",
            "name" : "Kumar"
        }
    ]'''
info = json.loads(data) # Returns a list of python dictionaries
print("User count: ", len(info))
for user in info:
    print('-'*50)
    print(user["id"])
    print(user["x"])
    print(user["name"])
