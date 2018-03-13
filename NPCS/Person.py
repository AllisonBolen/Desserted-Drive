from Observable import *
class Person(Observable):

    '''Persons help you by giving you candy. Each piece of candy increases your
    health by 1 point. A person can give you 1 piece of candy per turn. We could
    see this "helping" from the person as an attack with a negative attack value.
    Persons have 100 health and are not harmed by your attacks.'''

    def __init__(self):
        self.attack = -1
        self.hp = 100
        self.candy = ['SourStraws','ChocolateBars','NerdBombs'] # random choice to give player maybe?
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
