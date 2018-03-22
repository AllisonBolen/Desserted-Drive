from Home import *


class Neighborhood(Observer):
    ''' The neighborhood is made up of homes laid out in a grid. When created,
     the neighborhood should automatically build houses and attach them to
     one another in a grid. The size of the grid is set when the
     neighborhood is created.
        '''
    
    '''
    Initializes the Observer and creaets the grid and the count for the number of monsters
    Param:
      gridSize - The size of the grid
    return:
      nothing
    '''
    def __init__(self, gridSize):
        Observer.__init__(self)
        self.count = 0  # mosnter count of all the houses
        self.grid = self.populateHood(gridSize)  # need to popualte with houses in each grid space

    '''
    Populates the neighborhood with homes and puts monsters in those homes while increasing 
    the count.
    Param:
      size - the size of the grid
    return:
      neigh - returns the grid with the homes and monsters in it.
    '''
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

    '''
    Getter for the Grid size
    return:
      len(self.grid)**2 - len of the grid size squarerooted   
    '''
    def getGridSize(self):
        return len(self.grid) ** 2

    '''
    Getter for the count, or the number of monsters left.
    return:
      count - number of monsters left in game
    '''
    def getCount(self):
        return self.count

    '''
    Setter sets the count to an integer.
    Param:
      num - an integer value
    return:
      nothing
    '''
    def setCount(self, num):
        self.count = num

    '''
    Getter for grid.
    return:
      grid - how big the grid is and what it looks like
    '''
    def getGrid(self):
        return self.grid

    '''
    Setter for Grid.
    Param:
      g - an integer value
    return:
      nothing
    '''
    def setGrid(self, g):
        self.grid = g

    '''
    This method updates the count when the number of monsters changes
    return:
      nothing
    '''
    def update(self):
        self.count = self.count - 1
