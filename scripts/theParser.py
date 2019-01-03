class Parser:
    def __init__(self):
        self.actionDict = {"run":"run", "flee":"run", "retreat":"run", "attack":"hit", "hit":"hit"}
        self.enemyNames = ["enemy", "monster"]
    
    
    def getInput(self):
        self.raw_input = input("What do you do? ").lower()
        self.input = self.raw_input.split(" ")
        if "and" in self.input:
            print("Sorry bro, no *and*'s allowed!")
            self.getInput()
        elif "exit" in self.input:
            kill
    

    def processFightInput(self, player, NPC):
        #Takes input and interprets command as either "run" or as attacking the NPC with a weapon
        #Returns string "run" or the weapon (Object instance) used to attack
        playerTurn = True
        while playerTurn:
            self.getInput()
            #Make sure an action is well-defined
            actions = [self.actionDict[i] for i in self.input if i in self.actionDict.keys()]
            userActions = [i for i in self.input if i in self.actionDict.keys()]
            if len(actions) == 0:
                print("No valid actions recognised")
                continue
            elif len(actions) > 1:
                print("Too many actions: ", userActions)
                continue
            
            #Run like a bitch
            action = actions[0]
            if action == "run":
                return action
            
            #Make sure a target is well-defined
            targets = []
            if action == "hit":
                targets = [NPC for word in self.input if word in self.enemyNames + [NPC.name]]
                if len(targets)<1:
                    print("No valid target defined for action: ", userActions[0])
                    continue
                
                #spuck die Waffe aus
                #weapons = [weapon for weapon in player.inventory if weapon.weapontype in self.input]
                weapons = [weapon for weapon in player.inventory if weapon.name in self.raw_input]
                    
                
                
                if len(weapons) == 0:
                    print("No suitable weapon recognised")
                    continue
                elif len(weapons) > 1:
                    print("Too many weapons: ", [weapon.name for weapon in player.inventory if weapon.name in self.input])
                
                return weapons[0]