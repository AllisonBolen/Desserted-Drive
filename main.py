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
    print(gh.genAttack())
    print(vp.genAttack())
    print(ww.genAttack())
    print(zb.genAttack())

    print(pr.getHP())

    # home
    hm = Home.Home()
    p = Player.Player()


if __name__ == "__main__":
    main()
