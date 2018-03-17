from random import *
from Observable import *
from NPCS.NPC import *

class Werewolves(NPC):

    ''' Werewolves attack at a rate of 0-40 HP per turn.
    They are not harmed by ChocolateBars or SourStraws. Start with 200 HP. '''

    def __init__(self):
        NPC.__init__(self)
        self.attack = randint(0, 40)
        self.hp = 200
        self.immune = ['ChocolateBars', 'SourStraws']  # immune its not hurt by
        self.weakTo = [ 'HersheyKisses', 'NerdBomb']
        self.name = "Werewolves"

    # helper funcs
    def genAttack(self):
        self.attack = randint(0, 40)
        return self.attack
