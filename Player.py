from random import *
from Weapons import *

'''This is you. You have a certain amount of HP, randomly generated
between 100 - 125. You also have an attack value, between 10-20.
You are able to hold 10 weapons; these are randomly generated and added
to your inventory when you are created.'''
class Player(object):

    ''' The constructor for the player classself.
        creates an inventory list
        creates the hp for the player randomly
        creates the attack randomly
        sets the x loctaion to 0
        sets the y location to 0
    '''
    def __init__(self):
        self.inventory = self.populateWeapons()
        self.hp = randint(300, 450)
        self.attack = randint(30, 45)
        self.xLoc = 0
        self.yLoc = 0

    ''' This populates the list of weapons for the palyer and returns it to the constructor. '''
    def populateWeapons(self):
        hk = HersheyKisses.HersheyKisses()  # always have hks
        weaps = [hk]
        for w in range(0, 9):
            popList = ['ChocolateBars', 'NerdBomb', 'SourStraws']
            selected = randint(0, 2)
            if popList[selected] == 'ChocolateBars':
                cb = ChocolateBars.ChocolateBars()
                weaps.append(cb)
            elif popList[selected] == 'NerdBomb':
                nb = NerdBomb.NerdBomb()
                weaps.append(nb)
            elif popList[selected] == 'SourStraws':
                ss = SourStraws.SourStraws()
                weaps.append(ss)
        return weaps

    # getters
    def getAttack(self):
        return self.attack

    def getHp(self):
        return self.hp

    def getX(self):
        return self.xLoc

    def getY(self):
        return self.yLoc

    # setters
    def setAttack(self, a):
        self.attack = a

    def setHp(self, hp):
        self.hp = hp

    def getInventory(self):
        return self.inventory

    def setX(self, xin):
        self.xLoc = xin

    def setY(self, yin):
        self.yLoc = yin

    ''' randomly selects a number to attack with '''
    def genAttack(self):
        self.attack = randint(30, 45)
        return self.attack

    ''' appends the weapons to the players inventory '''
    def appendInventory(self, weapon):
        if weapon == 'ChocolateBars':
            cb = ChocolateBars.ChocolateBars()
            self.inventory.append(cb)
        if weapon == 'NerdBombs':
            nb = NerdBomb.NerdBomb()
            self.inventory.append(nb)
        if weapon == 'SourStraws':
            ss = SourStraws.SourStraws()
            self.inventory.append(ss)

    ''' removes the weapon from the players inventory '''
    def removeWeap(self, index):
        del self.inventory[index]
