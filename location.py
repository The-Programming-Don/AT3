import imp
from player import Player


from player import Player
from item import Item
from Npc import NPC


class Location(Player, Item, NPC):
    def __init__(self, name, x, y, rooms_avaliable, description, hasitems, hasNpc):
        self.name = name
        self.x = x
        self.y = y
        self.rooms_avaliable = rooms_avaliable
        self.description = description
        self.hasItems = hasitems
        self.hasNpc = hasNpc
        self.items = [ ]
        self.character = []
        

        