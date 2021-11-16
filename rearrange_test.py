#!/usr/bin/env python3
import unittest
from rearrange import rearrange_name
#class which will inherit from unittest.TestCase
class TestRearrage(unittest.TestCase):
  def test_basic(self):
    testcase = "Lovelace Ada"
    expected = "Ada Lovelace"
    self.assertEqual(rearrange_name(testcase), expected)
unittest.main()
