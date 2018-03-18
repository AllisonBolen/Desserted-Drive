from Observable import *

class NPC(Observable):
    ''' Base class '''

    def __init__(self):
        Observable.__init__(self)
        self.attack = 0
        self.hp = 0
        self.immune = []
        self.weakTo = []
        self.name = ""
        self.alive = True

    # getters
    def getAttack(self):
        return self.attack

    def getHp(self):
        return self.hp

    def getImmune(self):
        return self.immune

    def getWeakTo(self):
        return self.weakTo

    def getName(self):
        return self.name

    def getAlive(self):
        return self.alive

    # setters
    def setWeakTo(self, weakTo):
        self.weakTo = weakTo

    def setAttack(self, a):
        self.attack = a

    def setHp(self, hp):
        self.hp = hp

    def setImmune(self, c):
        self.immune = c

    def setAlive(self, state):
        self.alive = state

    # helper funcs
    def genAttack(self):
        pass
