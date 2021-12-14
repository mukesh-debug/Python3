#!/usr/bin/env python3
import xml.etree.ElementTree as ET  # 'ET' is alias here

# Define a multi line string i.e xml data as string
data = '''
<person>
 <name>Chuck</name>
 <phone type="intl">
   +1 734 303 4456
 </phone>
 <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)  # Using string create tree structure of xml

print('Name: ', tree.find('name').text)  # 'text' method gets text values for a tag
# 'find' method search for a tag in the tree structure
print('Phone: ', tree.find('phone').text.strip())
print('Attribute: ', tree.find('email').get('hide'))
# get method after find method is to search for key value pair of attributes
