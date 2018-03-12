

from random import *

class Zombie(observable):

'''Zombies attack you at a rate of 0-10 HP per turn.
Zombies are harmed by any weapon, but if attacked with SourStraws lose
twice the number of points from an attack. Start with between 50 and 100 HP.'''

    def __init__(self):
        self.attack = randint(0, 10)
        self.hp = ranint(50, 100)
        self.candy = ['ChocolateBars', 'SourStraws', 'HersheyKisses', 'NerdBombs'] # candy its not hurt by
        self.special = ['SourStraws']

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
        return randint(15, 30)
