from random import *

class NerdBombs(object):

    ''' NerdBombs are the best weapon in the game, modifying a player's attack
    by between 3.5 and 5. Unfortunately, they are single use. '''

    def __init__(self):
        self.modif = uniform(3.5, 5)
        self.uses = 4

    def getUses(self):
        return self.uses

    def getModif(self):
        return self.modif

    def setUses(self, uses):
        self.uses = uses

    def setModif(self, modif):
        self.modif = modif

    def genModif(self):
        self.modif = uniform(3.5, 5)
        return self.modif
