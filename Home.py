from random import *

from NPCS import *
from Observable import *
from Observer import *


class Home(Observable, Observer):
    '''Homes are full of 0-10 monsters. These do not need to be
    the same type of monster, in fact, some homes may have all types
    of monsters living within. The population of the homes is randomly
    generated when the home is created. The home should observe the monsters
    living within, and change the population if notified of some event.'''

    '''
    Initializes the Observables and the Observers while populating the 
    house with monsters.
    return:
      nothing
    '''
    def __init__(self):
        Observable.__init__(self)
        Observer.__init__(self)
        self.monsters = self.populateHouse()
        # list of Observable stuff

    '''
    Populates the house with a random amount of monsters and creates an Observer
    to watch what happens to them.
    return:
      monst - the list of monsters in the house
    '''
    def populateHouse(self):
        monst = []
        numMonst = randint(0, 10)
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

    '''
    Getter for a monster
    return:
      the monster
    '''
    def getMonsters(self):
        return self.monsters

    '''
    Getter for the number of monsters in the house that are not a Person
    return:
      count - number of monsters that are not a person
    '''
    def getNumMonsters(self):
        count = 0
        for monst in self.monsters:
            if monst.getName() not in ["Person"]:
                count = count + 1
        return count

    '''
    This method removes the monster and then replaces it with a Person
    then updates the house
    return:
      nothing
    '''
    def killMonster(self, monstIndex):
        del self.monsters[monstIndex]
        self.addPerson(monstIndex)
        self.update()

    '''
    This method creates a person and adds it to the house. It will insert the Person
    at the monster's index.
    return:
      nothing
    '''
    def addPerson(self, indx):
        npr = Person.Person()
        npr.add_observer(self)
        self.monsters.insert(indx, npr)

    '''
    This method updates the house with anything that changed.
    return:
      nothing
    '''
    def update(self):
        self.notify()
