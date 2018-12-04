class NPC:
    def __init__(self, name, health, attitude, greetings="", deathrattle="", inventory=[], equipment=[], maxHealth=-1):
        self.name = name
        self.health = health
        self.attitude = attitude
        self.inventory = inventory
        self.equipment = equipment
        self.greetings = greetings
        self.deathrattle = deathrattle
        if maxHealth == -1:
            self.maxHealth = health
        else:
            self.maxHealth = maxHealth
            
    def changeHealth(self, dHealth):
        self.health = min(max(0, self.health + dHealth), self.maxHealth)
        
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