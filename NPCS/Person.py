from Observable import *
from NPCS.NPC import *

class Person(NPC):

    '''Persons help you by giving you candy. Each piece of candy increases your
    health by 1 point. A person can give you 1 piece of candy per turn. We could
    see this "helping" from the person as an attack with a negative attack value.
    Persons have 100 health and are not harmed by your attacks.'''

    def __init__(self):
        NPC.__init__(self)
        self.attack = -1
        self.hp = 100
        self.immune = ['SourStraws','ChocolateBars','NerdBombs'] # random choice to give player maybe?
        self.weakTo = []
        self.name = "Person"

    def genAttack(self):
        return self.attack
