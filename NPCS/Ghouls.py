from random import *

from NPCS.NPC import *


class Ghouls(NPC):
    ''' Ghouls attack at a rate of 15-30 HP per turn. They are harmed by
    all weapons, but receive 5X the attackers attack if attacked with NerdBombs.
    Start with 40-80 HP. '''

    def __init__(self):
        NPC.__init__(self)
        self.attack = randint(15, 30)
        self.hp = randint(40, 80)
        self.immune = []  # immune its not hurt by
        self.weakTo = ['ChocolateBars', 'SourStraws', 'HersheyKisses', 'NerdBomb']
        self.name = "Ghouls"

    # helper funcs
    def genAttack(self):
        self.attack = randint(15, 30)
        return self.attack
