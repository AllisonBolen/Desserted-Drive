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
        print("\nYou need to save your friends!")
        print("\nYou have to visit all {hc} of their houses and beat all {mc} the monsters to save them!".format(hc=self.nbHood.getGridSize(), mc= self.nbHood.getCount()))
        choices = {"attack": self.doAttack,
                   "help": self.help,
                   "inventory": self.inventory,
                   "monsters": self.pmonsters,
                   "php": self.playerHP,
                   "travel": self.travel,
                   "hood": self.printGrid,
                   "loc": self.playerLoc,
                   "endturn": self.endTurn,
                   "globalcount": self.globalCount,
                   }

        self.printGrid()
        while (self.nbHood.getCount()):  # game isnt over
            while (self.turn):  # players turn

                command = input("\nWhat would you like to do? Command: ")
                requestCmd = command.split(' ', 1)[0]
                try:
                    choices[requestCmd.lower()]()
                except KeyError as e:
                    print("Thats not a valid command.")
            print("\n--------------------- Monsters Turn ---------------------\n")
            self.doMonstersTurn()
            print("\n---------------------- Heros Turn ----------------------\n")
        print("\nYOU WIN: ZERO MONSTERS LEFT!")

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
        self.playerHP()
        if len(self.nbHood.getGrid()[x][y].getMonsters()) > 0:
            # are they people or are they monsters
            personlist, monlist = self.split()
            if len(monlist) > 0:
                self.getDamage(monlist)
            else:
                print("There are no monsters to attack you.")

            if len(personlist) > 0:
                self.getHealth(personlist)
                self.getweapons(personlist)
            else:
                print("There are no people to help you.")
            self.playerHP()
            self.turn = True

    def gameOver(self):
        if self.player.getHp() <= 0:
            print("GAME OVER: You died.")
            raise SystemExit

    def getDamage(self, monlist):
        monster = monlist[randint(0, len(monlist) - 1)]
        damage = monster.genAttack()
        self.player.setHp(self.player.getHp() - damage)
        print("\n{mons} did {dam} damage to you.".format(mons=monster.getName(), dam=damage))
        self.gameOver()


    def getweapons(self, personlist):  # adds one item tothe listif its not ten
        if len(self.player.getInventory()) < 10:
            wep = personlist[0].getImmune()[randint(0, 2)]
            self.player.appendInventory(wep)
            print("\nYou have been given {} from a person in the house".format(wep))

    def getHealth(self, personlist):
        if self.player.getHp() < 125:
            count = len(personlist)
            self.player.setHp(self.player.getHp() + count)
            print("You have gained {} health points from the people in the house".format(count))

    def travel(self):
        dir = input(
            "\nWhat direction do you want to go: \n    North = N \n    South = S \n    West = W \n    East = E\n \nDirection: ").upper()

        if dir == "N" and self.canMove(dir):
            self.player.setX(self.player.getX() - 1)
        elif dir == "S" and self.canMove(dir):
            self.player.setX(self.player.getX() + 1)
        elif dir == "W" and self.canMove(dir):
            self.player.setY(self.player.getY() - 1)
        elif dir == "E" and self.canMove(dir):
            self.player.setY(self.player.getY() + 1)
        else:
            print("\nYou cant move there.")
        self.printGrid()

    def doAttack(self):
        personlist, monlist = self.split()
        if len(monlist) > 0:
            # print inventory
            self.inventory()
            # print monsters
            self.pmonsters()
            print("\n---------------------------- Attack -----------------------------")
            x = self.player.getX()
            y = self.player.getY()
            try:
                w = int(input("What weapon would you like to attack with? Type index: "))
            except ValueError as e:
                print("Thats not a valid command.")
            weapon = self.player.getInventory()[w]

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
                        print("\nYou did {ap} damage to {ms} with {ws}".format(ws=weapon.getName(), ap=attackPoints,
                                                                             ms=monster.getName()))
                        if monster.getHp() <= 0:
                            self.nbHood.getGrid()[x][y].killMonster(count)
                            print("You killed {ms}".format(ms=monster.getName()))
                    else:
                        print("\n{we} doesnt hurt {m}".format(we=weapon.getName(), m=monster.getName()))
                count = count + 1
            self.player.getInventory()[int(w)].setUses(self.player.getInventory()[int(w)].getUses() - 1)
            if self.player.getInventory()[int(w)].getUses() <= 0:
                self.player.removeWeap(int(w))
                print("\nYou broke {}".format(weapon.getName()))
            self.turn = False
        else:
            print("\nThere are no monsters to attack here.")

    def help(self):
        print("\n--------------------------- Help Menu -----------------------------------")
        print("Inventory = all the weapons you hold and their uses left: (weapon name) (#) ")
        print("Attack = lists your inventory and asks for a weapon name")
        print("PHP = prints player HP")
        print(
            "Travel: will ask you what direction you want to go in: \n    North = N \n    South = S \n    West = W \n    East = E")
        print("Hood = Print Neighborhood with monsters left in each house")

    def printGrid(self):
        print("\n--------------------------- Neighborhood -----------------------------------")
        dim = int((self.nbHood.getGridSize()) ** (0.5))
        header = "\t   "
        sep = "\t---"
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
            print("\t{index}|{num} ".format(index=i, num=numMs))

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
        print("\n--------------------------- Inventory -----------------------------------")
        for w in self.player.getInventory():
            n = w.getName()
            u = w.getUses()
            print('\tInventory Slot: {num}, Weapon: {name}, Uses: {uses}'.format(num=count, name=n, uses=u))
            count = count + 1

    def pmonsters(self):
        print("\n--------------------------- Occupants -----------------------------------")
        personlist, monlist = self.split()
        print('Persons in House: {pnum}'.format(pnum=len(personlist)))
        for p in personlist:
            print('\tName: {pname}, HP: {php}'.format(pname=p.getName(), php=p.getHp()))

        print('\nMonsters in House: {mnum}'.format(mnum=len(monlist)))
        for m in monlist:
            print('\tName: {mname}, HP: {mhp}'.format(mname=m.getName(), mhp=m.getHp()))

    def playerHP(self):
        print('\nHeros HP: {hp}'.format(hp=self.player.getHp()))

    def playerLoc(self):
        print("\nx: {x}, y: {y}".format(x=self.player.getX(), y=self.player.getY()))

    def globalCount():
        print("\nGlobal Monster Count: {}".format(nbHood.getCount()))
