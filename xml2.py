#!/usr/bin/env python3
import xml.etree.ElementTree as ET

data = '''<stuff>
<users>
  <user x="2">
    <id>001</id>
    <name>Chuck</name>
  </user>
  <user x="7">
    <id>009</id>
    <name>Brent</name>
  </user>
</users>
</stuff>'''
stuff = ET.fromstring(data)

user_list = stuff.findall('users/user')  # Creates a list of smaller trees
print("User count: ", len(user_list))
for item in user_list:
    print('-'*50)
    print('Name: ', item.find('name').text)
    print('Id: ', item.find('id').text)
    print('User Attribute: ', item.get("x"))
