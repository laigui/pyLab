# -*- coding: utf-8 -*-
"""
.. module: wof.py
   :platform: Windows, Linux, OSX
   :synopsis: A brief description of the function.
   
.. moduleauthor:: Mike Qin <laigui@gmail.com>
"""

# ============================================================================
#% Imports
# ============================================================================
import json
import random
import time


# ============================================================================
#% Classes
# ============================================================================
class WOFPlayer():
    """A class representing a Wheel of Fortune player."""
    def __init__(self, name):
        """Example of docstring on the __init__ method.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.prizeMoney = 0 # The amount of prize money for this player
        self.prizes = []    # The prizes this player has won so far
        
    def addMoney(self, amt):
        self.prizeMoney += amt

    def goBankrupt(self):
        self.prizeMoney = 0
        
    def addPrize(self, prize):
        self.prizes.append(prize)
        
    def __str__(self):
        return '{} (${})'.format(self.name, self.prizeMoney)
    
    
class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obscurePhrase, guessed):
        print('{} has ${}'.format(self.name, self.prizeMoney))
        print('')
        print('Category: {}'.format(category))
        print('Phrase: {}'.format(obscurePhrase))
        print('Guessed: {}'.format(guessed))
        inputValue = input("Guess a letter, phrase, or type 'exit' or 'pass': ")
        
        if inputValue == 'exit':
            exit()
        elif inputValue == 'pass':
            pass
        else:
            return inputValue
    
    
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    
    def __init__(self, name, diff):
        super().__init__(name)
        self.difficulty = diff
    
    def smartCoinFlip(self):
        rand_number = random.randint(1, 10)
        if rand_number > self.difficulty:
            return True
        else:
            return False
    
    def getPossibleLetters(self, guessed):
        letters = [letter for letter in LETTERS if letter not in guessed]
        
        if self.prizeMoney < VOWEL_COST:
            letters = [letter for letter in letters if letter not in VOWELS]
        
        return letters
        
    def getMove(self, category, obscurePhrase, guessed):
        guess_result = self.getPossibleLetters(guessed)
        
        if guess_result == []:
            return "pass"
        
        if self.smartCoinFlip() == True:
            for x in self.SORTED_FREQUENCIES:
                if x in guess_result:
                    break
                    return x
        else:
            return random.choice(guess_result)
    

# ============================================================================
#% Main Entry
# ============================================================================
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS  = 'AEIOU'
VOWEL_COST  = 250

# Repeatedly asks the user for a number between min & max (inclusive)
def getNumberBetween(prompt, min, max):
    userinp = input(prompt) # ask the first time

    while True:
        try:
            n = int(userinp) # try casting to an integer
            if n < min:
                errmessage = 'Must be at least {}'.format(min)
            elif n > max:
                errmessage = 'Must be at most {}'.format(max)
            else:
                return n
        except ValueError: # The user didn't enter a number
            errmessage = '{} is not a number.'.format(userinp)

        # If we haven't gotten a number yet, add the error message
        # and ask again
        userinp = input('{}\n{}'.format(errmessage, prompt))

# Spins the wheel of fortune wheel to give a random prize
# Examples:
#    { "type": "cash", "text": "$950", "value": 950, "prize": "A trip to Ann Arbor!" },
#    { "type": "bankrupt", "text": "Bankrupt", "prize": false },
#    { "type": "loseturn", "text": "Lose a turn", "prize": false }
def spinWheel():
    with open("wheel.json", 'r') as f:
        wheel = json.loads(f.read())
        return random.choice(wheel)

# Returns a category & phrase (as a tuple) to guess
# Example:
#     ("Artist & Song", "Whitney Houston's I Will Always Love You")
def getRandomCategoryAndPhrase():
    with open("phrases.json", 'r') as f:
        phrases = json.loads(f.read())

        category = random.choice(list(phrases.keys()))
        phrase   = random.choice(phrases[category])
        return (category, phrase.upper())

# Given a phrase and a list of guessed letters, returns an obscured version
# Example:
#     guessed: ['L', 'B', 'E', 'R', 'N', 'P', 'K', 'X', 'Z']
#     phrase:  "GLACIER NATIONAL PARK"
#     returns> "_L___ER N____N_L P_RK"
def obscurePhrase(phrase, guessed):
    rv = ''
    for s in phrase:
        if (s in LETTERS) and (s not in guessed):
            rv = rv+'_'
        else:
            rv = rv+s
    return rv

# Returns a string representing the current state of the game
def showBoard(category, obscuredPhrase, guessed):
    return """
Category: {}
Phrase:   {}
Guessed:  {}""".format(category, obscuredPhrase, ', '.join(sorted(guessed)))

