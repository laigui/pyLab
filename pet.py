# -*- coding: utf-8 -*-
"""
.. module: pet.py
   :platform: Windows, Linux, OSX
   :synopsis: A brief description of the function.
   
.. moduleauthor:: Mike Qin <laigui@gmail.com>
"""

# ============================================================================
#% Imports
# ============================================================================
from random import randrange


# ============================================================================
#% Classes
# ============================================================================
class Pet():
    """A brief description of the class."""
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    def __init__(self, name="Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]
        
    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"   

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger {} Boredom {} Words {}".format(self.hunger, self.boredom, self.sounds)
        return state
    
    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()
        
    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)


class Cat(Pet):
    sounds = ['Meow']

    def mood(self):
        if self.hunger > self.hunger_threshold:
            return "hungry"
        if self.boredom <2:
            return "grumpy; leave me alone"
        elif self.boredom > self.boredom_threshold:
            return "bored"
        elif randrange(2) == 0:
            return "randomly annoyed"
        else:
            return "happy"

    def chasing_rats(self):
        return "What are you doing, Pinky? Taking over the world?!"


class Dog(Pet):
    sounds = ['Woof', 'Ruff']

    def mood(self):
        if (self.hunger > self.hunger_threshold) and (self.boredom > self.boredom_threshold):
            return "bored and hungry"
        else:
            return "happy"


class Cheshire(Cat): # this inherits from Cat, which inherits from Pet

    def smile(self): # this method is specific to instances of Cheshire
        print(":D :D :D")
        
        
class Bird(Pet):
    sounds = ["chirp"]
    
    def __init__(self, name="Kitty", chirp_number=2):
        Pet.__init__(self, name) # call the parent class's constructor
        # basically, call the SUPER -- the parent version -- of the constructor, with all the parameters that it needs.
        self.chirp_number = chirp_number # now, also assign the new instance variable

    def hi(self):
        for i in range(self.chirp_number):
            print(self.sounds[randrange(len(self.sounds))])
        self.update_boredom()
        
        
# ============================================================================
#% Main Entry
# ============================================================================
if __name__ == "__main__":
    p1 = Pet("Fido")
    print(p1) # we've seen this stuff before!
    
    p1.feed()
    p1.hi()
    print(p1)
    
    c1 = Cat("Fluffy")
    print(c1) # this uses the same __str__ method as the Pets do
    
    c1.feed() # Totally fine, because the cat class inherits from the Pet class!
    c1.hi()
    print(c1)
    
    print(c1.chasing_rats())
    
    new_cat = Cheshire("Pumpkin") # create a Cheshire cat instance with name "Pumpkin"
    new_cat.hi() # same as Cat!
    new_cat.chasing_rats() # OK, because Cheshire inherits from Cat
    new_cat.smile() # Only for Cheshire instances (and any classes that you make inherit
    
    d1 = Dog("Astro")
    
    c1.boredom = 1
    print(c1.mood())
    c1.boredom = 3
    for i in range(10):
        print(c1.mood())
    print(d1.mood())