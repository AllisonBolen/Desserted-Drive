from random import *

class HersheyKisses(object):

    ''' HersheyKisses are the basic weapon. No one ever runs out
    of HersheyKisses. Unfortunately they have an attack modifier of 1. '''

    def __init__(self):
        self.modif = 1
        self.uses = 1000000000 # million
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
        self.modif = 1
        return self.modif
