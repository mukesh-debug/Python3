#!/usr/bin/env python3
import re
#func to rearrange first and last name
def rearrange_name(name):
  result = re.search(r"^([\w .]*) ([\w .]*)$", name)
  return "{} {}".format(result[2], result[1])

