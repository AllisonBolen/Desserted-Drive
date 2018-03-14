from random import *
from Weapons.Weapon import *

class HersheyKisses(Weapon):

    ''' HersheyKisses are the basic weapon. No one ever runs out
    of HersheyKisses. Unfortunately they have an attack modifier of 1. '''

    def __init__(self):
        Weapon.__init__(self)
        self.modif = 1
        self.uses = 1000000000 # million
        self.name = 'HersheyKisses'

    def genModif(self):
        self.modif = 1
        return self.modif
