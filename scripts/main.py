import numpy as np
from player import Player
from objects import Object, Key
from room import initialiseDungeon, getRoom
from fighting import doFight


def doMovement(currentRoom, spacko):
    placeholderKey = Key([], [], 666, "placeholder", 1337)
    while True:
        doorString = ""
        for door in currentRoom.doors:
            doorString += ", {}".format(door)
        directionToMoveIn = input("Which door would you like to use? ({}) ".format(doorString[2:]))
        
        #Kill switch
        if directionToMoveIn == "kill":
            error
        
        if directionToMoveIn in currentRoom.doors:
            if directionToMoveIn in currentRoom.lockedDoors:
                print("This door is locked...")
                for item in spacko.inventory:
                    if type(item) == type(placeholderKey):
                        if item.position == currentRoom.position and directionToMoveIn in item.target:
                            print("You unlock the door with {}!".format(item.name))
                            currentRoom.unlockDoor(directionToMoveIn)
                            spacko.move(directionToMoveIn)
                if directionToMoveIn in currentRoom.lockedDoors:
                    print("You do not have the right key for this door. SAD!")
            else:
                spacko.move(directionToMoveIn)
            
            break
        else:
            print("Invalid direction, try again.")


def lootRoom(currentRoom, spacko):
    rightChoices = np.ones(len(currentRoom.loot))
    
    for iLoot in range(0, len(currentRoom.loot)):
        loot = currentRoom.loot[iLoot]
        choice = input("A quick search reveals {}, do you want to pick it up? (y/n) ".format(loot.name))
        if choice.lower() in ["y", "yes"]:
            print("You pick up {}.".format(loot.name))
            spacko.addItem(loot)
            currentRoom.removeLoot(loot)
        elif choice.lower() in ["n", "no"]:
            pass
        else:
            rightChoices[iLoot] = 0
            print("Invalid command")
    
    if 0 in rightChoices:
        return True
    return False


def resolveEncounter(spacko, currentRoom):
    currentNPCs = currentRoom.NPCs
    if len(currentNPCs) > 0:
        roomNPC = currentNPCs[0]
        print("A {} approaches! It is {} and greets you with: '{}'".format(roomNPC.name, roomNPC.attitude, roomNPC.greetings))
        #do fight
        if roomNPC.attitude.lower() == "hostile":
            doFight(spacko, roomNPC)
            if spacko.health == 0:
                print("You ded. GAME OVER. \n git gud scrub")
                return True
            else:
                print(roomNPC.deathrattle)
                currentRoom.killNPC(roomNPC)
    return False


def main():
    #Init dungeon
    initialiseDungeon()
    
    #Define starting player character
    rustySword = Object(3, "rusty sword", 1)
    spacko = Player(10, [0, 0], inventory=[rustySword])
    
    #main loop
    while True:
        #Get room info
        currentRoom = getRoom(spacko.getPosition())
        
        #Room description
        print(currentRoom.description)
        for door in currentRoom.doors:
            print("There is a door to the {}.".format(door))
        
        #Resolve encounter
        isDead = resolveEncounter(spacko, currentRoom)
        if isDead:
            return
        
        #Loot room
        lootingRoom = True
        while lootingRoom:
            lootingRoom = lootRoom(currentRoom, spacko)
        
        #Move to the next room
        doMovement(currentRoom, spacko)
        
        #WIN CONDITION!
        if spacko.getPosition() == [2,1]:
            print("Congratulations, you won!\n\n"*100)
            break
        
        currentRoom.saveRoom()
    


if __name__ == '__main__':
    main()