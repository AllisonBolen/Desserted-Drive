from random import *
from Observable import *
class Werewolves(Observable):

    ''' Werewolves attack at a rate of 0-40 HP per turn.
    They are not harmed by ChocolateBars or SourStraws. Start with 200 HP. '''

    def __init__(self):
        self.attack = randint(0, 40)
        self.hp = 200
        self.candy = ['ChocolateBars', 'SourStraws'] # candy its not hurt by
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

    #helper funcs
    def genAttack(self):
        self.attack = randint(0, 40)
        return self.attack
