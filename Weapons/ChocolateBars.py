from random impirt *

class ChocolateBars(object):

    ''' ChocolateBars modify the players attack by between 2 - 2.4.
    They are usable 4 times. '''

    def __init__(self):
        self.modif = uniform(2, 2.4)
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
        self.modif = uniform(2, 2.4)
        return self.modif
