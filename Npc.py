import item


class NPC:
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC")

    def __str__(self):
        return self.name
        

class Fairy(NPC):
    def __init__(self):
        self.name = "Fairies"
        
    def talk(self):
        return """
        You wont get through this door young Adventurer
        """

class Ghost(NPC):
    def __init__(self):
        self.name = "The Fire Ghost"
        self.inventory = []

class Elf(NPC):
    def __init__(self):
        self.name = "The Jailed Elf"
        self.inventory = [item.Staff()]
        self.rupee = 0

