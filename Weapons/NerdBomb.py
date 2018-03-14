from random import *
from Weapons.Weapon import *

class NerdBomb(Weapon):

    ''' NerdBombs are the best weapon in the game, modifying a player's attack
    by between 3.5 and 5. Unfortunately, they are single use. '''

    def __init__(self):
        Weapon.__init__(self)
        self.modif = uniform(3.5, 5)
        self.uses = 1
        self.name = 'NerdBomb'

    def genModif(self):
        self.modif = uniform(3.5, 5)
        return self.modif
