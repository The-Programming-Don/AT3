from argparse import Action
from Npc import NPC
from player import Player
from item import Item
from location import Location

#instanciating locations
entrance = Location("entrance", 1, 0, "S E", "This seems to be the entrance room, its dark, mystical, weird magical totems are around \n and there is an ominous feeling about this place...", False, False)
exit = Location("Exit room", 3, 0, "N", "Its cold in here...there seems to be a trap door... the room is otherwise empty", False, False)
pre_exit = Location("Lower dungeon", 2,0,  "N" + "S", "Woah that door doesnt look like its going to open without a key \n there is a red gem... and what seems to be fairies... maybe i should go talk to them", True, True)
ghost_room = Location("Hallway", 1, 1, "W E N", "There is a scary ghost over there blocking the door, he looks rather timid, I can try talking to him... there is also a door just past him that isn't blocked", False, True)
gaunetlet_room = Location("Treasure room", 0, 1, "S", "There seems to be a gauntlet floating on a stone, it seems so mystical and there is writing on the stone \n it reads...'Gauntlet of Destruction'", True, False)
rock_room = Location("Dungeon's lair", 0, 1, "E S W", "Nice a red rupee!, there is a massive stone to my south that i cant get past, something is behind it \n but to me west there is a jail room... its getting scary in here", True, False)
jail = Location("Jail", 1, 3, "W", "It's dark, wet and cold in here, i can see a jail cell in the back corner, something is in there too...", False, True)
key_room = Location("The Wizards Vault", 2, 2, "N", "Woah there is a magical key, it looks important... something tells me i should'nt have made it this far.", True, False)




#instanciating the NPC's
ghost = NPC("The Firey Ghost", "'Grrr.. Get away from me! \n I will only let you past if you find something to cool me down'")
fairy = NPC("Fairies", "'hehehe... Not many people make it out of here, lets see if you're smart enough to open this door'")
elf = NPC("Elf", "'Pssssst... hey! ... Listen, if you give me 3 rupees i'll give ya this ice staff'")

pre_exit.character = [fairy]
ghost_room.character = [ghost]
jail.character = [elf]






#instanciating items
rupee1 = Item("rupee", "A shiny red gem")
rupee2 = Item("rupee", "A shiny red gem")
rupee3 = Item("rupee", "A shiny red gem")
key = Item("key", "its a key")
gauntlet = Item("Gauntlet of Destruction", "its a gauntlet")
staff = Item("staff", "its a magical staff")

pre_exit.items = [rupee1]
gaunetlet_room.items = [gauntlet]
rock_room.items = [rupee2]
key_room.items = [key]
jail.items = [rupee3, staff]




#Creating the 2D array in which all locations are mapped out
locationGrid = [
    [None,gaunetlet_room,None,None],
    [entrance,ghost_room,rock_room,jail],
    [pre_exit,None,key_room,None],
    [exit,None,None,None]   
]
locationGrid[0][1] = gaunetlet_room
locationGrid[1][0] = entrance
locationGrid[1][1] = ghost_room
locationGrid[1][2] = rock_room
locationGrid[1][3] = jail
locationGrid[2][0] = pre_exit
locationGrid[2][2] = key_room
locationGrid[3][0] = exit



# this function finds where the player is by returning the locationgrid
def where_abouts(x,y):
    if x < 0 or y < 0:
        return None
    try:
        return locationGrid[y][x]  
    except IndexError:
        return None  


#function makes it easy to aslways know what rooms are avaliable based on current location
def directions_avaliable():
    if player.current_room == gaunetlet_room:
        options = gaunetlet_room.rooms_avaliable
    if player.current_room == entrance:
        options = entrance.rooms_avaliable
    if player.current_room == ghost_room:
        options = ghost_room.rooms_avaliable
    if player.current_room == rock_room:
        options = rock_room.rooms_avaliable
    if player.current_room == jail:
        options = jail.rooms_avaliable
    if player.current_room == pre_exit:
        options = pre_exit.rooms_avaliable
    if player.current_room == key_room:
        options = key_room.rooms_avaliable
    if player.current_room == exit:
        options = exit.rooms_avaliable


    return options



# The frist user input
introduction = input("Hello, Enter the name of your character: ")

player = Player(introduction)
player.current_room = entrance
nextRoom = " "
'''
def options_avalible():
    print("You are now in the " + player.current_room.name + "\n" + player.current_room.description)

    if player.current_room.hasItems == True and player.current_room.hasNpc == False:
        print(player.current_room.items[0].description)
        nextRoom  = str(input("What would you like to do now?: Go " + (directions_avaliable()) + "\n" + player.current_room.items[0].type + "    type collect"))
    if player.current_room.hasItems == False and player.current_room.hasNpc == False:
        nextRoom  = str(input("What would you like to do now?: Go " + (directions_avaliable()))) 
    if player.current_room.hasItems == True and player.current_room.hasNpc == True:
        print(player.current_room.items[0].description)
        nextRoom  = str(input("What would you like to do now?: Go " + (directions_avaliable()) + "\n" + player.current_room.items[0].type + "    type collect" + "\n" + player.current_room.character[0].name + "    type talk"))
    return nextRoom
'''

def get_player_input():
    return input("Action: ")

def userInput():    
    if action_input == "I" or action_input == "i":
        print("Inventory: ")
        for item in player.inventory:
            print('*' + str(item))
    if action_input == "S" or action_input == "s":
        player.move_south()
    if action_input == "N" or action_input == "n":
        player.move_north()
    if action_input == "E" or action_input == "e":
        player.move_east()
    if action_input == "W" or action_input == "w":
        player.move_west()

    
while True:
    room = where_abouts(player.x, player.y)
    print(room.description)
    action_input = get_player_input()
    userInput()

'''
while True:
    try:
         
        nextRoom  = str(input("Where you like to go now?: " + (directions_avaliable())))
        if nextRoom == 'S':
            player.current_room = pre_exit
            break
        if nextRoom == 'E':
            player.current_room = ghost_room
            break
        else:
            print("That option isnt avaliable, try again.")
            continue
    except ValueError:
        print("That option isnt avaliable, try again.")
        continue
   
while True:
    try:
        print("You are now in the " + player.current_room.name + "\n" + player.current_room.description)
        if player.current_room.hasItems == True:
                print ("--> " + player.current_room.items[0].type + "              type 'collect'")
        if player.current_room.hasNpc == True:
                print("talk to " + player.current_room.character[0].name + "              type 'talk'")
        nextRoom  = str(input("What would you like to do now?: " + (directions_avaliable())))
        if nextRoom == 'S':
            player.current_room = pre_exit
            break
        if nextRoom == 'E':
            player.current_room = ghost_room
            break
        if nextRoom == 'talk':
            print(player.current_room.character[0].talk)
        if nextRoom == 'collect':
            print("You aquired a " + player.current_room.items[0].type)
            player.inventory = (player.current_room.items[0])
        else:
            print("That option isnt avaliable, try again.")
            continue
    except ValueError:
        print("That option isnt avaliable, try again.")
        continue
'''
