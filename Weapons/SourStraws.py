from random import *

from Weapons.Weapon import *


class SourStraws(Weapon):
    ''' SourStraws provide an attack modifier between 1 - 1.75.
    They can be used twice. '''

    def __init__(self):
        Weapon.__init__(self)
        self.modif = uniform(1, 1.75)
        self.uses = 2
        self.name = 'SourStraws'

    def genModif(self):
        self.modif = uniform(1, 1.75)
        return self.modif
