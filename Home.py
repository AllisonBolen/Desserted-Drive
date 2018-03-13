from random import *
from Observable import *
from Observer import *


class Home(Observable, Observer):

    '''Homes are full of 0-10 monsters. These do not need to be
    the same type of monster, in fact, some homes may have all types
    of monsters living within. The population of the homes is randomly
    generated when the home is created. The home should observe the monsters
    living within, and change the population if notified of some event.'''

    def __init__(self):
        monsters = self.populateHouse()
        # list of Observable stuff

    def populateHouse(self):
        monst = []
        numMonst = randint(0,10)
        for m in range(0, numMonst):
            popList = ['Ghouls', 'Person', 'Vampire', 'Zombie', 'Werewolves']
            selected = randint(0, 3)
            monst.append(popList[selected])
        return monst
