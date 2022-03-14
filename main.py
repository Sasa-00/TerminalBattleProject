from classes.game import Person, Colors
from classes.magic import Spell

# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 13, 130, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 15, 150, "white")

#Instantiate Peope
player = Person(600, 70, 60, 35, [fire, blizzard, meteor, thunder, cure])
enemy = Person(1200, 65, 45, 25, [])

running = True
i = 0

print(Colors.FAIL + Colors.BOLD + "AN ENEMY ATTACKS!" + Colors.ENDC)

while running:
    print("===================================")
    player.chooseAction()
    choice = int(input("Choose action: ")) - 1

    if choice == 0:
        dmg = player.generateDamage()
        enemy.takeDamage(dmg)
        print("You attacked for", dmg, "points of damage.")
    elif choice == 1:
        player.chooseMagic()
        magicChoice = int(input("Choose magic: ")) - 1

        spell = player.magic[magicChoice]
        magic_dmg = spell.generateSpellDamage()

        currentMp = player.getMp()

        if spell.cost > currentMp:
            print(Colors.FAIL + "\nNot enough MP\n" + Colors.ENDC)
            continue

        player.reduceMp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(Colors.OKBLUE + "\n" + spell.name, "heals for", str(magic_dmg), "HP")
        else:
            enemy.takeDamage(magic_dmg)
            print(Colors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + Colors.ENDC)

    enemy_dmg = enemy.generateDamage()
    player.takeDamage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "points of damage")

    print("--------------------------------")
    print("Enemy HP is", Colors.FAIL + str(enemy.getHp()) + " / " + str(enemy.getMaxHp()) + Colors.ENDC)

    print("Your HP is", Colors.OKGREEN + str(player.getHp()) + " / " + str(player.getMaxHp()) + Colors.ENDC)
    print("Your MP is", Colors.OKBLUE + str(player.getMp()) + " / " + str(player.getMaxMp()) + Colors.ENDC)

    if enemy.getHp() == 0:
        print(Colors.OKGREEN + "You WIN!!!" + Colors.ENDC)
        running = False

    if player.getHp() == 0:
        print(Colors.FAIL + "Enemy has defeated you!!!" + Colors.ENDC)
        running = False

