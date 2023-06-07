#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Utilities for plotting.

Usage
-----
import mjg_plot

Definitions
-----------
point: (x,y)
line segment: (point,point)


doctest (treat the >>> examples in function docstrings as tests)
-------
;t<Space> to run doctest:
- runs `make test`
- recipe for target 'test': python -m doctest mjg_plot.py

unittest (run tests defined in children of unittest.TestCase)
--------
;so to run unittest:
- sources this file as a script
- if this is the main script, it runs unit tests:
    unittest.main()
"""

import unittest

def create_grid_lines(num_lines:int) -> tuple:
    """Return tuple of normalized line segments (hlines, vlines).

    normalized:
        Coordinate values are in range [0.0:1.0).

    line segment:
        A point is a tuple of x,y coordinates: (x,y)
        A line segment is a tuple of end points: ((x1,y1),(x2,y2))

    Parameters
    ----------
    num_lines : int
        Number of horizontal and vertical lines, not counting the x-axis and y-axis.
        (The first hline is the x-axis; the first vline is the y-axis.)
        Example: num_lines = 5 returns 6 hlines and 6 vlines.

    Return
    ------
    Return value is the tuple (hlines, vlines).

    Example: num_lines = 5

    hlines:
        index | line segment
        ----- | ------------
          0   | ((0.0,0.0),(1.0, 0.0))
          5   | ((0.0,1.0),(1.0, 1.0))

    vlines:
        index | line segment
        ----- | ------------
          0   | ((0.0,0.0),(0.0,1.0))
          5   | ((1.0,0.0),(1.0,1.0))

    >>> N=5
    >>> hlines,vlines = create_grid_lines(N)
    >>> for l in hlines: print(l)
    ((0.0, 0.0), (1.0, 0.0))
    ((0.0, 0.2), (1.0, 0.2))
    ((0.0, 0.4), (1.0, 0.4))
    ((0.0, 0.6), (1.0, 0.6))
    ((0.0, 0.8), (1.0, 0.8))
    ((0.0, 1.0), (1.0, 1.0))
    >>> for l in vlines: print(l)
    ((0.0, 0.0), (0.0, 1.0))
    ((0.2, 0.0), (0.2, 1.0))
    ((0.4, 0.0), (0.4, 1.0))
    ((0.6, 0.0), (0.6, 1.0))
    ((0.8, 0.0), (0.8, 1.0))
    ((1.0, 0.0), (1.0, 1.0))
    """
    N = num_lines
    # Generate x and y values
    xvals = [x/N for x in range(N+1)]
    yvals = [y/N for y in range(N+1)]
    # Combine x and y values to form horizontal and vertical line segments
    hlines = [((xvals[0],y),(xvals[N],y)) for y in yvals]
    vlines = [((x,yvals[0]),(x,yvals[N])) for x in xvals]
    return hlines,vlines

class TestPlot(unittest.TestCase):
    def test_create_grid_lines(self):
        N = 5
        # Returns tuple of size 2: (hlines,vlines)
        r = create_grid_lines(N)
        self.assertEqual(len(r),2)
        # Each tuple is of size N: N line segments in hlines, N in vlines
        hlines = r[0]
        vlines = r[1]
        self.assertEqual(len(hlines),N+1)
        self.assertEqual(len(vlines),N+1)
        # Each line segment in hlines or vlines is of size 2: (x1,y1),(x2,y2)
        hline0 = hlines[0]
        self.assertEqual(len(hline0),2)
        # Each point in each line segment is of size 2: a point (x,y)
        hl_p0 = hline0[0]
        self.assertEqual(len(hl_p0),2)

if __name__ == '__main__':
    unittest.main()
