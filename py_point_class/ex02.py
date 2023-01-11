#2. Write a perimeter method in the Rectangle class so that we can find the perimeter
#   of any rectangle instance:
#
#   r = Rectangle(Point(0, 0), 10, 5)
#   test(r.perimeter() == 30)

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
    
    def perimeter(self):
        return 2 * (self.width + self.height)

r = Rectangle(Point(0, 0), 10, 5)
test(r.perimeter() == 30)