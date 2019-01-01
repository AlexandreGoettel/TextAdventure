from theParser import Parser


def doFight(player, NPC):
    while player.health > 0 and NPC.health > 0:
        parser = Parser() #Parser immediately requests output from the player when initialised
        #Choice is either string "run" or an object instance: the weapon used for attack
        choice = parser.processFightInput(player, NPC)
        if choice == "run":
            player.health = 0
            print("RUN LIKE A BITCH, DIE LIKE A BITCH!")
        else:
            NPC.changeHealth(-choice.damage)
            print("You hit the {}, dealing {} damage.".format(NPC.name, player.inventory[0].damage))
            print("The {} hits you, dealing {} damage.".format(NPC.name, NPC.equipment[0].damage))