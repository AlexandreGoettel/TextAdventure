class Player:
    def __init__(self, health, position, inventory=[], maxHealth=-1, maxInventory=3, gold=0):
        if maxHealth == -1:
            self.maxHealth = health
        else:
            self.maxHealth = maxHealth
        self.health = health
        self.x, self.y = position
        self.inventory = inventory
        self.maxInventory = maxInventory
        self.gold = gold
    
    def getPosition(self):
        return [self.x, self.y]
    
    def changeHealth(self, dHealth):
        self.health = min(max(0, self.health + dHealth), self.maxHealth)
    
    def move(self, direction):
        if direction.lower() == "north":
            self.y += 1
        elif direction.lower() == "south":
            self.y -= 1
        elif direction.lower() == "west":
            self.x -= 1
        elif direction.lower() == "east":
            self.x += 1
        else:
            print("invalid direction: ", direction)
    
    def addItem(self, item):
        if len(self.inventory) >= self.maxInventory:
            print("Not enough space in your inventory!")
        else:
            self.inventory += [item]
        
    def removeItem(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print("Item {} was not in inventory".format(item.name))