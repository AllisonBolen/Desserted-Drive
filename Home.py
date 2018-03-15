from random import *
from Observable import *
from Observer import *
from NPCS import *

class Home(Observable, Observer):

    '''Homes are full of 0-10 monsters. These do not need to be
    the same type of monster, in fact, some homes may have all types
    of monsters living within. The population of the homes is randomly
    generated when the home is created. The home should observe the monsters
    living within, and change the population if notified of some event.'''

    def __init__(self):
        Observable.__init__(self)
        Observer.__init__(self)
        self.monsters = self.populateHouse()
        # list of Observable stuff

    def populateHouse(self):
        monst = []
        numMonst = randint(0,10)
        for m in range(0, numMonst):
            popList = ['Ghouls', 'Person', 'Vampire', 'Zombie', 'Werewolves']
            selected = randint(0, 4)
            if popList[selected] == 'Ghouls':
                gh = Ghouls.Ghouls()
                gh.add_observer(self)
                monst.append(gh)
            elif popList[selected] == 'Person':
                pr = Person.Person()
                pr.add_observer(self)
                monst.append(pr)
            elif popList[selected] == 'Vampire':
                vm = Vampire.Vampire()
                vm.add_observer(self)
                monst.append(vm)
            elif popList[selected] == 'Zombie':
                zm = Zombie.Zombie()
                zm.add_observer(self)
                monst.append(zm)
            elif popList[selected] == 'Werewolves':
                ww = Werewolves.Werewolves()
                ww.add_observer(self)
                monst.append(ww)
        return monst

    def getMonsters(self):
        return self.monsters

    def getNumMonsters(self):
        count = 0
        for monst in self.monsters:
            if monst.getName() not in [ "Person" ]:
                count = count + 1
        return count

    def killMonster(self, monstIndex):
        del self.monsters[monstIndex]
        self.addPerson(monstIndex)
        self.update()

    def addPerson(self, indx):
        npr = Person.Person()
        npr.add_observer(self)
        self.monsters.insert(indx, npr)

    def update(self):
        self.notify()
