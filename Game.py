from NPCS import *
from Weapons import *
import Home
import Player
import Neighborhood
from random import *

class Game(object):

    def __init__(self):
        self.player = Player.Player()
        self.nbHood = Neighborhood.Neighborhood(randint(2, 5))
        self.turn = True # player = true monster = false   once anyone attacks you switch to what is itsnt now
        self.over = False

    def run(self):
        print("You need to save your friends!")
        print("You have to visit all {} of their houses to and beat the monsters to save them!".format(self.nbHood.getGridSize()))
        #while(nbHood.getCount!=0):
        self.printGrid()




    def printGrid(self):
        dim = int((self.nbHood.getGridSize()) ** (0.5))
        header = "   "
        sep = "---"
        for i in range(0, dim):
            header = header + "{} ".format(i)
            sep = sep + "--"
        print(header)
        print(sep)

        for i in range(0 , dim):
            numMs=""
            for j in range(0, dim):
                if self.player.getX() == i and self.player.getY() == j:
                     numMs = "{nums} P".format(nums=numMs)
                else:
                    numMs = "{nums} {monst}".format(nums=numMs, monst=self.nbHood.getGrid()[i][j].getNumMonsters())
            print("{index}|{num} ".format(index=i, num=numMs))
