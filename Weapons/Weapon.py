from random import *

class Weapon(object):

    ''' base weapons class. '''

    def __init__(self):
        self.modif = 0
        self.uses = 0 # million
        self.name = 'HersheyKisses'

    def getUses(self):
        return self.uses

    def getName(self):
        return self.name

    def getModif(self):
        return self.modif

    def setUses(self, uses):
        self.uses = uses

    def setModif(self, modif):
        self.modif = modif

    def genModif(self):
        pass
