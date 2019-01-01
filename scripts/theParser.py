class Parser:
    def __init__(self):
        self.input = input("What do you go? ")
    
    def processFightInput(self, player, NPC):
        #Takes input and interprets command as either "run" or as attacking the NPC with a weapon
        #Returns string "run" or the weapon (Object instance) used to attack
        pass