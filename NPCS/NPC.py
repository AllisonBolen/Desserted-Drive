from Observable import *

''' Base NPC: The base npc class is the parent to the mosnters that extend it.
They share the getters and setters and a base constructor. It extends the Observable
class and this passes those methods down too. '''
class NPC(Observable):

    ''''
    makes Observable visable
    creates an attack - randomly genereated depending on the monster
    creates hp - randomly genereated depending on the monster
    creates a list of weapons the monster is not affected by - different for every mosnter
    creates a list of what the mosnter is weak to different for every monster
    creates a name for the monster - different for every monster
    '''
    def __init__(self):
        Observable.__init__(self)
        self.attack = 0
        self.hp = 0
        self.immune = []
        self.weakTo = []
        self.name = ""

    ## getters
    ''' returns the monsters attack as an integer'''
    def getAttack(self):
        return self.attack
    ''' returns the monsters Hp as an integer'''
    def getHp(self):
        return self.hp
    '''returns the list of strings of names of the weapons the monster is weak to'''
    def getImmune(self):
        return self.immune
    ''' returns the list of the names of weapons the monster is weak to'''
    def getWeakTo(self):
        return self.weakTo
    '''returns the name of the monster as a string'''
    def getName(self):
        return self.name

    # setters
    '''sets the monsters Hp to the int sent in'''
    def setHp(self, hp):
        self.hp = hp

    '''
    randomly selects an attack modifier for the mosters when called
    returns int
    '''
    def genAttack(self):
        pass
