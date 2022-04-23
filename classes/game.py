import random
from .magic import Spell


# Definition colors class for console
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Definition class for player and enemy
class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generateDamage(self):
        return random.randrange(self.atkl, self.atkh)

    def takeDamage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxHp:
            self.hp = self.maxHp

    def getHp(self):
        return self.hp

    def getMaxHp(self):
        return self.maxHp

    def getMp(self):
        return self.mp

    def getMaxMp(self):
        return self.maxMp

    def reduceMp(self, cost):
        self.mp -= cost

    def chooseAction(self):
        i = 1
        print(Colors.OKBLUE + Colors.BOLD + "Actions" + Colors.ENDC)
        for action in self.actions:
            print("     " + str(i) + ":", action)
            i += 1

    def chooseMagic(self):
        i = 1
        print(Colors.OKBLUE + Colors.BOLD + "Magic" + Colors.ENDC)
        print(Colors.HEADER + "*** With white magic you heal yourself! ***" + Colors.ENDC)
        for spell in self.magic:
            print("     " + str(i) + ":", spell.name, "(cost:", str(spell.cost), ",type:", spell.type + ")")
            i += 1

