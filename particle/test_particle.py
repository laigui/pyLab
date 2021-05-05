# -*- coding: utf-8 -*-
"""
.. module: class.py
   :platform: Windows, Linux, OSX
   :synopsis: A brief description of the function.
   
.. moduleauthor:: Mike Qin <laigui@gmail.com>
"""

# ============================================================================
# % Imports
# ============================================================================
from unittest import TestCase

from scipy import constants
import particle as p


# ============================================================================
# % Test Cases
# ============================================================================



class TestParticle(TestCase):
    def test_hear_me(self):
        self.fail()

    def test_possible_flavors(self):
        self.fail()

    def test_flip(self):
        self.fail()

    def test_delta_x_min(self):
        self.fail()

    def test_particle_init():
        m_p = constants.m_p
        r_p = {'x': 1, 'y': 1, 'z': 53}
        a_p = p.Particle(1, m_p, r_p)
        assert a_p.r == r_p
        assert a_p.m == m_p