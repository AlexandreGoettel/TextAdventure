class Object:
    def __init__(self, damage, name, value):
        self.damage = damage
        self.name=name
        self.value = value
        
class Key(Object):
    def __init__(self, position, target, *args):
        Object.__init__(self, *args)
        self.position = position
        self.target = target