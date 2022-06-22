class Item:
    def __init__(self, type, description):
        self.type = type
        self.descriptions = description
        
class Rupee(Item):
    def __init__(self):
        self.type = "Red Rupee"
        self.description = "Its a shiny red gem, Sweet!"

class Staff(Item):
    def __init__(self):
        self.type = "Staff of Wind"
        self.description = "This staff emanates energy"

        self.value = 3
    
class Key(Item):
    def __init__(self):
        self.type = "Golden Key"
        self.description = "This Key looks valuable, maybe it opens something cool!"

class Gauntlet(Item):
    def __init__(self):
        self.type = "Gauntlet of Destruction"
        self.description = "This Gauntlet feels dangerous, I'm sure it's usefull."