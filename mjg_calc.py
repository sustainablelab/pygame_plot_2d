#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

def bob():
    val = True 
    return val

class TestStuff(unittest.TestCase):
    def test_bob(self):
        self.assertTrue(bob())

def normxy_to_window(win_size:tuple, xy:tuple) -> tuple:
    """Map normalized xy-coordinate to xy in the OS window

    win_size: (w,h)
    xy: (x,y)
    """
    w,h = win_size
    x,y = xy
    return (x*w,(1-y)*h)

class TestTransform(unittest.TestCase):
    def test_normxy_to_window(self):
        w = 123
        h = 456
        self.assertEqual(normxy_to_window((w,h),(0,0)), (0,h))
        self.assertEqual(normxy_to_window((w,h),(0,1)), (0,0))
        self.assertEqual(normxy_to_window((w,h),(1,0)), (w,h))
        self.assertEqual(normxy_to_window((w,h),(0.2,0.2)), (w*0.2,h*0.8))

if __name__ == '__main__':
    unittest.main()
