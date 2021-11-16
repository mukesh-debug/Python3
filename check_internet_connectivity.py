#!/usr/bin/env python3
"""To check if you are connected to the internet.
   This script will try to establish connection with example.com.
   Since http://example.com is maintained by IANA it is one of the reliable metric.
"""
import requests
def check_connection():
  url = "https://example.com"
  timeout = 5
  try:
    request = requests.get(url, timeout=timeout)
    print("Connected to the Internet")
    return True
  except (requests.ConnectionError, requests.Timeout) as exception:
    print('No internet connection')
    return False

if __name__=='__main__':
  check_connection()
  #print('-'*80)
  #print(check_connection())
