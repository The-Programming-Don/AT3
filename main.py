from player import Player
from item import Item
from location import parse_world_dsl, where_abouts, elfTile
from collections import OrderedDict
from Npc import Elf


# this is just a short method for getting player input
def get_player_input():
    return input("Action: ")


def get_actions(room, player):
    actions = OrderedDict()
    print("Choose an action: ")
    if player.inventory:
        add_action(actions, 'i', player.print_inventory, "Print inventory")
    if isinstance(room, elfTile):
        add_action(actions, 'b', player.Buy, "Buy")
    if where_abouts(room.x, room.y -1):
            add_action(actions, 'n', player.move_north, "Heading North")
    if where_abouts(room.x, room.y + 1):
            add_action(actions, 's', player.move_south, "Heading South")
    if where_abouts(room.x + 1, room.y):
            add_action(actions, 'e', player.move_east, "Heading East")
    if where_abouts(room.x -1, room.y):
            add_action(actions, 'w', player.move_west, "Heading West")
        
    return actions
#chosses which action
def choose_action(room, player):
    action = None
    while not action:
      available_actions = get_actions(room, player)
      action_input = input("Action: ")  
      print(action_input) 
      action = available_actions.get(action_input)
      if action:
        action()
      else:
        print("Invalid Action")



#actions adder function
def add_action(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action 
    print("{}: {}".format(hotkey, name))


player = Player("player")

# our play function    
while True:
    print("The Wizards Dungeon!")    
    parse_world_dsl()
    room = where_abouts(player.x, player.y)
    print(room.description())    
    choose_action(room, player)
    
    
    
    


