from random import *

from NPCS.NPC import *


class Vampire(NPC):
    ''' Vampires attack at a rate of 10-20 HP per turn. They are not harmed by
    ChocolateBars. Start with 100-200 HP. '''

    def __init__(self):
        NPC.__init__(self)
        self.attack = randint(10, 20)
        self.hp = randint(100, 200)
        self.immune = ['ChocolateBars']  # immune its not hurt by
        self.weakTo = ['SourStraws', 'HersheyKisses', 'NerdBomb']
        self.name = "Vampire"

    # helper funcs
    def genAttack(self):
        self.attack = randint(10, 20)
        return self.attack
