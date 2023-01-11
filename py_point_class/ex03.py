#3. Write a flip method in the Rectangle class that swaps the width and the 
#   height of any rectangle instance:
#
#   r = Rectangle(Point(100, 50), 10, 5)
#   test(r.width == 10 and r.height == 5)
#   r.flip()
#   test(r.width == 5 and r.height == 10)

from Point import Point
from Rectangle import Rectangle

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def flip(self):
        w = self.width
        h = self.height
        self.width = h
        self.height = w

r = Rectangle(Point(100, 50), 10, 5)
test(r.width == 10 and r.height == 5)
r.flip()
test(r.width == 5 and r.height == 10)