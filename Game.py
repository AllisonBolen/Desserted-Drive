import math
from random import *

import Neighborhood
import Player


class Game(object):
    def __init__(self):
        self.player = Player.Player()
        self.nbHood = Neighborhood.Neighborhood(randint(2, 5))
        self.turn = True  # player = true monster = false   once anyone attacks you switch to what is itsnt now
        self.over = False

    def run(self):
        print("You need to save your friends!")
        print("You have to visit all {} of their houses and beat the monsters to save them!".format(
            self.nbHood.getGridSize()))
        choices = {"attack": self.doAttack,
                   "help": self.help,
                   "inventory": self.inventory,
                   "monsters": self.pmonsters,
                   "php": self.playerHP,
                   "travel": self.travel,
                   "hood": self.printGrid,
                   "loc": self.playerLoc,
                   "endturn": self.endTurn,
                   }

        self.printGrid()
        while (self.nbHood.getCount()):  # game isnt over
            while (self.turn):  # players turn
                command = input("What would you like to do? Command: ")
                requestCmd = command.split(' ', 1)[0]
                try:
                    choices[requestCmd.lower()]()
                except KeyError as e:
                    print("Thats not a valid command.")

            self.doMonstersTurn()
        print("YOU WIN: ZERO MONSTERS LEFT!")

    def endTurn(self):
        self.turn = False

    def split(self):
        x = self.player.getX()
        y = self.player.getY()
        personlist = []
        monlist = []

        for l in self.nbHood.getGrid()[x][y].getMonsters():
            if l.getName() == "Person":
                personlist.append(l)
            else:
                monlist.append(l)
        return [personlist, monlist]

    def doMonstersTurn(self):
        x = self.player.getX()
        y = self.player.getY()
        print("Player Health: {}".format(self.player.getHp()))
        if len(self.nbHood.getGrid()[x][y].getMonsters()) > 0:
            # are they people or are they monsters
            personlist, monlist = self.split()
            if len(monlist) > 0:
                self.getDamage(monlist)
            else:
                print("There are no monsters to attack you.")

            if len(personlist) > 0:
                self.getweapons(personlist)
                self.getHealth(personlist)
            else:
                print("There are no people to help you.")

            self.turn = True

    def gameOver(self):
        if self.player.getHp() <= 0:
            print("GAME OVER: You died.")
            raise SystemExit

    def getDamage(self, monlist):
        monster = monlist[randint(0, len(monlist) - 1)]
        damage = monster.genAttack()
        self.player.setHp(self.player.getHp() - damage)
        print("{mons} did {dam} damage to you.".format(mons=monster.getName(), dam=damage))
        self.gameOver()
        print("Player Health: {}".format(self.player.getHp()))

    def getweapons(self, personlist):  # adds one item tothe listif its not ten
        if len(self.player.getInventory()) < 10:
            wep = personlist[0].getImmune()[randint(0, 2)]
            self.player.appendInventory(wep)
            print("You have been given {} from a person in the house".format(wep))

    def getHealth(self, personlist):
        if self.player.getHp() < 125:
            count = len(personlist)
            self.player.setHp(self.player.getHp() + count)
            print("You have gained {} health points from the people in the house".format(count))

    def travel(self):
        dir = input(
            "\nWhat direction do you want to go: \n    North = N \n    South = S \n    West = W \n    East = E\n Direction: ").upper()

        if dir == "N" and self.canMove(dir):
            self.player.setX(self.player.getX() - 1)
        elif dir == "S" and self.canMove(dir):
            self.player.setX(self.player.getX() + 1)
        elif dir == "W" and self.canMove(dir):
            self.player.setY(self.player.getY() - 1)
        elif dir == "E" and self.canMove(dir):
            self.player.setY(self.player.getY() + 1)
        else:
            print("You cant move there.")
        self.printGrid()

    def doAttack(self):
        personlist, monlist = self.split()
        if len(monlist) > 0:
            # print inventory
            print("\n--------------------------------------------------------------")
            self.inventory()
            # print monsters
            print("\n--------------------------------------------------------------")
            self.pmonsters()
            print("\n--------------------------------------------------------------")
            x = self.player.getX()
            y = self.player.getY()
            w = input("What weapon would you like to attack with? type index: <num>")
            weapon = self.player.getInventory()[int(w)]

            count = 0
            for monster in self.nbHood.getGrid()[x][y].getMonsters():
                attackPoints = int(math.ceil(self.player.genAttack() * weapon.genModif()))
                if monster.getName() != "Person":
                    if weapon.getName() in monster.getWeakTo():
                        # do Damage
                        if monster.getName() == "Zombie" and weapon.getName() == "SourStraws":
                            attackPoints = 2 * attackPoints
                            monster.setHp((monster.getHp() - attackPoints))
                        elif monster.getName() == "Ghouls" and weapon.getName() == "NerdBomb":
                            attackPoints = 5 * attackPoints
                            monster.setHp((monster.getHp() - attackPoints))
                        else:
                            monster.setHp((monster.getHp() - attackPoints))
                        print("You did {ap} damage to {ms} with {ws}".format(ws=weapon.getName(), ap=attackPoints,
                                                                             ms=monster.getName()))
                        if monster.getHp() <= 0:
                            self.nbHood.getGrid()[x][y].killMonster(count)
                            print("You killed {ms}".format(ms=monster.getName()))
                    else:
                        print("{we} doesnt hurt {m}".format(we=weapon.getName(), m=monster.getName()))
                count = count + 1
            self.player.getInventory()[int(w)].setUses(self.player.getInventory()[int(w)].getUses() - 1)
            if self.player.getInventory()[int(w)].getUses() <= 0:
                self.player.removeWeap(int(w))
                print("You broke {}".format(weapon.getName()))
            self.turn = False
        else:
            print("There are no monsters to attack here.")

    def help(self):
        print("Inventory = all the weapons you hold and their uses left: (weapon name) (#) ")
        print("Attack = lists your inventory and asks for a weapon name")
        print("PHP = prints player HP")
        print(
            "Travel: will ask you what direction you want to go in: \n    North = N \n    South = S \n    West = W \n    East = E")
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
            if (self.player.getX() == 0):
                canMove = False
        elif cmd == "W":
            if (self.player.getY() == 0):
                canMove = False
        elif cmd == "S":
            if (self.player.getX() == len(self.nbHood.getGrid()[0]) - 1):
                canMove = False
        elif cmd == "E":
            if (self.player.getY() == len(self.nbHood.getGrid()[0]) - 1):
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
        personlist, monlist = self.split()
        print('\nPersons in House: {pnum}'.format(pnum=len(personlist)))
        for p in personlist:
            print('Name: {pname}, HP: {php}'.format(pname=p.getName(), php=p.getHp()))

        print('\nMonsters in House: {mnum}'.format(mnum=len(monlist)))
        for m in monlist:
            print('Name: {mname}, HP: {mhp}'.format(mname=m.getName(), mhp=m.getHp()))

    def playerHP(self):
        print('\nPlayers HP: {hp}'.format(hp=self.player.getHp()))

    def playerLoc(self):
        print("\nx: {x}, y: {y}".format(x=self.player.getX(), y=self.player.getY()))

    def globalCount():
        print("Global Monster Count: {}".format(nbHood.getCount()))
