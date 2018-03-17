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
        self.turn = True  # player = true monster = false   once anyone attacks you switch to what is itsnt now
        self.over = False

    def run(self):
        choices = {"Attack": self.doAttack,
                   "Help": self.help,
                   "Inventory": self.inventory,
                   "Monsters": self.pmonsters,
                   "PHP": self.playerHP,
                   "Travel": self.travel,
                   "Hood": self.printGrid
                   }

        print("You need to save your friends!")
        print("You have to visit all {} of their houses to and beat the monsters to save them!".format(
            self.nbHood.getGridSize()))
        self.printGrid()
        while (self.nbHood.getCount()):  # game isnt over
            while (self.turn):  # players turn
                command = input("What would you like to do?")
                requestCmd = command.split(' ', 1)[0]
                choices[requestCmd]()


    def travel(self):
        dir = input("What direction do you want to go: \n    North = N \n    South = S \n    West = W \n    East = E")
        self.player.getX()
        self.player.getY()
        print(self.player.getX())
        print(self.player.getY())
        if dir == "N" and self.canMove(dir):
            self.player.setX(self.player.getX()-1)
        elif dir =="S" and self.canMove(dir):
            self.player.setX(self.player.getX()+1)
        elif dir == "W" and self.canMove(dir):
            self.player.setY(self.player.getY()-1)
        elif dir =="E" and self.canMove(dir):
            self.player.setY(self.player.getY()+1)
        else:
            print("You cant move there.")
        self.printGrid()

    def doAttack(self):
        # print inventory
        print("--------------------------------------------------------------")
        self.inventory()
        # print monsters
        print("--------------------------------------------------------------")
        self.pmonsters()
        print("--------------------------------------------------------------")
        x = self.player.getX()
        y = self.player.getY()
        w = input("What weapon would you like to attack with? type index: <num>")
        weapon = self.player.getInventory()[int(w)]

        attackPoints = self.player.genAttack() * weapon.genModif()
        count = 0
        for monster in self.nbHood.getGrid()[x][y].getMonsters():
            print(monster.getName())
            if monster.getName() != "Person":
                if weapon.getName() in monster.getWeakTo():
                    # do Damage
                    if monster.getName() == "Zombie" and weapon.getName() == "SourStraws":
                        attackPoints = 2 * attackPoints
                        monster.setHp(monster.getHp() - attackPoints)
                    elif monster.getName() == "Ghouls" and weapon.getName() == "NerdBomb":
                        attackPoints = 5 * attackPoints
                        monster.setHp((monster.getHp() - attackPoints))
                    else:
                        monster.setHp((monster.getHp() - (attackPoints)))
                if monster.getHp() <= 0:
                    self.nbHood.getGrid()[x][y].killMonster(count)
                    print("You did {ap} damage to {ms} with {ws}".format(ws=weapon.getName(), ap=attackPoints,
                                                                         ms=monster.getName()))
                    print("You killed {ms}".format(ms=monster))
                else:
                    print("You did {ap} damage to {ms} with {ws}".format(ws=weapon.getName(), ap=attackPoints,
                                                                         ms=monster.getName()))
            count = count + 1
        self.player.getInventory()[int(w)].setUses(self.player.getInventory()[int(w)].getUses() - 1)
        if self.player.getInventory()[int(w)].getUses() <= 0:
            self.player.removeWeap(int(w))
            print("You broke {}".format(weapon.getName()))

    def help(self):
        print("Inventory = all the weapons you hold and their uses left: (weapon name) (#) ")
        print("Attack = lists your inventory and asks for a weapon name")
        print("PHP = prints player HP")
        print("Travel: will ask you what direction you want to go in: \n    North = N \n    South = S \n    West = W \n    East = E")
        print("Hood = Print Neighborhood with monsters left in each house")

    def printGrid(self):
        dim = int((self.nbHood.getGridSize()) ** (0.5))
        header = "   "
        sep = "---"
        for i in range(0, dim):
            header = header + "{} ".format(i)
            sep = sep + "--"
        print(header)
        print(sep)

        for i in range(0, dim):
            numMs = ""
            for j in range(0, dim):
                if self.player.getX() == i and self.player.getY() == j:
                    numMs = "{nums} P".format(nums=numMs)
                else:
                    numMs = "{nums} {monst}".format(nums=numMs, monst=self.nbHood.getGrid()[i][j].getNumMonsters())
            print("{index}|{num} ".format(index=i, num=numMs))

    def canMove(self, cmd):
        canMove = True
        if cmd == "N":
            if (self.player.getY() == 0):
                canMove = False
        elif cmd == "W":
            if (self.player.getX() == 0):
                canMove = False
        elif cmd == "S":
            if (self.player.getX() == (int((self.nbHood.getGridSize()) ** (0.5)) - 1)):
                canMove = False
        elif cmd == "E":
            if (self.player.getY() == (int((self.nbHood.getGridSize()) ** (0.5)) - 1)):
                canMove = False
        return canMove

    def inventory(self):
        count = 0
        for w in self.player.getInventory():
            n = w.getName()
            u = w.getUses()
            print('Inventory Slot: {num}, Weapon: {name}, Uses: {uses}'.format(num=count, name=n, uses=u))
            count = count + 1

    def pmonsters(self):
        x = self.player.getX()
        y = self.player.getY()
        personlist = []
        monlist = []
        for l in self.nbHood.getGrid()[x][y].getMonsters():
            n = l.getName()
            h = l.getHp()
            if n == "Person":
                personlist.append(l)
            else:
                monlist.append(l)
        print('Persons in House: {pnum}'.format(pnum=len(personlist)))
        for p in personlist:
            print('Name: {pname}, HP: {php}'.format(pname=p.getName(), php=p.getHp()))

        print('Monsters in House: {mnum}'.format(mnum=len(monlist)))
        for m in monlist:
            print('Name: {mname}, HP: {mhp}'.format(mname=m.getName(), mhp=m.getHp()))

    def playerHP(self):
        print('Players HP: {hp}'.format(hp=self.player.getHp()))
