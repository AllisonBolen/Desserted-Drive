from random import *
from Weapons.Weapon import *

class ChocolateBars(Weapon):

    ''' ChocolateBars modify the players attack by between 2 - 2.4.
    They are usable 4 times. '''

    def __init__(self):
        Weapon.__init__(self)
        self.modif = uniform(2, 2.4)
        self.uses = 4
        self.name = 'ChocolateBars'

    def genModif(self):
        self.modif = uniform(2, 2.4)
        return self.modif
