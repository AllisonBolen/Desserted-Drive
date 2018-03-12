
from random import *

class Vampire(observable):

''' Vampires attack at a rate of 10-20 HP per turn. They are not harmed by
ChocolateBars. Start with 100-200 HP. '''

    def __init__(self):
        self.attack = randint(10, 20)
        self.hp = ranint(100, 200)
        self.candy = ['ChocolateBars'] # candy its not hurt by
        self.special = []

    # getters
    def getAttack(self):
        return self.attack

    def getHP(self):
        return self.hp

    def getCandy(self):
        return self.candy

    def getSpecial(self):
        return self.special

    # setters
    def setSpecial(self, special):
        self.special = special

    def setAttack(self, a):
        self.attack = a

    def setHP(self, hp):
        self.hp = hp

    def setCandy(self, c):
        self.candy = c

    # helper funcs
    def genAttack(self):
        self.attack = randint(10, 20)
        return attack
