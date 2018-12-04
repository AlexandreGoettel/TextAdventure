from NPC import NPC
import numpy as np
from objects import Object, Key
import os

class Room:
    def __init__(self, position, doors, description, loot=[], NPCs=[], lockedDoors=[]):
        self.position = position
        self.doors = doors
        self.description = description
        self.loot = loot #list of Object instances
        self.NPCs = NPCs #list of NPC instances
        self.lockedDoors = lockedDoors
    
    def addLoot(self, newLoot):
        self.loot += [newLoot]
    
    def removeLoot(self, oldLoot):
        if oldLoot in self.loot:
            self.loot.remove(oldLoot)
        else:
            print("If you see this message - you tried to remove loot from a room and it didn't work")
    
    def killNPC(self, deadNPC):
        if deadNPC in self.NPCs:
            for stuff in deadNPC.inventory:
                self.addLoot(stuff)
            self.NPCs.remove(deadNPC)
        else:
            print("NPC not in this room. Can't kill NPC")
    
    def unlockDoor(self, door):
        if door in self.lockedDoors:
            self.lockedDoors.remove(door)
        else:
            print("This door is already unlocked...")
    
    def saveRoom(self):
        if not os.path.exists("../world"):
            os.mkdir("../world")
        if not os.path.exists("../world/Rooms"):
            os.mkdir("../world/Rooms")
        np.save("../world/Rooms/{}_{}.npy".format(self.position[0], self.position[1]), np.array([self]))
    

def getRoom(position):
    return np.load("../world/Rooms/{}_{}.npy".format(position[0], position[1]))[0]


def initialiseDungeon():
    positions = [[0, 0], [0, 1], [1, 1]]
    for position in positions:
        if position == [0, 0]:
            room = Room(position, ["north"], "An empty room, filled with nothing but dust, dispair and the lack of content.")
        
        elif position == [0, 1]:
            key = Key([1, 1], ["east"], 0, "golden key", 5)
            rustySword = Object(3, "rusty sword", 1)
            skeleton = NPC("skeleton", 5, "hostile", greetings="clak-clap", deathrattle="The skeleton crumbles to dust, leaving a small pile with something shiny in it...", inventory=[key], equipment=[rustySword])
            room = Room(position, ["south", "east"], "Some unfortunate adventurers' remains lie on the ground of this suspiciously well-lit room.", NPCs=[skeleton])
        
        elif position == [1, 1]:
            gold = Object(0, "pile of gold", 100)
            room = Room(position, ["east", "west"], "A golden room, full of looot.", loot=[gold], lockedDoors=["east"])
        
        room.saveRoom()


if __name__ == "__main__":
    initialiseDungeon()