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
        print(f'Health: {hp}')
        at = mst.genAttack()
        print(f'attack gend: {at}')
    # home
    hm = Home.Home()
    p = Player.Player()


if __name__ == "__main__":
    main()
