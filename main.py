from NPCS import *
from Weapons import *
import Home
import Player

def main():
    #weapons
    cb = ChocolateBars.ChocolateBars()
    nb = NerdBomb.NerdBomb()
    hk = HersheyKisses.HersheyKisses()
    ss = SourStraws.SourStraws()

    # mess with weapons
    print(cb.getUses())
    print(nb.getUses())
    print(hk.getUses())
    print(ss.getUses())

    # monsters
    gh = Ghouls.Ghouls()
    pr = Person.Person()
    vp = Vampire.Vampire()
    ww = Werewolves.Werewolves()
    zb = Zombie.Zombie()

    # mess with monsters
    monstList = [gh,pr,vp,ww,zb]
    for mst in monstList:
        hp = mst.getHP()
        print('Health: {}'.format(hp))
        at = mst.genAttack()
        print('attack gend: {}'.format(at))
    # home
    hm = Home.Home()
    p = Player.Player()

    for w in p.getInventory():
        n = w.getName()
        m = w.genModif()
        print('weapon: {name}, modifier: {modif}'.format(name=n, modif=m))


if __name__ == "__main__":
    main()
