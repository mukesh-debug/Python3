#!/usr/bin/env python3
import unittest
from drawingBook import pageCount

class CountPages(unittest.TestCase):
    def test0(self):
        n, p = 6, 2
        result=1
        self.assertEqual(pageCount(n,p), result)

    def test1(self):
        n, p = 5, 4
        result=0
        self.assertEqual(pageCount(n,p), result)

if __name__=='__main__':
    unittest.main()
