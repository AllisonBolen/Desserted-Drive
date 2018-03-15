from Observer import *
from Home import *

class Neighborhood(Observer):

    ''' The neighborhood is made up of homes laid out in a grid. When created,
     the neighborhood should automatically build houses and attach them to
     one another in a grid. The size of the grid is set when the
     neighborhood is created.
        '''
    def __init__(self, gridSize):
        Observer.__init__(self)
        self.count = 0 # mosnter count of all the houses
        self.grid = self.populateHood(gridSize) # need to popualte with houses in each grid space

    def populateHood(self, size):
        neigh = []
        for i in range(0, size):
            hood = []
            for j in range(0, size):
                newHome = Home()
                self.count = self.count + newHome.getNumMonsters()
                hood.append(newHome)
                newHome.add_observer(self)
            neigh.append(hood)
        return neigh

    def getCount(self):
        return self.count

    def setCount(self, num):
        self.count = num

    def getGrid(self):
        return self.grid

    def setGrid(self, g):
        self.grid = g

    def update(self):
        self.count = self.count - 1
