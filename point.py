# -*- coding: utf-8 -*-
"""
.. module: point.py
   :platform: Windows, Linux, OSX
   :synopsis: A brief description of the function.
   
.. moduleauthor:: Mike Qin <laigui@gmail.com>
"""

# ============================================================================
#% Imports
# ============================================================================


# ============================================================================
#% Classes
# ============================================================================
class Point:
    """Point class for representing and manipulating x,y cooridinates."""
    
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY
        
    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
    

# ============================================================================
#% Main Entry
# ============================================================================
if __name__ == "__main__":
    #testing class constructor (__init__ method)
    p = Point(3, 4)
    assert p.y == 4
    assert p.x == 3
    
    #testing the distance method
    p = Point(3, 4)
    assert p.distanceFromOrigin() == 5.0
    
    #testing the move method
    p = Point(3, 4)
    p.move(-2, 3)
    assert p.x == 1
    assert p.y == 7