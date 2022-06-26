from player import Player
from item import Item
from location import Exit, Gauntlet_room, GhostRoom, KeyRoom, Pre_Exit, Rock_Room, parse_world_dsl, where_abouts, elfTile
from collections import OrderedDict
from Npc import Elf


# this is just a short method for getting player input
def get_player_input():
    return input("Action: ")



# this functinon processes what avaliable actions there are given room, items in invent, ruppes ect.
def get_actions(room, player):
    actions = OrderedDict()
    print("Choose an action: ")
    if isinstance(room, Exit):
        print("Congratulations Traveller! You did it! Enjoy freedom.")
        return
    if isinstance(room, KeyRoom):
        add_action(actions, "c", player.collect_key, "Collect The Wizards Key")
    if player.inventory:
        add_action(actions, 'i', player.print_inventory, "Print inventory")
    if isinstance(room, elfTile):
        add_action(actions, 'b', player.Buy, "Buy")       
        add_action(actions, "p", player.pick_up_rupee, "Pick up rupee")        
    if isinstance(room, Gauntlet_room):
        add_action(actions, "t", player.pick_up_gauntlet, "Take the Gauntlet")
        
    if isinstance(room, Pre_Exit):
        add_action(actions, "p", player.pick_up_rupee, "Pick up rupee")
        
    if where_abouts(room.x, room.y -1):
        if isinstance(room, GhostRoom):
                if player.search_for_staff() == True:
                    add_action(actions, 'c', player.move_north, "Cool Down the Fire Ghost with the Staff of Ice")
        else:
            add_action(actions, 'n', player.move_north, "Heading North")
    if where_abouts(room.x, room.y + 1):
        if isinstance(room, Pre_Exit) and player.allowplayerinroom == True:
            add_action(actions, 'U', player.move_south, "Use the Wizard Key to unlock the door")
        elif isinstance(room, Pre_Exit) and player.allowplayerinroom == False:
            pass            
        elif isinstance(room, Rock_Room) and player.hasGauntlet == True:
            add_action(actions, "d", player.destroy_Rock, "Destory the Rock with the gauntlet")
            
        elif isinstance(room, Rock_Room) and player.hasGauntlet == False:
            add_action(actions, "p", player.pick_up_rupee, "Pick up rupee")
            pass
        else:
            add_action(actions, 's', player.move_south, "Heading South")
    if where_abouts(room.x + 1, room.y):
            add_action(actions, 'e', player.move_east, "Heading East")
            
    if where_abouts(room.x -1, room.y):
            add_action(actions, 'w', player.move_west, "Heading West")
        
    return actions


#this function is the cream. it sets a none tpye variable as 'action'
#then within the while loop i am prining available actions to the user and getting their input.
#if the users input is valid the 'action' now becomes that and then we add () to execute the funciton
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



#this was created to help me create all the actions quickly
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
    
    
    
    


