
from random import *
from Observable import *
class Ghouls(Observable):

    ''' Ghouls attack at a rate of 15-30 HP per turn. They are harmed by
    all weapons, but receive 5X the attackers attack if attacked with NerdBombs.
    Start with 40-80 HP. '''

    def __init__(self):
        self.attack = randint(15, 30)
        self.hp = ranint(40, 80)
        self.candy = [] # candy its not hurt by
        self.special = ['NerdBombs']

    # getters
    def getAttack(self):
        return self.attack

    def getHP(self):
        return self.hp

    def getSpecial(self):
        return self.special

    def getCandy(self):
        return self.candy

    # setters
    def setAttack(self, a):
        self.attack = a

    def setHP(self, hp):
        self.hp = hp

    def setSpecial(self, special):
        self.special = special

    def setCandy(self, c):
        self.candy = c

    #helper funcs
    def genAttack(self):
        self.attack = randint(15, 30)
        return self.attack
