from random import *

class SourStraws(object):

    ''' SourStraws provide an attack modifier between 1 - 1.75.
    They can be used twice. '''

    def __init__(self):
        self.modif = uniform(1.5, 1.75)
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
        self.modif = uniform(1.5, 1.75)
        return self.modif
