import imp
from player import Player


from player import Player
from item import Item
from Npc import NPC


class Location(Player, Item, NPC):
    def __init__(self, name, rooms_avaliable, description):
        self.name = name
        self.rooms_avaliable = rooms_avaliable
        self.description = description
        

        