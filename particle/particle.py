# -*- coding: utf-8 -*-
"""
.. module: particle.py
   :platform: Windows, Linux, OSX
   :synopsis: A brief description of the function.
   
.. moduleauthor:: Mike Qin <laigui@gmail.com>
"""

# ============================================================================
#% Imports
# ============================================================================
from scipy import constants


# ============================================================================
#% Classes
# ============================================================================
class Particle():
    """A particle is a constituent unit of the universe.
    
    Args:
    c (:obj:`float`): charge in units of [e].
    m (:obj:`float`): mass in units of [kg].
    r (:obj:`dict`): position in units of [meters].
    """
    
    roar = "I am a particle!"
    
    def __init__(self, charge, mass, position):
        """Initializes the particle with default values for charge c, mass m, 
        and position r.
        """
        self.c = charge
        self.m = mass
        self.r = position  
        
    def hear_me(self):
        myroar = self.roar + (
        "\n My charge is: " + str(self.c) +
        "\n My mass is: " + str(self.m) +
        "\n My x position is: " + str(self.r['x']) +
        "\n My y position is: " + str(self.r['y']) +
        "\n My z position is: " + str(self.r['z']))
        print(myroar)
        
    @staticmethod
    def possible_flavors():
        return ["up", "down", "top", "bottom", "strange", "charm"]

    def flip(self):
        if self.flavor == "up":
            self.flavor = "down"
        elif self.flavor == "down":
            self.flavor = "up"
        elif self.flavor == "top":
            self.flavor = "bottom"
        elif self.flavor == "bottom":
            self.flavor = "top"
        elif self.flavor == "strange":
            self.flavor = "charm"
        elif self.flavor == "charm":
            self.flavor = "strange"
        else :
            raise AttributeError("The quark cannot be flipped, because the flavor is not valid.")
            
    def delta_x_min(self, delta_p_x):
        hbar = constants.hbar
        delx_min = hbar / (2.0 * delta_p_x)
        return delx_min