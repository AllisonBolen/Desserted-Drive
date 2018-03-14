from random import *
from Observable import *
from NPCS.NPC import *

class NPC(Observable):

    ''' Base class '''

    def __init__(self):
        self.attack = 0
        self.hp = 0
        self.candy = []  # candy its not hurt by
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
        pass
