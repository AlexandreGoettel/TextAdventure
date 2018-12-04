def doFight(player, NPC):
    while player.health > 0 and NPC.health > 0:
        choice = input("Would you like to hit the {} with your {} or would you like to run like a coward? (hit/run) ".format(NPC.name, player.inventory[0].name))
        if choice.lower() == "run":
            player.health = 0
            print("RUN LIKE A BITCH, DIE LIKE A BITCH!")
        elif choice.lower() == "hit":
            print("You hit the {}, dealing {} damage.".format(NPC.name, player.inventory[0].damage))
            NPC.changeHealth(-player.inventory[0].damage)
            print("The {} hits you, dealing {} damage.".format(NPC.name, NPC.equipment[0].damage))
        else:
            print("invalid command")
            continue