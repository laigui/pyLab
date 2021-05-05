# -*- coding: utf-8 -*-
"""
.. module: pokemon.py
   :platform: Windows, Linux, OSX
   :synopsis: A brief description of the function.
   
.. moduleauthor:: Mike Qin <laigui@gmail.com>
"""

# ============================================================================
#% Imports
# ============================================================================
import numpy as np 
import matplotlib.pyplot as plt


# ============================================================================
#% Classes
# ============================================================================
class Pokemon():
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name,level = 5):
        self.name = name
        self.level = level
        self.weak = "Normal"
        self.strong = "Normal"

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10
        
    def opponent(self):
        return (self.weak, self.strong)

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"
    
    def __init__(self, name,level = 5):
        super().__init__(name, level = 5)
        self.weak = "Fire"
        self.strong = "Water"

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

class Ghost_Pokemon(Pokemon):
    p_type = "Ghost"

    def __init__(self, name,level = 5):
        super().__init__(name, level = 5)
        self.weak = "Dark"
        self.strong = "Psychic"
        
    def update(self):
        self.health_boost = 3
        self.attack_boost = 4
        self.defense_boost = 3

class Fire_Pokemon(Pokemon):
    p_type = "Fire"

    def __init__(self, name,level = 5):
        super().__init__(name, level = 5)
        self.weak = "Water"
        self.strong = "Grass"
        
class Flying_Pokemon(Pokemon):
    p_type = "Flying"
    
    def __init__(self, name,level = 5):
        super().__init__(name, level = 5)
        self.weak = "Electric"
        self.strong = "Fighting"
   

# ============================================================================
#% Main Entry
# ============================================================================
if __name__ == "__main__":
    p1 = Grass_Pokemon("Belle")
    print(p1)
    print(p1.opponent())