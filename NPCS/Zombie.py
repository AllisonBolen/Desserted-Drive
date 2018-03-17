from random import *
from Observable import *
from NPCS.NPC import *

class Zombie(NPC):

    '''Zombies attack you at a rate of 0-10 HP per turn.
    Zombies are harmed by any weapon, but if attacked with SourStraws lose
    twice the number of points from an attack. Start with between 50 and 100 HP. '''

    def __init__(self):
        NPC.__init__(self)
        self.attack = randint(0, 10)
        self.hp = randint(50, 100)
        self.immune = [] # immune its not hurt by
        self.weakTo = ['ChocolateBars', 'SourStraws', 'HersheyKisses', 'NerdBomb']
        self.name = "Zombie"
        
    # helper funcs
    def genAttack(self):
        self.attack = randint(0, 10)
        return self.attack
