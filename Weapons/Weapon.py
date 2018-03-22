''' base weapons class. This is the main weapon class that the weapon objects extend.
    The methods are usable on the objects that extend here. the player has a lsit of weapons to attack with'''
class Weapon(object):

    '''
    Initializes a weapon by giving it a name, it's uses, and it's modif
    return:
      nothing
    '''
    def __init__(self):
        self.modif = 0  #damage modifier
        self.uses = 0  #the amount of uses
        self.name = ''  #The name of weapon

    '''
    Getter for the weapons number of uses

    return:
      the integer of the weapons uses
    '''
    def getUses(self):
        return self.uses

    '''
    Getter for the Weapons name

    return:
      the string of the name of weapon
    '''
    def getName(self):
        return self.name

    '''
    Getter for the Weapons damage modifier

    return:
      the integer value of the modifier
    '''
    def getModif(self):
        return self.modif

    '''
    Setter for the weapons uses
      sets the uses to an integer value
    '''
    def setUses(self, uses):
        self.uses = uses

    '''
    Setter for the wapons damage modifier
      sets the modifier to an integer value
    '''
    def setModif(self, modif):
        self.modif = modif

    '''
    Generates the damage modifier. This will be used in other classes to
      tell how much damage a curtain weapon will do.
    '''
    def genModif(self):
        pass
